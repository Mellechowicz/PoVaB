# PoVaB
**P**rojected **o**rbitals on **Va**sp **B**andstructure

Utility for extracting the projected bandstructure (character plot) from Vienna Ab Initio Software Package [1] output (vasprun.xml)

[1] G. Kresse and J. Furthmüller,Phys. Rev. B 54, 11169 (1996); Comput. Mater. Sci. 6, 15 (1996)

Program analysies the vasprun.xml file for calculations **with LORBIT** tag <img src="https://render.githubusercontent.com/render/math?math=\in \{1,2,11,12,13,14\}">.

### Requirements
For ```Python 3.7.2``` and up:
```
numpy >= 1.16.2
matplotlib >= 3.0.2
defusedxml >= 0.5.0
argparse >= 1.1
```
The above may be installed using ```pip```:
``` bash
sudo pip3 install -r requirements.txt
```

For tagging the High symmetry points on the plots we require a separate LaTeX installation.

### Installation
```bash
  git clone https://github.com/Mellechowicz/PoVaB.git
  cd PoVaB
  sudo python3 setup.py install
```

### Options
```bash
usage: PoVaB [-h] [--efermi EFERMI] [--outfile OUTFILE]
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
```

[![CodeFactor](https://www.codefactor.io/repository/github/mellechowicz/povab/badge)](https://www.codefactor.io/repository/github/mellechowicz/povab)
[![codebeat badge](https://codebeat.co/badges/54186a8d-8b10-418f-96be-7267e390f5dc)](https://codebeat.co/projects/github-com-mellechowicz-povab-master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be6cedf1649d4c5a9ec0a7084f645934)](https://www.codacy.com/manual/apkadzielawa/PoVaB?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Mellechowicz/PoVaB&amp;utm_campaign=Badge_Grade)
<sub><sup>This work was supported by The Ministry of Education, Youth and Sports from the Large Infrastructures for Research, Experimental Development and Innovations project *IT4Innovations National Supercomputing Center – LM2015070*.</sup></sub>
