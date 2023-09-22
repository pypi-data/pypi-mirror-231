#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
#
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

import argparse
argcomplete_available = True
try:
    import argcomplete
except ImportError:
    argcomplete_available = False

def argument_error(argument, value, message):
    parser.print_usage(sys.stderr)
    print((f'{parser.prog}: error: argument {argument}: invalid value {value}: '
        f'{message}'), file=sys.stderr)
    sys.exit(2)

def parse_args():
    import argparse
    argcomplete_available = True
    try:
        import argcomplete
    except ImportError:
        argcomplete_available = False
    parser = argparse.ArgumentParser(
            prog='genexpsim',
            description='Simulation of gene expression for single or multiple cells',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--duration', type=float, default=24.0,
            help='The duration of simulation in hours')
    parser.add_argument('--seed', type=int,
            help='The seed used for the random generator, None for random seed')
    parser.add_argument('--koff', type=float, default=8.0,
            help='The rate of DNA inactivation per hour per active gene')
    parser.add_argument('--kon', type=float, default=1.5,
            help='The rate of DNA activation per hour per inactive gene')
    parser.add_argument('--km', type=float, default=225.0,
            help='The rate of mRNA transcription per hour per active gene')
    parser.add_argument('--gm', type=float, default=0.75,
            help='The rate of mRNA degradation per hour per mRNA molecule')
    parser.add_argument('--kp', type=float, default=1.25,
            help='The rate of protein translation per hour per mRNA molecule')
    parser.add_argument('--gp', type=float, default=0.35,
            help='The rate of protein degradation per hour per protein molecule')
    parser.add_argument('--n_gene_copies', '--ngc', type=int, default=2,
            help='The number of gene copies')
    parser.add_argument('--ap', '--alpha_paternal', type=float, default=0.5,
            help='The bias for allelic gene expression, 1 (0) for paternal (maternal) monoallelic expression, 0.5 for biallic expression. Defined as ap=p/(p+m) with p (m) size of paternal (maternal) expression. Must be in [0, 1]')
    parser.add_argument('--variable_process',
            choices=['DNA_activation', 'DNA_inactivation', 'mRNA_transcription'],
            help='The process for which the rate shall be variable, if omitted all rates are constant')
    parser.add_argument('--w', '--omega', type=float,
            help='The parameter omega for the variable rate per hour, if omitted a value of 2*pi/24 corresponding to a period of 24 hours is used')
    parser.add_argument('--dw', '--domega', type=float, default=0.0,
            help='The standard deviation on omega. If not 0, then omega is randomly chosen with normal distribution around w')
    parser.add_argument('--b', '--beta', type=float, default=1.0,
            help='The parameter beta for the variable rate, must be in range [-1, 1]')
    parser.add_argument('--p', '--phi', type=float,
            help='The parameter phi for the variable rate. If omitted then randomly chosen in [0, 2*pi]')
    parser.add_argument('--ng0', type=int,
            help='The number of active genes at start. If omitted then randomly chosen depending on N_GENE_COPIES, KOFF and KON. Has to be <= N_GENE_COPIES')
    parser.add_argument('--nm0', type=int,
            help='The number of mRNA molecules at start. If omitted then randomly chosen depending on parameters NG0, KM and GM')
    parser.add_argument('--np0', type=int,
            help='The number of protein molecules at start. If omitted then randomly chosen depending on parameters NM0, KP and GP')
    parser.add_argument('--dt', type=float,
            help='The minimal resolution time in hours for the calculation of the thetas, must be > 0. If omitted then dt is set to pi/120/W corresponding to 0.1 hours for a period of 24 hours')
    parser.add_argument('-n', '--n_cells', type=int, default=1,
            help='The number of cells in the network (if 1 then a single cell simulation is performed)')
    parser.add_argument('--square_length', type=float, default=1.0,
            help='The length of the square where the cells are placed')
    parser.add_argument('--random_cell_positions',
            help='If specified, cells are positioned randomly on square of length square_length, else on a grid, defined by N_CELLS')
    parser.add_argument('-l', '--coupling_length', '--lambda', type=float, default=0.2,
            help='The length of the coupling range for the cells interaction. Depending on their distance two cells are coupled with a probability ~ exp(-distance/LAMBDA). Shall be in the same unit as SQUARE_LENGTH')
    parser.add_argument('-k', '--coupling_strength', '--kappa', type=float,
            default=0.01,
            help='The coupling strength for neighbouring, interacting cells in the Kuramoto dynamic')
    parser.add_argument('-p', '--plot', action="store_true",
            help='If results shall be plotted')
    parser.add_argument('-s', '--summary', action="store_true",
            help='If results shall be summarised in txt-files')
    parser.add_argument('--n_cells_to_plot_summarise', type=int, default=10,
            help='The number of cells to plot or to summarise')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--dump', action="store_true",
            help='If simulation shall be saved with pickle')
    group.add_argument('--dump_file', type=argparse.FileType('rb'),
            help='The pkl file where a given simulation is saved. If given then no simulation is run. This option is useful for plotting or summarising afterwards')
    parser.add_argument('--n_cpus', type=int, default=1,
            help='The number of CPU cores used in parallel processing')
    parser.add_argument('-v', '--verbose', action='count', default=0,
            help='Verbose (trace import statements), can be supplied multiple times to increase verbosity')
    parser.add_argument('DIR', type=str,
            help='The output directory path for the plot, summary and dump files')
    if argcomplete_available:
        argcomplete.autocomplete(parser)
    args = parser.parse_args()

    import multiprocessing as mp
    import sys

    if args.duration <= 0:
        argument_error('-t/--duration', args.duration, 'must be > 0')
    if args.n_gene_copies < 0:
        argument_error('--n_gene_copies/--ngc', args.n_gene_copies, 'must be >= 0')
    if args.ap < 0 or args.ap > 1:
        argument_error('--ap/--alpha_paternal', args.ap, 'must be in [0, 1]')
    if args.b < -1 or args.b > 1:
        argument_error('--b/--beta', args.b, 'must be in [-1, 1]')
    if args.ng0 and args.ng0 > args.n_gene_copies:
        argument_error('--ng0', args.ng0, (f'must be <= {args.n_gene_copies} which is '
                'the number of gene copies (option --n_gene_copies/--ngc)'))
    elif args.ng0 and args.ng0 < 0:
        argument_error('--ng0', args.ng0, f'must be >= 0')
    if args.nm0 and args.nm0 < 0:
        argument_error('--nm0', args.nm0, f'must be >= 0')
    if args.np0 and args.np0 < 0:
        argument_error('--np0', args.np0, f'must be >= 0')
    if args.dt and args.dt < 0:
        argument_error('--dt', args.dt, f'must be >= 0')
    if args.n_cells < 1:
        argument_error('-n/--n_cells', args.n_cells, 'must be >= 1')
    if args.n_cells_to_plot_summarise < 1:
        argument_error('--n_cells_to_plot_summarise', args.n_cells_to_plot_summarise,
                'must be >= 1')
    if args.n_cpus < 1:
        argument_error('--n_cpus', args.n_cpus, 'must be >= 1')
    elif args.n_cpus > mp.cpu_count():
        argument_error('--n_cpus', args.n_cpus, (f'must be <= {mp.cpu_count()}, which '
            'is the available number of cpu cores on this machine'))
    return args

