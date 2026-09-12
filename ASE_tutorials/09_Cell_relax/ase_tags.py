import numpy as np
from ase import Atoms
from ase.io import read,write
from ase.visualize import view
from ase.calculators.emt import EMT
import matplotlib.pyplot as plt

atoms = read("Cu_mp-30_conventional_standard.cif")
sc = atoms.repeat([3,2,2])
# print(sc.get_tags())

for i in range(5):
     sc[i].tag = 1

tags = sc.get_tags()
tag1 = tags ==1
sc.positions[tag1,1] += 20 # y coordinates of atoms with tag = 1 is increased by 20   

atoms.center()
view(sc)