"""
usage: __main__.py [-h] [--efermi EFERMI] [--outfile OUTFILE]
                   [--vasprun VASPRUN]
                   [--orbitals {s,p,d,f,sp,spd,spdf,pd,pdf,df}]
                   [--range RANGE] [--ions IONS]
                   [--labels LABELS [LABELS ...]] [--dpi DPI]

Plotting the projected bands

optional arguments:
  -h, --help            show this help message and exit
  --efermi EFERMI, -E EFERMI
                        Fermi energy in eV (default: 0.0 eV)
  --outfile OUTFILE, -o OUTFILE
                        Name of the plotted figure (default: 'fig.png'
  --vasprun VASPRUN, -v VASPRUN
                        Name of the vasprun xml file (default='./vasprun.xml')
  --orbitals {s,p,d,f,sp,spd,spdf,pd,pdf,df}, -l {s,p,d,f,sp,spd,spdf,pd,pdf,df}
                        Type of orbitals (e.g. 'df' for d and f electrons
                        only; default='spd'
  --range RANGE, -r RANGE
                        Plot energy range from [Ef-r[0], Ef-r[1]] (default:
                        -1.5,0.25 <=> -1.5 eV - 0.25 eV)
  --ions IONS, -i IONS  Coma separated id's of ions taken into account
                        (enumerating from 0; default 0)
  --labels LABELS [LABELS ...]
                        Labels for each of high symmetry points. (e.g.,
                        '$\Gamma$'; default None)
  --dpi DPI             Figure dpi (default: 200)

"""
