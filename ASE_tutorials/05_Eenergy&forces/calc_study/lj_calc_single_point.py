import numpy as np
from ase import Atoms
from ase.visualize import view
from ase.build import bulk, make_supercell
from ase.io import read,write
from ase.calculators.lj import LennardJones



posi = [[0.00,0.00,0.00],[2.7,0.00,0.00]]
box = [30,30,30]
atoms = Atoms(symbols = ['Ar','Ar'],positions = posi ,cell = box, pbc = True)
atoms.calc = LennardJones(epsilon = 0.0104, sigma = 3.40, rc = 15.0)
print(atoms.get_potential_energy())
print(atoms.get_forces())




