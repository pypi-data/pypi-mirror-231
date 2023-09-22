# genexpsim: Simulation of gene expression for single or multiple cells
# Copyright 2021–2023 Robert Wolff <mahlzahn@posteo.de>
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
import pandas as pd
from .GES import *

class Molecule:
    def __init__(self, identifier, n_0=None, n_max=None, label='', kind='',
            rng=None):
        self.identifier = identifier
        self.n_0 = n_0
        self.n_max = n_max
        if n_max != None and n_0 != None and n_0 > n_max:
            raise ValueError(f'Given n_0 = {n_0} is greater than n_max = {n_max}')
        self.label = label
        self.kind = kind if kind in ['gene', 'mrna', 'prot'] else 'other'
        if not type(rng) == np.random._generator.Generator:
            self.rng = rng
        else:
            self.rng = np.random.default_rng(rng)

        #TODO: make n randomly chosen
        self.n = 0 if n_0 == None else n_0

    def __repr__(self):
        text = f'genexpsim.GESMultiGenes.Molecule(\'{self.identifier}\', {self.n}'
        if self.n_max != None:
            text += f', n_max={self.n_max}'
        if self.label:
            text += f', label=\'{self.label}\''
        if self.kind:
            text += f', kind=\'{self.kind}\''
        return text + ')'

    def add(self, k=1):
        n_new = self.n + k
        if self.n_max == None or self.n_max >= n_new:
            self.n = n_new
        else:
            raise ValueError((f'k = {k} molecules cannot be added, else n > n_max '
                f'= {self.n_max}'))

    def remove(self, k=1):
        n_new = self.n - k
        if n_new >= 0:
            self.n = n_new
        else:
            raise ValueError(f'k = {k} molecules cannot be removed, else n < 0')

class Process:
    """
    rate r(t) = k * (1 - β * cos(ω * t - φ))
    """
    def __repr__(self):
        text = (f'genexpsim.GESMultiGenes.Process({self.mol1}, {self.mol2}, '
                f'{self.k}')
        if self.circadian:
            text += (f', beta={self.beta}, omega={self.omega_sel}, '
                    f'phi={self.phi_sel}')
        if self.label:
            text += f', label=\'{self.label}\''
        return text + ')'

    def __init__(self, mol1, mol2, k, beta=None, omega=None, domega=None,
            phi=None, label='', rng=None):
        """
        ----------
        Parameters
        ----------
        beta: float
            If None or 0 then rate is time independent.
        """
        self.mol1 = mol1
        self.mol2 = mol2
        self.k = k
        self.beta = beta
        self.omega = omega
        self.domega = domega
        self.phi = phi
        self.label = label
        if type(rng) == np.random._generator.Generator:
            self.rng = rng
        else:
            self.rng = np.random.default_rng(rng)

        if self.mol1:
            if self.mol2:
                if self.k < 0: # suppression
                    if self.mol2.n_max != None: # gene copy number
                        n = lambda: self.mol1.n * self.mol2.n
                    else:
                        n = lambda: self.mol1.n
                    self._trigger = lambda: self.mol2.remove()
                else: # transcription / translation
                    if self.mol2.n_max != None: # gene copy number (TF)
                        n = lambda: self.mol1.n * (self.mol2.n_max - self.mol2.n)
                    else:
                        n = lambda: self.mol1.n
                    self._trigger = lambda: self.mol2.add()
                self.kind = self.mol2.kind
            else: # inactivation / degradation
                n = lambda: self.mol1.n
                self._trigger = lambda: self.mol1.remove()
                self.kind = self.mol1.kind
        elif self.mol2: # activation
            if self.mol2.n_max != None: # gene copy number (gene activation)
                n = lambda: self.mol2.n_max - self.mol2.n
            else:
                n = lambda: 1
            self._trigger = lambda: self.mol2.add()
            self.kind = self.mol2.kind
        else:
            raise ValueError(f'Process {self.name} has neither mol1 nor mol2')

        self.circadian = bool(self.beta and self.omega)
        if self.circadian:
            self.omega_sel = self.rng.normal(omega, domega) if domega else omega
            self.phi_sel = phi if phi != None else self.rng.uniform(0, 2 * np.pi)
            k_time = lambda time: k * (1 - self.beta * np.cos(self.omega_sel * time
                - self.phi_sel))
        else:
            k_time = lambda time: k

        self._rate = lambda time=0: n() * k_time(time)

    def rate(self, time=0):
        return self._rate(time)

    def trigger(self):
        return self._trigger()

    def set_k(self, k):
        return self.__init__(self.mol1, self.mol2, k, self.beta, self.omega,
                self.domega, self.phi, self.label, self.rng)

    def set_beta(self, beta):
        return self.__init__(self.mol1, self.mol2, self.k, beta, self.omega,
                self.domega, self.phi, self.label, self.rng)

    def set_omega(self, omega):
        return self.__init__(self.mol1, self.mol2, self.k, self.beta, omega,
                self.domega, self.phi, self.label, self.rng)

    def set_domega(self, domega):
        return self.__init__(self.mol1, self.mol2, self.k, self.beta, self.omega,
                domega, self.phi, self.label, self.rng)

    def set_phi(self, phi):
        return self.__init__(self.mol1, self.mol2, self.k, self.beta, self.omega,
                self.domega, phi, self.label, self.rng)

    def set_label(self, label):
        return self.__init__(self.mol1, self.mol2, self.k, self.beta, self.omega,
                self.domega, self.phi, label, self.rng)

