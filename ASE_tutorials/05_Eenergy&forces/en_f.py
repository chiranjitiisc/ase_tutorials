import numpy as np
from ase import Atoms
from ase.visualize import view
from ase.build import bulk, make_supercell
from ase.io import read,write
from ase.calculators.emt import EMT
cu_uc = read("Cu_mp-30_conventional_standard.cif")

cu_sc = cu_uc.repeat([2,2,2])
cu_sc.wrap()

cu_sc.calc = EMT()

print(cu_sc.get_potential_energy())


