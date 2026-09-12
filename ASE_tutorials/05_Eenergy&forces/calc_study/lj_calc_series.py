import numpy as np
from ase import Atoms
from ase.visualize import view
from ase.build import bulk, make_supercell
from ase.io import read,write
from ase.calculators.lj import LennardJones
from matplotlib.pyplot import plot,show

box = [30,30,30]
forces = []
energies = []
r = np.linspace(3.2,7,500)
for i in r:
    atoms = Atoms(symbols = ['Ar','Ar'],positions = [[0.0,0.0,0.0],[i,0.0,0.0]] ,cell = box, pbc = True)
    atoms.calc = LennardJones(epsilon = 0.0104, sigma = 3.40, rc = 15.0)
    energies.append(atoms.get_potential_energy())
    forces.append(atoms.get_forces())

plot(r,energies)
show()



