import numpy as np
from ase import Atoms
from ase.io import read,write
from ase.visualize import view
from ase.calculators.emt import EMT
import matplotlib.pyplot as plt
from ase.eos import EquationOfState

atoms = read('Cu_mp-30_conventional_standard.cif')
ocell = atoms.cell.cellpar()
# view(atoms)
atoms.calc = EMT()
pe_unitcell = atoms.get_potential_energy()
print(pe_unitcell)
a = np.linspace(3.4,3.8,9)
pe = []
v  = []

for i in a:
     atoms.set_cell([i,i,i,ocell[3],ocell[4],ocell[5]], scale_atoms =True)
     pe.append(atoms.get_potential_energy())
     v.append(i**3)
     atoms.set_cell([ocell[0],ocell[1],ocell[2],ocell[3],ocell[4],ocell[5]],scale_atoms = True)

en_min = np.min(pe)
a_opt = a[np.argmin(pe)]
print(en_min,a_opt)
atoms.set_cell([a_opt,a_opt,a_opt,ocell[3],ocell[4],ocell[5]])
eos = EquationOfState(v,pe)
v0,e0,B = eos.fit()
eos.plot()
print(v0,e0,B)
plt.plot(v,pe)
plt.show()


