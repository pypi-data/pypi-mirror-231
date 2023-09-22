# genexpsim: Simulation of gene expression for single or multiple cells
# Copyright 2021-2023 Robert Wolff <mahlzahn@posteo.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from enum import IntEnum
from array import array
import matplotlib.pyplot as plt

class Process(IntEnum):
    DNA_INACTIVATION = 0
    DNA_ACTIVATION = 1
    RNA_TRANSCRIPTION = 2
    RNA_DEGRADATION = 3
    PROTEIN_TRANSLATION = 4
    PROTEIN_DEGRADATION = 5
    DNA_INA = 0
    DNA_ACT = 1
    RNA_TRA = 2
    RNA_DEG = 3
    PRO_TRA = 4
    PRO_DEG = 5

ProcessLabels=['DNA inactivation', 'DNA activation', 'mRNA transcription',
        'mRNA degradation', 'protein translation', 'protein degradation']

ProcessShortLabels=['DNA inact.', 'DNA act.', 'mRNA transcr.',
        'mRNA degrad.', 'protein transl.', 'protein degrad.']

class Level(IntEnum):
    ACTIVE_GENES = 0
    RNA_COUNT = 1
    PROTEIN_COUNT = 2
    DNA = 0
    RNA = 1
    PRO = 2

LevelLabels=['active alleles', 'mRNA count', 'protein count']

