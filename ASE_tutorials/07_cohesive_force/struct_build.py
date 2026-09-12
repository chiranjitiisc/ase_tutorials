import numpy as np
from ase import Atoms
from ase.io import read,write
from ase.visualize import view

atoms = read('Cu_mp-30_conventional_standard.cif')
sup_cell = atoms.repeat((3,3,3))
sup_cell.wrap()
write('sup_cell.cif',sup_cell)
sup_cell.center()
view(sup_cell)