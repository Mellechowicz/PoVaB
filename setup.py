import re
from setuptools import setup
from os import makedirs,environ
from shutil import rmtree
from sys import argv,version_info

packages_PoVaB     = ['PoVaB']
executables_PoVaB  = ['PoVaB/bin/PoVaB']
requirements_PoVaB = []

VERSION='0.2.0'

if __name__ == '__main__':
    options=""
    for arg in argv[2:]:
        options+=" %s"%arg

    options=re.sub('=',' ',options)
    options=re.sub('~',environ['HOME'],options)
    if '--user' in argv:
        try:
            locDir = environ['PYTHONUSERBASE']
            with open(environ['HOME']+'/.bashrc','a+') as bashrc:
                bashrc.write('\nexport PYTHONPATH=%s/lib/python%d.%d/site-packages/PoVaB-%s-py%d.%d.egg:$PYTHONPATH\n'%(locDir,version_info[0],version_info[1],VERSION,version_info[0],version_info[1]))
            makedirs(locDir,exist_ok=True)
        except KeyError:
            locDir = environ['HOME']+'/.local'
            print('Installing in %s'%(environ['HOME']))
        options+=' --prefix %s'%locDir
    try:
        with open('requirements.txt','r') as reqs:
            for line in reqs.readlines():
                package = re.sub('[><=]+.*','',line)
                package = re.sub('\s','',package)
                if len(package)>0:
                    requirements_PoVaB.append(package)
    except FileNotFoundError:
        requirements_PoVaB = [ 'numpy', 'matplotlib', 'setuptools', 'defusedxml' ]
    if 'clean' in argv or 'clear' in argv:
        try:
            rmtree('PoVaB.egg-info')
            rmtree('build')
            rmtree('dist')
        except FileNotFoundError:
            print("Already removed")
    else:
        setup(name='PoVaB',
              version=VERSION,
              description='PoVaB visualization utility',
              long_description="""
                Projected orbitals on Vasp Bandstructure Utility for extracting the projected bandstructure
                (character plot) from Vienna Ab Initio Software Package output (vasprun.xml)
              """,
              author='Andrzej P. Kądzielawa',
              author_email='andrzej.piotr.kadzielawa@vsb.cz',
              url='https://github.com/Mellechowicz/PoVaB',
              packages=packages_PoVaB,
              install_requires=requirements_PoVaB,
              provides=['PoVaB'],
              scripts=executables_PoVaB,
              platforms=['POSIX'],
              license='',
              test_suite='nose.collector',
              tests_require=['nose'])
