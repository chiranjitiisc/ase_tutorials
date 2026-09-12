import numpy as np
from ase import Atoms
from ase.visualize import view
from ase.build import bulk, make_supercell
from ase.io import read,write
from ase.calculators.morse import MorsePotential
from ase.calculators.lj import LennardJones
import matplotlib.pyplot as plt

box = [30,30,30]
r = np.linspace(3.2,12,500)

def en(calculator):
    e = []
    for i in r:
        atoms = Atoms(symbols = ['Ar','Ar'],positions = [[0,0,0],[i,0,0]] ,cell = box, pbc = True)
        atoms.calc = calculator
        e.append(atoms.get_potential_energy())
    return(e)

lj_en = en(LennardJones(sigma=3.4, epsilon =0.0104, rc =15 ))
mp_en = en(MorsePotential(epsilon = 0.0104, r0 = 3.816, rho0 =6.0))
lj_min =np.min(lj_en)
mp_min = np.min(mp_en)
print(lj_min, mp_min)
lj_r_min = np.argmin(lj_en)
mp_r_min = np.argmin(mp_en)
print(r[lj_r_min])
print(r[mp_r_min])
plt.plot(r,lj_en,label = 'Lennard Jones')
plt.plot(r,mp_en,label = 'Morse Potential')
plt.legend()
plt.show()