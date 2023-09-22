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

from .GES import *

class GESCircadian(GES):
    """A class for Circadian gene expression simulation

    Parametrisation of a Circadian expression with DNA (in)activation / mRNA
    transcription rate according to
        r(t) = k * (1 - b * cos(w * t - p))
    This class needs to be implemented by implementing the method new_rates().
    """
    def __repr__(self):
        return (f'genexpsim.GESCircadian(duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def init_constants(self, koff, kon, km, gm, kp, gp, w=None, dw=0, b=1, p=None,
            Ngc=2, ng0=None, nm0=None, np0=None):
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
        self.w_sel = w_sel if dw == 0 else self.rng.normal(w_sel, dw)
        self.b = b
        self.p = p
        self.p_sel = p if p != None else self.rng.uniform(0, 2 * np.pi)
        super().init_constants(koff=koff, kon=kon, km=km, gm=gm, kp=kp, gp=gp,
                Ngc=Ngc, ng0=ng0, nm0=nm0, np0=np0)

class GESCircadianDNAInactivation(GESCircadian):
    """A class for gene expression simulation with variable DNA inactivation

    Parametrisation of DNA inactivation rate according to
        r(t) = k * (1 - b * cos(w * t - p))
    """
    def __repr__(self):
        return (f'genexpsim.GESCircadianDNAInactivation(duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def new_rates(self):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent rates. Access to current time with self.time_now, rates
        with self.rates_now and to levels with self.levels_now.
        Here the DNA inactivation rate is time dependent. 
        """
        rate_off = self.koff * (1 - self.b * np.cos(self.w_sel * self.time_now
            - self.p_sel))
        self.rates_now = [rate_off * self.levels_now[Level.ACTIVE_GENES],
            self.kon * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            self.km * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        add_values(self.rates, self.rates_now)

class GESCircadianDNAActivation(GESCircadian):
    """A class for gene expression simulation with variable DNA activation

    Parametrisation of DNA activation rate according to
        r(t) = k * (1 - b * cos(w * t - p))
    """
    def __repr__(self):
        return (f'genexpsim.GESCircadianDNAActivation(duration={self.duration}, '
                f'seed={self.seed_sel}, verbose={self.verbose})')

    def new_rates(self):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent rates. Access to current time with self.time_now, rates
        with self.rates_now and to levels with self.levels_now.
        Here the DNA activation rate is time dependent. 
        """
        rate_on = self.kon * (1 - self.b * np.cos(self.w_sel * self.time_now
            - self.p_sel))
        self.rates_now = [self.koff * self.levels_now[Level.ACTIVE_GENES],
            rate_on * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            self.km * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        add_values(self.rates, self.rates_now)

class GESCircadianRNATranscription(GESCircadian):
    """A class for gene expression simulation with variable mRNA transcription
    
    Parametrisation of mRNA transcription rate according to
        r(t) = k * (1 - b * cos(w * t - p))
    """
    def __repr__(self):
        return (f'genexpsim.GESCircadianRNATranscription(duration={self.duration},'
                f' seed={self.seed_sel}, verbose={self.verbose})')

    def new_rates(self):
        """Calculates the rates of the processes in Process

        This function might be overwritten by your own subclasses to allow
        e.g. time dependent rates. Access to current time with self.time_now, rates
        with self.rates_now and to levels with self.levels_now.
        Here the mRNA transcription rate is time dependent. 
        """
        rate_m = self.km * (1 - self.b * np.cos(self.w_sel * self.time_now
            - self.p_sel))
        self.rates_now = [self.koff * self.levels_now[Level.ACTIVE_GENES],
            self.kon * (self.Ngc - self.levels_now[Level.ACTIVE_GENES]),
            rate_m * self.levels_now[Level.ACTIVE_GENES],
            self.gm * self.levels_now[Level.RNA_COUNT],
            self.kp * self.levels_now[Level.RNA_COUNT],
            self.gp * self.levels_now[Level.PROTEIN_COUNT]]
        add_values(self.rates, self.rates_now)

