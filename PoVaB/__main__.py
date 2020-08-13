#!/usr/bin/python3

import numpy as np
import defusedxml.ElementTree as ET
from sys import argv
from PoVaB.argv import Options
from PoVaB.tags import Tags

if __name__ == '__main__':
    opt = Options(*argv)
    root = ET.parse(opt('vasprun')).getroot()

    tags = Tags(opt('vasprun'))

    filename = opt('outfile')
    if filename[-4:] == '.png':
        filename = filename[:-4]
    o        = opt('orbitals')
    ions=[ int(a) for a in opt('ions').split(',')]
    efermi = opt('efermi')
    eLimit = [ np.float(a) for a in opt('range').split(',')]
    labels = opt('labels')
    dpi    = opt('dpi')

    #
    # mmmmm                    #         #                        #
    # #   "#  mmm    mmm    mmm#         #mmm    mmm   m mm    mmm#   mmm
    # #mmmm" #"  #  "   #  #" "#         #" "#  "   #  #"  #  #" "#  #   "
    # #   "m #""""  m"""#  #   #         #   #  m"""#  #   #  #   #   """m
    # #    " "#mm"  "mm"#  "#m##         ##m#"  "mm"#  #   #  "#m##  "mmm"

    eigenvalues = {
            'dimensions': {},
            'fields'    : {},
            'spagetti'  : [[],[]]
            }

    data = root.find('calculation').find('projected').find('eigenvalues')[0]
    for d in data.findall('dimension'):
        eigenvalues['dimensions'][int(d.attrib['dim'])-1]= d.text
        # indexing from 0
    for i,f in enumerate(data.findall('field')):
        eigenvalues['fields'][i]= f.text
    array = data.find('set')
    for (s,spin) in enumerate(array):
        for kpoint in spin:
            local = []
            for entry in kpoint:
                local.append(np.fromstring(entry.text,sep=' '))
            eigenvalues['spagetti'][s].append(np.array(local))
    del data,array

    projections = {
            'dimensions': {},
            'fields'    : {},
            'spagetti'  : [[],[],[],[]]
            }
    data = root.find('calculation').find('projected').find('array')
    for d in data.findall('dimension'):
        eigenvalues['dimensions'][int(d.attrib['dim'])-1]= d.text
        # indexing from 0
    for i,f in enumerate(data.findall('field')):
        eigenvalues['fields'][i]= f.text
    array = data.find('set')
    for (s,spin) in enumerate(array):
        for kpoint in spin:
            projections['spagetti'][s].append([])
            for band in kpoint:
                local = []
                for ion in band:
                    local.append(np.fromstring(ion.text,sep=' '))
                projections['spagetti'][s][-1].append(np.array(local))
    del data,array

    data               = root.find('kpoints').find('generation')
    TOTAL_KPOINTS      = int(data.find('i').text)
    high_symmetry_path = []
    for v in data.findall('v'):
        high_symmetry_path.append(np.fromstring(v.text,sep=' '))
    del data

    mul = np.zeros(len(high_symmetry_path)-1)
    for i,_ in enumerate(mul):
        mul[i] = np.linalg.norm(high_symmetry_path[i]-high_symmetry_path[i+1])
    mul /= np.max(mul)

    data     = root.find('kpoints').find('varray')
    kpoints  = []
    for point in data:
        kpoints.append(np.fromstring(point.text,sep=' '))
    del data

    atomNames = []
    data      = root.find('atominfo').find('array').find('set')
    for rc in data:
        atomNames.append(rc[0].text)
    del data

    from itertools import cycle
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True,
                     'text.usetex':       True})

    # Data for plotting

    orbitals = {
            'sp':   [0,1,2,3],
            'spd':  [0,1,2,3,4,5,6,7,8],
            'spdf': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
            'pd':   [1,2,3,4,5,6,7,8],
            'pdf':  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
            'df':   [4,5,6,7,8,9,10,11,12,13,14,15],
            's':    [0],
            'p':    [1,2,3],
            'd':    [4,5,6,7,8],
            'f':    [9,10,11,12,13,14,15]
            }

    atom_types = ''.join(['_%s%d%s'%(n,i+1,o) for i,n in zip(ions,[atomNames[ion] for ion in ions])])
    fig, ax = plt.subplots()
    data = []
    try:
        colors = cycle(['k','r']) if tags['ISPIN'] == 2 else cycle['k']
    except AttributeError:
        colors = cycle['k']
    for i,kpoint in enumerate(projections['spagetti'][0]):
        data.append([])
        for (b,band),color in zip(enumerate(kpoint),colors):
            data[i].append(None)
            if np.all(eigenvalues['spagetti'][0][i][b][0] < efermi + eLimit[0]) or np.all(eigenvalues['spagetti'][0][i][b][0] > efermi + eLimit[1]):
                continue
            occ = 0.0
            for ion in ions:
                occ += np.sum(band[ion,orbitals[o]])
            if occ < 1e-4:
                continue
            ax.scatter(TOTAL_KPOINTS*np.sum(mul[:i//TOTAL_KPOINTS])+(i%TOTAL_KPOINTS)*mul[i//TOTAL_KPOINTS], eigenvalues['spagetti'][0][i][b][0]-efermi,s=10*np.power(2*occ,2), c=color, alpha=0.9)
            data[i][b] = (i,*kpoints[i],eigenvalues['spagetti'][0][i][b][0]-efermi,occ)
    for i,kpoint in enumerate(data):
        for b,bnd in enumerate(kpoint):
            if bnd:
                with open('data%s_%04d.txt'%(atom_types,b),'a') as out:
                    out.write("%3d % .8f % .8f % .8f % .8f %.8f\n"%bnd)
    xticks  = []
    xlabels = []
    for i,a in enumerate(labels):
        xticks.append(TOTAL_KPOINTS*np.sum(mul[:i]))
        xlabels.append(a)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    ax.set(xlabel='', ylabel=r'band energy, $E_b - E_f$ (eV)',
           title=r'Band structure projected on %s ions of \textsuperscript{%s} electrons'%(r''.join([r'%s\textsubscript{(%d)}'%(n,i+1) for i,n in zip(ions,[atomNames[ion] for ion in ions])]), o))
    ax.grid()

    fig.savefig(filename+'.png',dpi=dpi)

    exit()

