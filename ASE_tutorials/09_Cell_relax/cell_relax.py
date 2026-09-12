import numpy as np
from ase import Atoms
from ase.io import read,write
from ase.visualize import view
from ase.calculators.emt import EMT
import matplotlib.pyplot as plt
from ase.build import fcc111
from ase.optimize import BFGS

slab = fcc111(symbol ='Cu', size = (2,2,3), vacuum = 8)
slab.center()
slab.calc = EMT()
pei = slab.get_potential_energy()
tags = slab.get_tags()
top = tags == 1 
mid = tags == 2
bot = tags == 3
slab.positions[top,2] += 5
pef = slab.get_potential_energy()
print(pef,pei)
print(len(slab))