class GES:
    """A class for gene expression simulation"""
    def __init__(self, duration=24, seed=None, verbose=None):
        """
        ----------
        Parameters
        ----------
        duration: float
            The duration of simulation in hours (default: 24)
        seed: int, None
            The seed used for the random generator, None for random seed (default:
            None)
        verbose: int
            The level of verbosity, 0 or None for quietness (default: None)
        """
        self.duration = duration
        self.seed = seed
        if seed == None:
            seed_sequence = np.random.SeedSequence()
            self.seed_sel = seed_sequence.generate_state(1)[0]
        else:
            self.seed_sel = self.seed
        self.rng = np.random.default_rng(self.seed_sel)
        self.verbose = verbose
        self.constants_initialised = False

    def __repr__(self):
        return (f'genexpsim.GES(duration={self.duration}, seed={self.seed_sel}, '
                f'verbose={self.verbose})')

    def init_constants(self, koff, kon, km, gm, kp, gp, Ngc=2, ng0=None, nm0=None,
            np0=None):
        """Initialises the constants for the initial levels and rates calculation

        This function might be overwritten by your own subclasses to allow
        different start settings or rates calculation.
        ----------
        Parameters
        ----------
        koff: float
            rate of DNA inactivation per hour per active gene
        kon: float
            rate of DNA activation per hour per inactive gene
        km: float
            rate of mRNA transcription per hour per active gene
        gm: float
            rate of mRNA degradation per hour per mRNA molecule
        kp: float
            rate of protein translation per hour per mRNA molecule
        gp: float
            rate of protein degradation per hour per protein molecule
        Ngc: int
            number of gene copies (default: 2)
        ng0: int or None
            number of active genes at start. If None, then randomly chosen
            depending on Ngc, koff and kon. Has to be <= Ngc (default: None)
        nm0: int or None
            number of mRNA molecules at start. If None, then randomly chosen
            depending on parameters ng0, km and gm. (default: None)
        np0: int or None
            number of protein molecules at start. If None, then randomly chosen
            depending on parameters nm0, kp and gp. (default: None)
        """
        self.koff = np.abs(koff)
        self.kon = np.abs(kon)
        self.km = np.abs(km)
        self.gm = np.abs(gm)
        self.kp = np.abs(kp)
        self.gp = np.abs(gp)
        self.Ngc = Ngc
        self.ng0 = ng0
        self.nm0 = nm0
        self.np0 = np0
        self.constants_initialised = True

    def init_levels(self):
        """Initializes the DNA, mRNA and protein levels

        This function might be overwritten by your own subclasses to allow
        different start settings or adding levels.
        """
        self.levels = []
        for i in np.arange(len(Level)):
            self.levels.append(array('i'))
        self.levels_now = len(Level) * [None]
        # Simulate number of active genes on according to binomial distribution
        # with probability p = kon / (kon + koff)
        if (self.koff + self.kon == 0):
            ngp = 0
        else:
            ngp = self.kon / (self.kon + self.koff)
        ngm = self.Ngc * ngp
        if self.ng0 == None:
            ng0 = self.rng.binomial(self.Ngc, ngp)
        else:
            ng0 = self.ng0
        self.levels_now[Level.ACTIVE_GENES] = ng0
        self.levels[Level.ACTIVE_GENES].append(ng0)
        # Simulate number of mRNA molecules according to number of expected number
        # of active genes ngm = Ngc * koff / (kon + koff) and rates km and gm with
        # Poisson distribution
        if self.nm0 == None:
            if self.gm == 0:
                nm0 = 0
            else:
                nmm = ngm * self.km / self.gm
                nm0 = self.rng.poisson(nmm)
        else:
            nm0 = self.nm0
        self.levels_now[Level.RNA_COUNT] = nm0
        self.levels[Level.RNA_COUNT].append(nm0)
        # Simulate number of protein molecules according to number of mRNA
        # molecules nm0, and rates kp and gp with Poisson distribution
        if self.np0 == None:
            if self.gp == 0:
                np0 = 0
            else:
                npm = nmm * self.kp / self.gp
                np0 = self.rng.poisson(nm0 * self.kp / self.gp)
        else:
            np0 = self.np0
        self.levels_now[Level.PROTEIN_COUNT] = np0
        self.levels[Level.PROTEIN_COUNT].append(np0)

    def init_rates(self):
        """Initializes the rates"""
        self.rates = []
        self.rates_var = []
        for i in np.arange(len(Process)):
            self.rates.append(array('f'))
            self.rates_var.append(array('f'))
        self.new_rates()

    def init(self):
        """Initializes the simulation
        ------
        Raises
        ------
        RuntimeError:
            If the constants have not been initialised with init_constants(...)
        """
        if not self.constants_initialised:
            raise RuntimeError('The function init_constants has not been executed \
                    before run')
        self.time_now = 0.
        self.times = array('f', [0.])
        self.events = array('b')
        self.init_levels()
        self.init_rates()

    def new_levels(self, process=None):
        """Calculates the new levels in Level for a given time point and process

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent processes. Access to current time with self.time_now,
        rates with self.rates_now and to levels with self.levels_now.
        ----------
        Parameters
        ----------
        process: int
            The process which shall be executed. One of the six processes in
            Process enum. If None then current levels are repeated.
        """
        if process == Process.DNA_INACTIVATION:
            if self.levels_now[Level.ACTIVE_GENES] > 0:
                self.levels_now[Level.ACTIVE_GENES] -= 1
        elif process == Process.DNA_ACTIVATION:
            if self.levels_now[Level.ACTIVE_GENES] < self.Ngc:
                self.levels_now[Level.ACTIVE_GENES] += 1
        elif process == Process.RNA_TRANSCRIPTION:
            if self.levels_now[Level.ACTIVE_GENES] > 0:
                self.levels_now[Level.RNA_COUNT] += 1
        elif process == Process.RNA_DEGRADATION:
            if self.levels_now[Level.RNA_COUNT] > 0:
                self.levels_now[Level.RNA_COUNT] -= 1
        elif process == Process.PROTEIN_TRANSLATION:
            if self.levels_now[Level.RNA_COUNT] > 0:
                self.levels_now[Level.PROTEIN_COUNT] += 1
        elif process == Process.PROTEIN_DEGRADATION:
            if self.levels_now[Level.PROTEIN_COUNT] > 0:
                self.levels_now[Level.PROTEIN_COUNT] -= 1
        add_values(self.levels, self.levels_now)
    
    def new_rates(self):
        """Calculates the rates of the processes in Process for a given time point

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent rates. Access to current time with self.time_now, rates
        with self.rates_now and to levels with self.levels_now.
        """
        self.rates_now = [self.koff * self.levels_now[Level.ACTIVE_GENES],
            self.kon * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            self.km * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        add_values(self.rates, self.rates_now)

    def finalize(self, end_at_duration=True):
        """Finalizees the simulation if run until self.duration
        ----------
        Parameters
        ----------
        end_at_duration: bool
            If a final point for times, rates and levels is added at self.duration
            (default: True)
        """
        if end_at_duration:
            try:
                repeat_values(self.levels)
                del self.levels_now
            except AttributeError:
                pass
            try:
                repeat_values(self.rates)
                del self.rates_now
            except AttributeError:
                pass
            self.times.append(self.duration)
        try:
            del self.time_now
        except AttributeError:
            pass
        del self.rng, self.constants_initialised
    
    def run(self):
        """Executes the simulation
        ------
        Raises
        ------
        RuntimeError:
            If the constants have not been initialised with init_constants(...)
        """
        self.init()
        while True:
            abs_rates = np.abs(self.rates_now)
            total_rate = np.sum(abs_rates)
            if total_rate == 0:
                self.finalize(end_at_duration=False)
                break
            self.time_now += self.rng.exponential(scale=1/total_rate)
            if self.time_now > self.duration:
                self.finalize(end_at_duration=True)
                break
            process = self.rng.choice(np.arange(len(Process)),
                    p=np.divide(abs_rates, total_rate))
            self.events.append(process)
            self.new_levels(process)
            self.new_rates()
            # add time_now at the end such that levels and rates can use the
            # time difference self.time_now - self.times[-1] in their calculation
            self.times.append(self.time_now)

    def compress_rates_levels(self, dt):
        n_times = len(self.times)
        if len(self.rates[0]) != n_times or len(self.levels[0]) != n_times:
            print('Warning: rates or levels have been already compressed before')
            return
        rates_cs = np.column_stack(self.rates)
        rates = list(map(lambda r: array('f'), self.rates))
        levels_cs = np.column_stack(self.levels)
        levels = list(map(lambda l: array('i'), self.levels))
        for t in np.arange(0, self.duration + dt / 2, dt):
            i_t = np.argmax(np.greater_equal(self.times, t))
            add_values(rates, rates_cs[i_t])
            add_values(levels, levels_cs[i_t])
        self.rates = rates
        self.levels = levels

    def plot_rates(self, plot_filename=None, time=None):
        """Plots rates of the different processes
        ----------
        Parameters
        ----------
        plot_filename: str
            The name of the file where the plot is saved. If None, then it is not
            saved anywhere and the plot is done interactively (default: None)
        time: float
            The maximum time for the x-axis of the plot. If None, then the total
            duration of the simulation is used (default: None)
        """
        time = time if time else self.duration
        fig, ax = plt.subplots(3, sharex=True, tight_layout=True)
        labels = ProcessLabels
        if len(self.rates[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.rates[0]))
        for process in [Process.DNA_INA, Process.DNA_ACT]:
            ax[2].step(times, self.rates[process], label=labels[process],
                    where='post')
        for process in [Process.RNA_TRA, Process.RNA_DEG]:
            ax[1].step(times, self.rates[process], label=labels[process],
                    where='post')
        for process in [Process.PRO_TRA, Process.PRO_DEG]:
            ax[0].step(times, self.rates[process], label=labels[process],
                    where='post')
        for axi in ax:
            axi.legend()
            axi.set_ylabel('rate / h⁻¹')
            axi.grid(axis='x', which='major')
        plot_set_ax(ax[2], time)
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def plot_events_levels(self, plot_filename=None, time=None):
        """Plots events and levels of active genes, mRNA molecules and proteins
        ----------
        Parameters
        ----------
        plot_filename: str
            The name of the file where the plot is saved. If None, then it is not
            saved anywhere and the plot is done interactively (default: None)
        time: float
            The maximum time for the x-axis of the plot. If None, then the total
            duration of the simulation is used (default: None)
        """
        time = time if time else self.duration
        fig, ax = plt.subplots(3, 1, sharex=True, tight_layout=True)
        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        ax[0].step(times, self.levels[Level.PRO], c='tab:red', where='post')
        ax[0].set_ylabel(LevelLabels[Level.PRO])
        ax[0].grid(axis='x', which='major')
    
        ax[1].step(times, self.levels[Level.RNA], where='post',
                visible=False)
        ymax = ax[1].get_ylim()[1]
        Ngc = np.max(self.levels[Level.DNA])
        scale_level = ymax / (Ngc + 1)
        ax[1].step(times, np.multiply(self.levels[Level.DNA], scale_level),
                c='tab:orange', where='post')
        ax[1].step(times, self.levels[Level.RNA], c='tab:blue', where='post')
        ax[1].set_ylabel(LevelLabels[Level.RNA])
        secax = ax[1].secondary_yaxis('right',
                functions=(lambda y: y / scale_level, lambda y: y * scale_level))
        secax.set_ylabel(LevelLabels[Level.DNA])
        ax[1].grid(axis='x', which='major')
    
        ax[2].plot(self.times[1:len(self.events) + 1], self.events, '|',
                c='darkgreen')
        ax[2].set_yticks(np.arange(len(Process)))
        ax[2].set_yticklabels(ProcessShortLabels)
        plot_set_ax(ax[2], time)

        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def print_summary(self, print_filename=None, print_stdout=True):
        """Prints a summary of rates and levels
        ----------
        Parameters
        ----------
        print_filename: str
            The name of the file where the printout is saved. If None, then it is
            not saved anywhere (default: None)
        print_stdout: bool
            Whether the printout shall be done on stdout (defaut: True).
        """
        if print_filename:
            f = open(print_filename, 'w')
        elif not print_stdout:
            return
        def write(text):
            if print_filename:
                print(text, file=f)
            if print_stdout:
                print(text)

        if len(self.rates[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        write(f'count\toutrate\tinrate\tprocess')
        for process in Process:
            rate_mean = integrate(times, self.rates[process]) / self.duration
            count = self.events.count(process)
            write(f'{count:7d}\t{count/self.duration:7.2f}\t{rate_mean:7.2f}'
            + f'\t{Process(process).name}')

        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        write(f'mean\tstd\tlevel')
        for level in Level:
            level_mean = integrate(times, self.levels[level]) / self.duration
            level_std = np.sqrt(integrate(times,
                (self.levels[level] - level_mean) ** 2) / self.duration)
            write(f'{level_mean:7.2f}\t{level_std:7.2f}\t{Level(level).name}')
            #write(f'{level_std/level_mean:7.2f}')
        if print_filename:
            f.close()

def add_values(x, y):
    """Helper function to add list of values to given list of arrays
    ----------
    Parameters
    ----------
    x: list(array)
        The list of arrays where a list of values is going to be added to each
        array in the list
    y: list
        The list of values to be added. len(y) must be equal len(x)
    """
    list(map(lambda x, y: x.append(y), x, y))

def repeat_values(x):
    """Helper function to repeat last values for a given list of arrays
    ----------
    Parameters
    ----------
    x: list(array)
        The list of arrays where the last values are going to be added to each
        array in the list
    """
    list(map(lambda x: x.append(x[-1]), x))

def integrate(x, y, where='post'):
    """Integrates ydx
    ----------
    Parameters
    ----------
    x: list(float)
        The arguments x
    y: list(float)
        The values of the function y(x)
    where: {'pre', 'post', 'mid'}
        Defines where the steps should be placed (default: 'post'):
        * 'pre': The x value is continued constantly to the left from every x
        position, i.e. the interval (x[i-1], x[i]] has the value x[i].
        * 'post': The x value is continued constantly to the right from every x
        position, i.e. the interval [x[i], x[i+1]) has the value x[i].
        * 'mid': Steps occur half-way between the x positions.
    -------
    Returns
    -------
    integral: float
        Integral of the ydx
    """
    dx = np.subtract(x[1:], x[:-1])
    if where == 'pre':
        y = y[1:]
    elif where == 'mid':
        y = np.add(y[1:], y[:-1]) / 2
    elif where == 'post':
        y = y[:-1]
    else:
        raise ValueError('where needs to be \'pre\', \'mid\' or \'post\'')
    return np.sum(np.multiply(y, dx))

def differentiate(x, y, where='post'):
    """Differentiates dy/dx
    ----------
    Parameters
    ----------
    x: list(float)
        The arguments x
    y: list(float)
        The values of the function y(x)
    where: {'pre', 'post', 'mid'}
        Defines where the steps should be placed (default: 'post'):
        * 'pre': The x value is continued constantly to the left from every x
        position, i.e. the interval (x[i-1], x[i]] has the value x[i].
        * 'post': The x value is continued constantly to the right from every x
        position, i.e. the interval [x[i], x[i+1]) has the value x[i].
        * 'mid': Steps occur half-way between the x positions.
    -------
    Returns
    -------
    x, d: list(float), list(float):
        The new arguments x (with length = len(x) - 1) and differentiated d = dy/dx
    """
    dx = np.subtract(x[1:], x[:-1])
    dy = np.subtract(y[1:], y[:-1])
    if where == 'pre':
        x = x[1:]
    elif where == 'mid':
        x = np.divide(np.add(x[1:], x[:-1]), 2)
    elif where == 'post':
        x = x[:-1]
    else:
        raise ValueError('where needs to be \'pre\', \'mid\' or \'post\'')
    return x, np.divide(dy, dx)

def plot_set_ax(ax, time=None):
    ax.set_xlabel('time / h')
    if time:
        ax.set_xlim(0, time)
    if time > 60:
        ax.xaxis.set_minor_locator(plt.MultipleLocator(12))
        ax.xaxis.set_major_locator(plt.MultipleLocator(24))
    elif time > 30:
        ax.xaxis.set_minor_locator(plt.MultipleLocator(6))
        ax.xaxis.set_major_locator(plt.MultipleLocator(12))
    ax.grid(axis='x', which='major')