class GESMultiGenes(GES):
    """A class for gene expression simulation with multiple genes

    Parametrisation of a Circadian expression with DNA (in)activation / mRNA
    transcription rate according to
        r(t) = k * (1 - b * cos(w * t - p))
    """
    def __init__(self, mols_file, procs_file, duration=24, seed=None, verbose=0):
        """
        ----------
        Parameters
        ----------
        mols_file: str
            The path of the file with molecules as tabulator separated table with
            the following columns:
            id: str
                An identifier for the molecule, used to define processes
            kind: {gene, mrna, prot, other}
                The kind of molecule, if omitted set to other. Is only used to
                order rates and levels in the plots
            n_max: int
                The maximum number of molecules, e.g. gene copy number. If omitted
                no upper bound is set
            n_0: int
                The initial number of molecules, if omitted the initial number is
                chosen randomly or set to zero.
            label: str
                A nice label for the molecule used in plots, etc.
        procs_file: str
            The path of the file with processes as tabulator separated table with
            the following columns:
            id1, id2: str, str
                The identifiers for the molecules involved in the process, must
                match identifiers from mols_file. The id1 is defining the initial
                molecule and the id2 is defining the changed molecule. Examples of
                processes are:
                id1  | id2  | process type
                ---------------------------------
                     | gene | gene activation
                gene |      | gene inactivation
                gene | mrna | mRNA transcription
                mrna |      | mRNA degradation
                mrna | prot | protein translation
                prot |      | protein degradation
            k: float
                The constant k for the rate
            β: float
                The constant β for the rate
            ω: float
                The constant ω for the rate
            σω: float
                The standard deviation on ω, if not omitted and not zero then ω is
                randomly chosen with a normal distribution around given ω with σω
            φ: float
                The constant φ for the rate, if omitted it is chosen randomly in
                [0, 2π]
            label: str
                A nice label for the process used in plots, etc.
        duration: float
            The duration of simulation in hours (default: 24)
        seed: int, None
            The seed used for the random generator, None for random seed (default:
            None)
        verbose: int
            The level of verbosity, 0 or None for quietness (default: None)
        """
        super().__init__(duration, seed, verbose)
        self.mols_file = mols_file
        self.mols = pd.read_csv(mols_file, delimiter="\t", comment="#")
        self.procs_file = procs_file
        self.procs = pd.read_csv(procs_file, delimiter="\t", comment="#")
        mols_procs = pd.concat([self.procs['id1'], self.procs['id2']])
        mols_procs = mols_procs[mols_procs.notna()].unique()
        if not np.isin(mols_procs, self.mols['id']).all():
            raise ValueError(('Some procs include molecules not in mols.\n'
                f'mols in procs: {np.sort(mols_procs)}\n'
                f"mols in mols:  {np.sort(self.mols['id'])}"))
        self.molecules = dict()
        for i_mol, mol in self.mols.replace({np.nan:None}).iterrows():
            self.molecules[mol.id] = Molecule(
                    mol.id,
                    int(mol.n_0 + 0.5) if mol.n_0 else None,
                    int(mol.n_max + 0.5) if mol.n_max else None,
                    label=mol.label,
                    kind=mol.kind,
                    rng=self.rng)
        self.processes = []
        for i_proc, proc in self.procs.replace({np.nan:None}).iterrows():
            self.processes.append(Process(
                self.molecules[proc.id1] if proc.id1 else None,
                self.molecules[proc.id2] if proc.id2 else None,
                proc.k,
                proc.β,
                proc.ω,
                proc.σω,
                proc.φ,
                proc.label,
                self.rng))
        self.molecules = list(self.molecules.values())
        self.kinds = []
        for kind in ['other', 'prot', 'mrna', 'gene']:
            if kind in list(map(lambda mol: mol.kind, self.molecules)):
                self.kinds.append(kind)

    def __repr__(self):
        return (f'genexpsim.GESMultiGenes('
                f"'{self.mols_file}', "
                f"'{self.procs_file}', "
                f'duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def new_levels(self, process=None):
        self.levels_now = list(map(lambda mol: mol.n, self.molecules))
        add_values(self.levels, self.levels_now)

    def new_rates(self):
        self.rates_now = list(map(lambda proc: proc.rate(self.time_now),
            self.processes))
        add_values(self.rates, self.rates_now)

    def run(self):
        self.time_now = 0.
        self.times = array('f', [0.])
        self.events = array('b')
        self.levels = []
        self.levels_now = []
        for mol in self.molecules:
            self.levels.append(array('i', [mol.n]))
            self.levels_now.append(mol.n)
        self.rates = []
        self.rates_now = []
        for proc in self.processes:
            self.rates.append(array('f', [proc.rate()]))
            self.rates_now.append(proc.rate())

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
            process = self.rng.choice(np.arange(len(self.processes)),
                    p=np.divide(abs_rates, total_rate))
            self.processes[process].trigger()
            self.events.append(process)
            self.new_levels()
            self.new_rates()
            # add time_now at the end such that levels and rates can use the
            # time difference self.time_now - self.times[-1] in their calculation
            self.times.append(self.time_now)

    def finalize(self, end_at_duration=True):
        super().finalize(end_at_duration=end_at_duration)
        for proc in self.processes:
            del proc.rng, proc._trigger, proc._rate
        for mol in self.molecules:
            del mol.rng

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
        for i_proc, proc in enumerate(self.processes):
            rate_mean = integrate(times, self.rates[i_proc]) / self.duration
            count = self.events.count(i_proc)
            write(f'{count:7d}\t{count/self.duration:7.2f}\t{rate_mean:7.2f}'
            + f'\t{proc.label}')

        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        write(f'mean\tlevel')
        for i_mol, mol in enumerate(self.molecules):
            level_mean = integrate(times, self.levels[i_mol]) / self.duration
            write(f'{level_mean:7.2f}\t{mol.label}')
        if print_filename:
            f.close()

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
        i_ax = list(map(lambda proc: self.kinds.index(proc.kind), self.processes))
        n_ax = len(self.kinds)
        fig, ax = plt.subplots(n_ax, sharex=True, tight_layout=True)
        if len(self.rates[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.rates[0]))
        for i_proc, proc in enumerate(self.processes):
            ax[i_ax[i_proc]].step(times, self.rates[i_proc], label=proc.label,
                    where='post')
        plot_set_ax(ax[-1], time)
        for axi in ax:
            axi.legend()
            axi.set_ylabel('rate / h⁻¹')
            axi.grid(axis='x', which='major')
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def plot_levels(self, plot_filename=None, time=None):
        """Plots levels of active genes, mRNA molecules and proteins
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
        i_ax = list(map(lambda mol: self.kinds.index(mol.kind), self.molecules))
        n_ax = len(self.kinds)
        fig, ax = plt.subplots(n_ax, sharex=True, tight_layout=True)
        if len(self.levels[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.levels[0]))
        for i_mol, mol in enumerate(self.molecules):
            ax[i_ax[i_mol]].step(times, self.levels[i_mol], label=mol.label,
                    where='post')
        plot_set_ax(ax[-1], time)
        for i_ax, ax in enumerate(ax):
            ax.legend()
            if self.kinds[i_ax] == 'gene':
                ax.set_ylabel('number of\nactive genes')
            elif self.kinds[i_ax] == 'mrna':
                ax.set_ylabel('mRNA count')
            elif self.kinds[i_ax] == 'prot':
                ax.set_ylabel('protein count')
            else:
                ax.set_ylabel('count')
            ax.grid(axis='x', which='major')
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

    def plot_events(self, plot_filename=None, time=None):
        """Plots events of the different processes
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
        fig, ax = plt.subplots(1, sharex=True, tight_layout=True)
        if len(self.rates[0]) == len(self.times):
            times = self.times
        else:
            times = np.linspace(0, self.duration, len(self.rates[0]))
        ax.plot(self.times[1:len(self.events) + 1], self.events, '|',
                c='darkgreen')
        ax.set_yticks(np.arange(len(self.processes)))
        ax.set_yticklabels(list(map(lambda proc: proc.label, self.processes)))
        plot_set_ax(ax, time)
        if plot_filename:
            plt.savefig(plot_filename)
        else:
            plt.show()
        plt.close(fig)

