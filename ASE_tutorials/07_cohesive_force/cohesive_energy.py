import numpy as np
from ase import Atoms
from ase.io import read,write
from ase.visualize import view
from ase.calculators.emt import EMT

atoms = read('sup_cell.cif')
atoms.set_pbc(False)
posi = atoms.get_positions()
atoms.calc = EMT()
cell_energy = atoms.get_potential_energy()
atoms.center()
view(atoms)
atom1 = atoms[0]
atom1.position += [50,50,50]
view(atoms)
final_energy = atoms.get_potential_energy()
print("Total energy difference for removing one Cu atom: ", final_energy-cell_energy)

box = [100,100,100]
single_atom = Atoms(symbols = 'Cu', positions = [[50,50,50]], cell = box, pbc = False)
view(single_atom)
single_atom.calc = EMT()
single_energy = single_atom.get_potential_energy()
print("Cell Potential Energy = ",cell_energy," and ", "Single atom potential energy = ",single_energy)