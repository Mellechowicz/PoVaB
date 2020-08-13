# -*- coding: utf-8 -*-
import argparse as ap
import numpy as np

class Error:
    access = 123

class Options:
    """ Options-parsing class """
    keys = [ 'outfile', 'vasprun', 'orbitals', 'ions', 'efermi', 'range', 'labels', 'dpi' ]

    def __init__(self, *args):
        """
            Initialization of parser, together with arguments.
        """
        self.parser = ap.ArgumentParser(description='Plotting the projected bands')
        self.parser.add_argument('--efermi', '-E', default=0.0, type=np.float,
                help='Fermi energy in eV (default: 0.0 eV)')
        self.parser.add_argument('--outfile', '-o', default='fig.png',
                help='Name of the plotted figure (default: \'fig.png\'')
        self.parser.add_argument('--vasprun', '-v', default='vasprun.xml',
                help='Name of the vasprun xml file (default=\'./vasprun.xml\')')
        self.parser.add_argument('--orbitals', '-l', default='spd',
                choices=['s','p','d','f','sp','spd','spdf','pd','pdf','df'],
                help='Type of orbitals (e.g. \'df\' for d and f electrons only; default=\'spd\'')
        self.parser.add_argument('--range', '-r', default='-1.5,0.25',
                help='Plot energy range from [Ef-r[0], Ef-r[1]] (default: -1.5,0.25 <=> -1.5 eV - 0.25 eV)')
        self.parser.add_argument('--ions', '-i', default='0',
               help='Coma separated id\'s of ions taken into account (enumerating from 0; default 0)')
        self.parser.add_argument('--labels', nargs='+', default=[],
               help='Labels for each of high symmetry points. (e.g., \'$\Gamma$\'; default None)')
        self.parser.add_argument('--dpi', default=200, type=int,
                help='Figure dpi (default: 200)')

        self.opt = self.parser.parse_args(args[1:])

    def __call__(self, key):
        try:
            return self.opt.__dict__[key]
        except KeyError:
            print("No key \"%s\" defined, please try: "%key)
            print("%s"%(str(self.keys)))
            exit(Error.access)