def sim_plot(sim, name, args):
    if args.verbose:
        print(f'INFO: Start plotting for {name}')
    sim.plot_rates(f'{name}_rates_{sim.duration}h.png')
    sim.plot_events_levels(f'{name}_events_levels_{sim.duration}h.png')
    if sim.duration > 120:
        sim.plot_rates(f'{name}_rates_120h.png', time=120)
        sim.plot_events_levels(f'{name}_events_levels_120h.png', time=120)
    if args.verbose:
        print(f'INFO: Finish plotting for {name}')

def sim_print_summary(sim, name, args):
    if args.verbose:
        print(f'INFO: Start printing summary for {name}')
        sim.print_summary(f'{name}_{sim.duration}h.txt',
                print_stdout=(args.verbose > 1))
    else:
        sim.print_summary(f'{name}_{sim.duration}h.txt',
                print_stdout=False)
def main():
    args = parse_args()

    import genexpsim
    import multiprocessing as mp
    import numpy as np
    import os
    import pickle
    import sys

    sim = None
    if args.dump_file:
        sim = pickle.load(args.dump_file)
    elif args.n_cells == 1:
        if not args.variable_process:
            sim = genexpsim.GES(args.duration, args.seed, verbose=args.verbose)
            sim.init_constants(koff=args.koff, kon=args.kon, km=args.km, gm=args.gm,
                    kp=args.kp, gp=args.gp, Ngc=args.n_gene_copies, ng0=args.ng0,
                    nm0=args.nm0, np0=args.np0)
        else:
            if args.variable_process == 'DNA_activation':
                sim = genexpsim.GESCircadianDNAActivation(args.duration, args.seed,
                        verbose=args.verbose)
            elif args.variable_process == 'DNA_inactivation':
                sim = genexpsim.GESCircadianDNAInactivation(args.duration, args.seed,
                        verbose=args.verbose)
            elif args.variable_process == 'mRNA_transcription':
                sim = genexpsim.GESCircadianRNATranscription(args.duration, args.seed,
                        verbose=args.verbose)
            sim.init_constants(koff=args.koff, kon=args.kon, km=args.km, gm=args.gm,
                    kp=args.kp, gp=args.gp, w=args.w, dw=args.dw, b=args.b, p=args.p,
                    Ngc=args.n_gene_copies, ng0=args.ng0, nm0=args.nm0, np0=args.np0)
        sim.run()
    else:
        if args.variable_process == 'DNA_activation':
            sim = genexpsim.GESNetworkCircadian(genexpsim.Process.DNA_ACTIVATION,
                    args.duration, args.seed, verbose=args.verbose,
                    Ncells=args.n_cells, square_length=args.square_length,
                    neighbour_coupling_length=args.coupling_length,
                    neighbour_coupling=args.coupling_strength)
        elif args.variable_process == 'DNA_inactivation':
            sim = genexpsim.GESNetworkCircadian(genexpsim.Process.DNA_INACTIVATION,
                    args.duration, args.seed, verbose=args.verbose,
                    Ncells=args.n_cells, square_length=args.square_length,
                    neighbour_coupling_length=args.coupling_length,
                    neighbour_coupling=args.coupling_strength)
        elif args.variable_process == 'mRNA_transcription':
            sim = genexpsim.GESNetworkCircadian(genexpsim.Process.RNA_TRANSCRIPTION,
                    args.duration, args.seed, verbose=args.verbose,
                    Ncells=args.n_cells, square_length=args.square_length,
                    neighbour_coupling_length=args.coupling_length,
                    neighbour_coupling=args.coupling_strength)
        else:
            print('No variable process given, but n_cells > 1')
            quit()

        sim.init_constants(koff=args.koff, kon=args.kon, km=args.km, gm=args.gm,
                kp=args.kp, gp=args.gp, w=args.w, dw=args.dw, b=args.b, p=args.p,
                Ngc=args.n_gene_copies, ng0=args.ng0, nm0=args.nm0, np0=args.np0,
                dt=args.dt)
        sim.run(cpu_count=args.n_cpus)

    if args.verbose:
        print(f'{args.DIR}: seed {sim.seed}, duration {sim.duration} h')
    prefix = f'{args.DIR}/seed_{sim.seed}'
    if args.summary or args.plot or args.dump:
        os.makedirs(f'{args.DIR}', exist_ok=True)
    if args.dump:
        pickle.dump(sim, open(f'{prefix}_{sim.duration}h.pkl', 'wb'))
    if args.plot:
        sim_plot(sim, f'{prefix}', args)
    if args.summary:
        sim_print_summary(sim, f'{prefix}', args)
    if type(sim) == genexpsim.GESNetworkCircadian:
        if args.plot:
            sim.plot_costhetas(f'{prefix}_costhetas_{sim.duration}h.png')
            sim.plot_cell_levels(f'{prefix}_cell_levels_{sim.duration}h.png')
            sim.plot_genetic_noise(f'{prefix}_genetic_noise_{sim.duration}h.png')
            if sim.duration > 120:
                sim.plot_costhetas(f'{prefix}_costhetas_120h.png', time=120)
                sim.plot_cell_levels(f'{prefix}_cell_levels_120h.png', time=120)
                sim.plot_genetic_noise(f'{prefix}_genetic_noise_120h.png', time=120)
            sim.plot_cell_positions_interactions(f'{prefix}_cells.png')
            sim.plot_cell_interactions(f'{prefix}_cell_interactions.png')
            sim.plot_cell_interactions_hist(f'{prefix}_cell_interactions_hist.png')
        with mp.Pool(args.n_cpus) as pool:
            chunksize = args.n_cells_to_plot_summarise // args.n_cpus + (
                    args.n_cells_to_plot_summarise % args.n_cpus > 0) # ceil
            sim_name_args = []
            for i, c in enumerate(sim.cells[:args.n_cells_to_plot_summarise]):
                sim_name_args.append([c, f'{prefix}_cell_{i}', args])
            if args.plot:
                pool.starmap(sim_plot, sim_name_args, chunksize)
            if args.summary:
                pool.starmap(sim_print_summary, sim_name_args, chunksize)

if __name__ == "__main__":
    main()
