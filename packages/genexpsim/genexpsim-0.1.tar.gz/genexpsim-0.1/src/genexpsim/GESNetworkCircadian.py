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
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import multiprocessing as mp

from .GES import *
from .GESCircadian import *

class GESNetworkCircadian(GES):
    def __init__(self, process, duration=24., seed=None, verbose=None, Ncells=100,
            square_length=1., random_cell_positions=True,
            neighbour_coupling_length=0.2, neighbour_coupling=0.01):
        """
        Parameters
        ----------
        process: genexpsim.Process
            The process for which the rate shall be variable (currently
            implemented: DNA_INACTIVATION, DNA_ACTIVATION, RNA_TRANSCRIPTION)
        duration: float
            The duration of simulation in hours (default: 24.0)
        seed: int
            The seed used for the random generator, None for random seed (default:
            None)
        verbose: int
            The level of verbosity, 0 or None for quietness (default: None)
        Ncells: int
            The number of cells in the network (default: 100)
        square_length: float
            The length of the square where the cells are placed randomly (default:
            1.0)
        random_cell_positions: bool
            If True, then cells are positioned randomly on square of length
            square_length, else on a grid, defined by Ncells. (default: True)
        neighbour_coupling_length: float
            The length of the coupling range for the cells interaction in the
            probability ~ exp(-distance/range) in the simulation of the
            neighbouring cells, in same unit as length (default: 0.2)
        neighbour_coupling: float
            The coupling constant for neighbouring, interacting cells (default:
            0.01)
        ------
        Raises
        ------
        ValueError:
            If given process is not implemented
        """
        if process not in [Process.DNA_INACTIVATION, Process.DNA_ACTIVATION,
                Process.RNA_TRANSCRIPTION]:
            raise ValueError(('Given process must be one of '
                'genexpsim.Process.DNA_INACTIVATION, '
                'genexpsim.Process.DNA_ACTIVATION, '
                'genexpsim.Process.RNA_TRANSCRIPTION.'))
        self.process = process
        self.Ncells = Ncells
        self.square_length = square_length
        self.random_cell_positions = random_cell_positions
        self.neighbour_coupling_length = neighbour_coupling_length
        self.neighbour_coupling = neighbour_coupling
        super().__init__(duration, seed, verbose)
        seed_sequence = np.random.SeedSequence(seed)
        self.seed_sel = seed_sequence.entropy
        [seed_sel_rng], self.cell_seeds = np.split(seed_sequence.generate_state(
            Ncells + 1), [1])
        self.rng = np.random.default_rng(seed_sel_rng)
    
    def __repr__(self):
        return (f'genexpsim.GESNetworkCircadian('
                f'process=genexpsim.Process.{Process(self.process).name}, '
                f'duration={self.duration}, seed={self.seed_sel}, '
                f'verbose={self.verbose}, Ncells={self.Ncells}, '
                f'square_length={self.square_length}, '
                f'random_cell_positions={self.random_cell_positions}, '
                f'neighbour_coupling_length={self.neighbour_coupling_length}, '
                f'neighbour_coupling={self.neighbour_coupling})')

    def init_constants(self, koff, kon, km, gm, kp, gp, w=None, dw=0, b=1, p=None,
            Ngc=2, ng0=None, nm0=None, np0=None, dt=None):
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
        w: float
            The parameter omega for the variable rate per hour. If None then set to
            2*pi/24, corresponding to a period of 24 hours (default: None)
        dw: float
            The standard deviation on w. If not 0, then w is randomly chosen
            with normal distribution around w (default: 0)
        b: float
            The parameter beta for the variable rate, must be in range [-1, 1]
            (default: 1)
        p: float or None
            The parameter phi for the variable rate. If None, then randomly chosen
            in [0, 2*pi] (default: None)
        Ngc: int
            The number of gene copies (default: 2)
        ng0: int or None
            The number of active genes at start. If None, then randomly chosen
            depending on Ngc, koff and kon. Has to be <= Ngc (default: None)
        nm0: int or None
            The number of mRNA molecules at start. If None, then randomly chosen
            depending on parameters ng0, km and gm. (default: None)
        np0: int or None
            The number of protein molecules at start. If None, then randomly chosen
            depending on parameters nm0, kp and gp. (default: None)
        dt: float or None
            The minimal resolution time in hours for the calculation of the thetas,
            must be > 0. If None, dt is set to np.pi / 120 / w corresponding to
            0.1 hours for a period of 24 hours. (default: None)
        ------
        Raises
        ------
        ValueError:
            If given b is not in [-1, 1]
        """
        if b < -1 or b > 1: # because else rate can become negative
            raise ValueError("b < -1 or b > 1")
        self.w = w
        self.dw = dw
        w_sel = w if w != None else 2 * np.pi / 24
        self.ws = self.Ncells * [w_sel] if dw == 0 else self.rng.normal(w_sel, dw,
                self.Ncells)
        self.dt = dt
        self.dt_sel = dt if dt else np.pi/120/w_sel # 0.1 h for a period of 24 h
        self.b = b
        self.p = p
        self.ps = self.Ncells * [p] if p != None else self.rng.uniform(0,
                2 * np.pi, self.Ncells)
        super().init_constants(koff=koff, kon=kon, km=km, gm=gm, kp=kp, gp=gp,
                Ngc=Ngc, ng0=ng0, nm0=nm0, np0=np0)

    def init_cells(self):
        """Initializes the cells with positions and simulation"""
        if self.random_cell_positions:
            self.x = self.rng.uniform(0, self.square_length, self.Ncells)
            self.y = self.rng.uniform(0, self.square_length, self.Ncells)
        else:
            nx = int(np.ceil(np.sqrt(self.Ncells)))
            ny = int(np.ceil(self.Ncells / nx))
            self.x = np.repeat(np.linspace(0, self.square_length, nx),
                    ny)[:self.Ncells]
            self.y = np.repeat([np.linspace(0, self.square_length, ny)], nx,
                    axis=0).flatten()[:self.Ncells]
        d = list(map(lambda xi, yi: np.sqrt(np.square(np.subtract(xi, self.x)) +
            np.square(np.subtract(yi, self.y))), self.x, self.y))
        neighbours_lower = self.rng.binomial(1, np.exp(-np.tril(np.divide(d,
            self.neighbour_coupling_length)))) - np.identity(self.Ncells,
                    dtype=int)
        self.neighbours = neighbours_lower.T * neighbours_lower
        #TODO: next two variables unused
        #neighbour_couplings = self.neighbour_coupling * self.neighbours
        #n_neighbours = np.sum(self.neighbours, axis=0)

        self.cells = []
        for i in np.arange(self.Ncells):
            if self.process == Process.DNA_ACTIVATION:
                cell = GESNetworkCircadianDNAActivationOneCell(self.duration,
                        self.cell_seeds[i], verbose=self.verbose)
            elif self.process == Process.DNA_INACTIVATION:
                cell = GESNetworkCircadianDNAInactivationOneCell(self.duration,
                        self.cell_seeds[i], verbose=self.verbose)
            elif self.process == Process.RNA_TRANSCRIPTION:
                cell = GESNetworkCircadianRNATranscriptionOneCell(self.duration,
                        self.cell_seeds[i], verbose=self.verbose)
            cell.init_constants(koff=self.koff, kon=self.kon, km=self.km,
                    gm=self.gm, kp=self.kp, gp=self.gp, Ngc=self.Ngc, w=self.ws[i],
                    dw=0, b=self.b, p=self.ps[i], ng0=self.ng0, nm0=self.nm0,
                    np0=self.np0)
            cell.init()
            self.cells.append(cell)

    def init_thetas(self):
        """Initializes the thetas"""
        self.thetas_now = -self.ps
        #self.thetas = []
        self.thetas_pre = []
        for i in np.arange(self.Ncells):
            #self.thetas.append(array('f'))
            #self.thetas[i].append(self.thetas_now[i])
            self.thetas_pre.append(array('f'))
            self.thetas_pre[i].append(self.thetas_now[i])

    def init_levels(self):
        """Initializes the DNA, mRNA and protein levels

        This function might be overwritten by your own subclasses to allow
        different start settings or adding levels.
        """
        self.levels = []
        self.levels_var = []
        for i in np.arange(len(Level)):
            self.levels.append(array('i'))
            self.levels_var.append(array('f'))
        self.new_levels()

    def init(self):
        """Initializes the simulation
        ------
        Raises
        ------
        RuntimeError:
            If the constants have not been initialised with init_constants(...)
        """
        self.events_cell = array('i')
        self.init_thetas()
        self.init_cells()
        super().init()

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
        levels = list(map(lambda c: c.levels_now, self.cells))
        self.levels_now = np.sum(levels, axis=0)
        add_values(self.levels, self.levels_now)
        add_values(self.levels_var, np.var(levels, axis=0))

    def new_rates(self):
        """Calculates the rates of the processes in Process for a given time point

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent rates. Access to current time with self.time_now, rates
        with self.rates_now and to levels with self.levels_now.
        """
        self.abs_rates_now = np.abs(list(map(lambda c: c.rates_now, self.cells)))
        self.rates_now = np.sum(self.abs_rates_now, axis=0)
        add_values(self.rates, self.rates_now)
        add_values(self.rates_var, np.var(self.abs_rates_now, axis=0))

    def finalize(self, end_at_duration=True):
        """Finalizees the simulation if run until self.duration
        ----------
        Parameters
        ----------
        end_at_duration: bool
            If a final point for times, rates, levels and thetas is added at
            self.duration (default: True)
        """
        del(self.thetas_now, self.abs_rates_now)
        repeat_values(self.levels_var)
        repeat_values(self.rates_var)
        super().finalize(end_at_duration=end_at_duration)

    def calculate_thetas(self):
        thetas = self.thetas_now
        for t in np.arange(self.dt_sel, self.duration + self.dt_sel, self.dt_sel):
            thetas = thetas + self.dt_sel * (self.ws + np.sum(
                list(map(lambda theta, neighbour:
                    neighbour * self.neighbour_coupling * np.sin(theta - thetas),
                    thetas, self.neighbours)), axis=0))
            add_values(self.thetas_pre, thetas)

    def run(self, cpu_count=None):
        """Executes the simulation
        ------
        Raises
        ------
        RuntimeError:
            If the constants have not been initialised with init_constants(...)
        ValueError:
            If given process is not implemented
        """
        self.init()
        self.calculate_thetas()

        list(map(lambda c: c[1].set_thetas_pre(self.thetas_pre[c[0]], self.dt_sel),
            enumerate(self.cells)))

        cpu_count = cpu_count if cpu_count else mp.cpu_count()
        chunksize = self.Ncells // cpu_count + (self.Ncells % cpu_count > 0) # ceil
        if self.verbose:
            print(f'INFO: Start single cell simulations with {cpu_count} processes'
                    +f' and {chunksize} cells per process')
        with mp.Pool(processes=cpu_count) as pool:
            self.cells = pool.map(run_cell, enumerate(self.cells), chunksize)
        if self.verbose:
            print(f'INFO: Finish single cell simulations')

        times = np.concatenate(list(map(lambda c: c.times[1:-1], self.cells)))
        events = np.concatenate(list(map(lambda c: c.events, self.cells)))
        events_cell = np.concatenate(list(map(lambda i:
            [i] * len(self.cells[i].events), np.arange(self.Ncells))))
        sorted_i = np.argsort(times)
        cell_i = np.concatenate(list(map(lambda c: np.arange(len(c.events)),
            self.cells)))
        self.times.extend(np.take_along_axis(times, sorted_i, axis=0))
        self.events.extend(np.take_along_axis(events, sorted_i, axis=0))
        self.events_cell.extend(np.take_along_axis(events_cell, sorted_i, axis=0))
        cell_i_sorted = np.take_along_axis(cell_i, sorted_i, axis=0)
        rates_all = list(map(lambda c: c.rates, self.cells))
        self.rates = np.sum(rates_all, axis=0)
        self.rates_var = np.var(rates_all, axis=0)
        levels_all = list(map(lambda c: c.levels, self.cells))
        self.levels = np.sum(levels_all, axis=0)
        self.levels_var = np.var(levels_all, axis=0)

    def plot_cell_positions_interactions(self, plot_filename=None):
        #TODO: add documentation
        fig, ax = plt.subplots(tight_layout=True)
        for j in np.arange(self.Ncells):
            x = []
            y = []
            for i in np.arange(j+1, self.Ncells):
                if self.neighbours[j,i] == 1:
                    x.append(self.x[j])
                    x.append(self.x[i])
                    y.append(self.y[j])
                    y.append(self.y[i])
            ax.plot(x, y, 'r-')
        for j in np.arange(self.Ncells):
            ax.plot(self.x[j], self.y[j], '.', markersize=4)
            ax.annotate(j, (self.x[j], self.y[j]), fontsize='small')
        ax.set_aspect(1)
        ax.set_xlim(0, self.square_length)
        ax.set_ylim(0, self.square_length)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def plot_cell_interactions_hist(self, plot_filename=None):
        #TODO: add documentation
        fig, ax = plt.subplots(tight_layout=True)
        n_neighbours = np.sum(self.neighbours, axis=-1)
        n_min, n_max = np.min(n_neighbours), np.max(n_neighbours)
        n_mean, n_std = np.mean(n_neighbours), np.std(n_neighbours)
        x, y, _ = ax.hist(n_neighbours, bins=np.arange(n_min - 0.5, n_max + 1, 1),
                label=f'n = {n_mean:.1f} ± {n_std:.1f}')
        ax.set_xlim(n_min - 0.5, n_max + 0.5)
        ax.set_ylabel('frequency')
        ax.set_xlabel('number of neighbours')
        ax.legend()
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)
        return x, y

    def plot_cell_interactions(self, plot_filename=None):
        #TODO: add documentation
        fig, ax = plt.subplots(tight_layout=True)
        n_neighbours = np.sum(self.neighbours, axis=-1)
        n_mean, n_std = np.mean(n_neighbours), np.std(n_neighbours)
        ax.hist(range(self.Ncells), bins=np.arange(-0.5, self.Ncells, 1),
                weights=n_neighbours, label=f'n = {n_mean:.1f} ± {n_std:.1f}')
        ax.set_xlim(-0.5, self.Ncells - 0.5)
        ax.set_ylabel('number of neighbours')
        ax.set_xlabel('cell')
        ax.legend()
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)
    
    def plot_cell_levels(self, plot_filename=None, time=None, cells_per_plot=None):
        #TODO: add documentation
        time = time if time else self.duration
        cells_per_plot = cells_per_plot if cells_per_plot else self.Ncells
        for j in np.arange(self.Ncells/cells_per_plot, dtype=int):
            fig, ax = plt.subplots(3, 1, sharex=True, tight_layout=True)
            range_cells = range(j * cells_per_plot,
                    min((j+1) * cells_per_plot, self.Ncells))
            for i in range_cells:
                if len(self.cells[i].levels[0]) == len(self.cells[i].times):
                    times = self.cells[i].times
                else:
                    times = np.linspace(0, self.duration,
                            len(self.cells[i].levels[0]))
                ax[0].step(times, self.cells[i].levels[Level.PRO],
                        c='tab:red', where='post')
                ax[1].step(times, self.cells[i].levels[Level.RNA],
                        c='tab:blue', where='post')
                ax[2].step(times, self.cells[i].levels[Level.DNA],
                        c='tab:orange', where='post')
            if len(self.levels[0]) == len(self.times):
                times = self.times
            else:
                times = np.linspace(0, self.duration, len(self.levels[0]))
            ax[0].step(times, np.divide(self.levels[Level.PRO], self.Ncells),
                    c='k', where='post')
            ax[0].set_ylabel(LevelLabels[Level.PRO])
            ax[0].grid(axis='x', which='major')
            ax[1].step(times, np.divide(self.levels[Level.RNA], self.Ncells),
                    c='k', where='post')
            ax[1].set_ylabel(LevelLabels[Level.RNA])
            ax[1].grid(axis='x', which='major')
            ax[2].step(times, np.divide(self.levels[Level.DNA], self.Ncells),
                    c='k', where='post')
            ax[2].set_ylabel(LevelLabels[Level.DNA])
            plot_set_ax(ax[2], time)
            if plot_filename:
                if cells_per_plot < self.Ncells:
                    base, ext = os.path.splitext(plot_filename)
                    plt.savefig(f'{base}_{j}{ext}')
                else:
                    plt.savefig(plot_filename)
            else:
                plt.show()
            plt.close(fig)
    
    def plot_cell_rates(self, plot_filename=None, time=None, cells_per_plot=None):
        #TODO: add documentation
        time = time if time else self.duration
        cells_per_plot = cells_per_plot if cells_per_plot else self.Ncells
        for j in np.arange(self.Ncells/cells_per_plot, dtype=int):
            fig, ax = plt.subplots(3, 1, sharex=True, tight_layout=True)
            range_cells = range(j * cells_per_plot,
                    min((j+1) * cells_per_plot, self.Ncells))
            for i in range_cells:
                ax[0].step(self.cells[i].times,
                        self.cells[i].rates[Process.PROTEIN_TRANSLATION],
                        c='tab:blue', where='post')
                ax[0].step(self.cells[i].times,
                        self.cells[i].rates[Process.PROTEIN_DEGRADATION],
                        c='tab:orange', where='post')
                ax[1].step(self.cells[i].times,
                        self.cells[i].rates[Process.RNA_TRANSCRIPTION],
                        c='tab:blue', where='post')
                ax[1].step(self.cells[i].times,
                        self.cells[i].rates[Process.RNA_DEGRADATION],
                        c='tab:orange', where='post')
                ax[2].step(self.cells[i].times,
                        self.cells[i].rates[Process.DNA_INACTIVATION],
                        c='tab:blue', where='post')
                ax[2].step(self.cells[i].times,
                        self.cells[i].rates[Process.DNA_ACTIVATION],
                        c='tab:orange', where='post')
            if len(self.rates[0]) == len(self.times):
                times = self.times
            else:
                times = np.linspace(0, self.duration, len(self.rates[0]))
            ax[0].step(times, np.divide(self.rates[Process.PRO_TRA], self.Ncells),
                    c='k', where='post', label=ProcessLabels[Process.PRO_TRA])
            ax[0].step(times, np.divide(self.rates[Process.PRO_DEG], self.Ncells),
                    c='r', where='post', label=ProcessLabels[Process.PRO_DEG])
            ax[0].set_ylabel('rate / h⁻¹')
            ax[0].grid(axis='x', which='major')
            ax[0].legend()
            ax[1].step(times, np.divide(self.rates[Process.RNA_TRA], self.Ncells),
                    c='k', where='post', label=ProcessLabels[Process.RNA_TRA])
            ax[1].step(times, np.divide(self.rates[Process.RNA_DEG], self.Ncells),
                    c='r', where='post', label=ProcessLabels[Process.RNA_DEG])
            ax[1].set_ylabel('rate / h⁻¹')
            ax[1].grid(axis='x', which='major')
            ax[2].step(times, np.divide(self.rates[Process.DNA_INA], self.Ncells),
                    c='k', where='post', label=ProcessLabels[Process.DNA_INA])
            ax[2].step(times, np.divide(self.rates[Process.DNA_ACT], self.Ncells),
                    c='r', where='post', label=ProcessLabels[Process.DNA_ACT])
            ax[2].set_ylabel('rate / h⁻¹')
            plot_set_ax(ax[2], time)
            if plot_filename:
                if cells_per_plot < self.Ncells:
                    base, ext = os.path.splitext(plot_filename)
                    plt.savefig(f'{base}_{j}{ext}')
                else:
                    plt.savefig(plot_filename)
            else:
                plt.show()
            plt.close(fig)

    def plot_costhetas(self, plot_filename=None, time=None, cells_per_plot=None):
        #TODO: add documentation
        time = time if time else self.duration
        cells_per_plot = cells_per_plot if cells_per_plot else self.Ncells
        times = np.linspace(0, self.duration, len(self.thetas_pre[0]))
        for j in np.arange(self.Ncells/cells_per_plot, dtype=int):
            fig, ax = plt.subplots(tight_layout=True)
            range_cells = range(j * cells_per_plot,
                    min((j+1) * cells_per_plot, self.Ncells))
            for i in range_cells:
                ax.plot(times, np.cos(self.thetas_pre[i]), label=f'{i}')
                #if time == self.duration:
                #    ax.annotate(i, (time, np.cos(self.thetas_pre[i][-1])),
                #            fontsize='small')
            ax.plot(times, 2 * np.abs(np.sum(np.exp(np.multiply(1j,
                    self.thetas_pre)), axis=0)/self.Ncells) - 1, color='k',
                    label='synchronisation index')
            secax = ax.secondary_yaxis('right',
                    functions=(lambda y: (y + 1) / 2, lambda y: 2 * y - 1))
            secax.set_ylabel('synchronisation index')
            if cells_per_plot <= 10:
                ax.legend()
            ax.set_ylabel(r'$\cos(\theta_i)$')
            plot_set_ax(ax, time)
            if plot_filename:
                if cells_per_plot < self.Ncells:
                    base, ext = os.path.splitext(plot_filename)
                    plt.savefig(f'{base}_{j}{ext}')
                else:
                    plt.savefig(plot_filename)
            else:
                plt.show()
            plt.close(fig)

    def plot_genetic_noise(self, plot_filename=None, time=None):
        #TODO: add documentation
        time = time if time else self.duration
        fig, ax = plt.subplots(tight_layout=True)
        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        ax.plot(times, np.divide(self.levels_var[Level.PROTEIN_COUNT],
            np.square(np.divide(self.levels[Level.PROTEIN_COUNT], self.Ncells))))
        ax.set_ylabel('genetic noise')
        plot_set_ax(ax, time)
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def plot_synchronisation_index(self, plot_filename=None, time=None):
        #TODO: add documentation
        time = time if time else self.duration
        fig, ax = plt.subplots(tight_layout=True)
        times = np.linspace(0, self.duration, len(self.thetas_pre[0]))
        plt.plot(times, np.abs(np.sum(np.exp(np.multiply(1j,
            self.thetas_pre)), axis=0)/self.Ncells))
        ax.set_ylabel('synchronisation index')
        ax.set_ylim(0,1)
        plot_set_ax(ax, time)
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def animate_luciferase(self, plot_filename=None, time=None, time_movie=None):
        #TODO: add documentation
        #TODO: time not used as intended
        # time_movie in seconds
        time = time if time else self.duration
        time_movie = time_movie if time_movie else time / 10
        fig, ax = plt.subplots(2, tight_layout=True, gridspec_kw={'height_ratios':
            [3, 1]})
        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        l = np.column_stack(np.array(list(map(lambda c: c.levels[Level.RNA],
            self.cells))))
        l_max = np.max(l)
        scat = ax[0].scatter(self.x, self.y, 50)
        ax[0].set_aspect(1)
        #ax[0].set_xlim(0, self.square_length)
        #ax[0].set_ylim(0, self.square_length)
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        curve, = ax[1].plot([], [])
        ax[1].set_ylabel(LevelLabels[Level.RNA])
        ax[1].set_ylim(min(self.levels[Level.RNA]) / self.Ncells,
                max(self.levels[Level.RNA]) / self.Ncells)
        plot_set_ax(ax[1], time)
        def update(i):
            scat.set_sizes(50*l[i] / l_max)
            curve.set_data(times[:i], self.levels[Level.RNA][:i] / self.Ncells)
            return [scat, curve]
        animation = anim.FuncAnimation(fig, update, frames=len(times), interval=10)
        if plot_filename:
            fps = int(len(times) / time_movie)
            animation.save(plot_filename, fps=fps)
        else:
            plt.show()

class GESNetworkCircadianDNAActivationOneCell(GESCircadian):
    """A class for gene expression simulation with variable DNA activation

    Parametrisation of DNA activation rate according to
        r(t) = k * (1 - b * cos(theta))
    """
    def __repr__(self):
        return (f'genexpsim.GESNetworkCircadianDNAActivationOneCell('
                f'duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def set_thetas_pre(self, thetas, dt):
        self.thetas_pre = thetas
        self.dt_sel = dt

    def new_rates(self, theta=None, add_to_rates=True):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        different, e.g. time dependent rates. Access to current rates with
        self.rates_now and to current counts with self.ng_now, self.nm_now and
        self.np_now.
        Here the DNA activation rate is time dependent.
        ----------
        Parameters
        ----------
        theta: float
            The current theta used in the time dependent DNA activation rate. If
            None then theta is extrapolated from previously saved thetas with
            set_thetas_pre(...) (default: None)
        add_to_rates: bool
            If True then the calculated rates are added to the self.rates array,
            else only self.rates_now is set (default: True)
        """
        if self.time_now == 0:
            theta = -self.p_sel
        elif theta == None:
            # Assume thetas have been set before with set_thetas_pre(...)
            j = np.int(self.time_now // self.dt_sel)
            x = self.time_now % self.dt_sel / self.dt_sel
            theta = np.multiply(1 - x, self.thetas_pre[j]) + np.multiply(x,
                    self.thetas_pre[j+1])
        rate_on = self.kon * (1 - self.b * np.cos(theta))
        self.rates_now = [self.koff * self.levels_now[Level.ACTIVE_GENES],
            rate_on * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            self.km * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        if add_to_rates:
            add_values(self.rates, self.rates_now)

class GESNetworkCircadianDNAInactivationOneCell(GESCircadian):
    """A class for gene expression simulation with variable DNA inactivation

    Parametrisation of DNA inactivation rate according to
        r(t) = k * (1 - b * cos(theta))
    """
    def __repr__(self):
        return (f'genexpsim.GESNetworkCircadianDNAInactivationOneCell('
                f'duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def set_thetas_pre(self, thetas, dt):
        self.thetas_pre = thetas
        self.dt_sel = dt

    def new_rates(self, theta=None, add_to_rates=True):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        different, e.g. time dependent rates. Access to current rates with
        self.rates_now and to current counts with self.ng_now, self.nm_now and
        self.np_now.
        Here the DNA activation rate is time dependent.
        ----------
        Parameters
        ----------
        theta: float
            The current theta used in the time dependent DNA activation rate. If
            None then theta is extrapolated from previously saved thetas with
            set_thetas_pre(...) (default: None)
        add_to_rates: bool
            If True then the calculated rates are added to the self.rates array,
            else only self.rates_now is set (default: True)
        """
        if self.time_now == 0:
            theta = -self.p_sel
        elif theta == None:
            # Assume thetas have been set before with set_thetas_pre(...)
            j = np.int(self.time_now // self.dt_sel)
            x = self.time_now % self.dt_sel / self.dt_sel
            theta = np.multiply(1 - x, self.thetas_pre[j]) + np.multiply(x,
                    self.thetas_pre[j+1])
        rate_off = self.kon * (1 - self.b * np.cos(theta))
        self.rates_now = [rate_off * self.levels_now[Level.ACTIVE_GENES],
            self.kon * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            self.km * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        if add_to_rates:
            add_values(self.rates, self.rates_now)

class GESNetworkCircadianRNATranscriptionOneCell(GESCircadian):
    """A class for gene expression simulation with variable mRNA transcription

    Parametrisation of mRNA transcription rate according to
        r(t) = k * (1 - b * cos(theta))
    """
    def __repr__(self):
        return (f'genexpsim.GESNetworkCircadianRNATranscriptionOneCell('
                f'duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def set_thetas_pre(self, thetas, dt):
        self.thetas_pre = thetas
        self.dt_sel = dt

    def new_rates(self, theta=None, add_to_rates=True):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        different, e.g. time dependent rates. Access to current rates with
        self.rates_now and to current counts with self.ng_now, self.nm_now and
        self.np_now.
        Here the mRNA transcription rate is time dependent.
        ----------
        Parameters
        ----------
        theta: float
            The current theta used in the time dependent DNA activation rate. If
            None then theta is extrapolated from previously saved thetas with
            set_thetas_pre(...) (default: None)
        add_to_rates: bool
            If True then the calculated rates are added to the self.rates array,
            else only self.rates_now is set (default: True)
        """
        if self.time_now == 0:
            theta = -self.p_sel
        elif theta == None:
            # Assume thetahave been set before with set_thetas_pre(...)
            j = np.int(self.time_now // self.dt_sel)
            x = self.time_now % self.dt_sel / self.dt_sel
            theta = np.multiply(1 - x, self.thetas_pre[j]) + np.multiply(x,
                    self.thetas_pre[j+1])
        rate_m = self.km * (1 - self.b * np.cos(theta))
        self.rates_now = [self.koff * self.levels_now[Level.ACTIVE_GENES],
            self.kon * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            rate_m * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        if add_to_rates:
            add_values(self.rates, self.rates_now)

def run_cell(i_cell):
    i, cell = i_cell
    if cell.verbose:
        print(f'INFO: Start simulation for cell {i}')
    cell.run()
    cell.compress_rates_levels(cell.dt_sel)
    return cell
