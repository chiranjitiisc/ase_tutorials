import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms, units
from ase.io import read, write
from ase.io.trajectory import Trajectory
from ase.calculators.lj import LennardJones
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

box = [30, 30, 30]
posi = [[10, 10, 10],[14.0, 10, 10]]
atoms = Atoms(symbols=['Ar', 'Ar'],positions=posi,cell=box,pbc=True)
MaxwellBoltzmannDistribution(atoms, temperature_K= 30)
atoms.calc = LennardJones(epsilon=0.0104,sigma=3.40,rc=25)

print(atoms.get_potential_energy())
print(atoms.get_velocities())
print(units.fs)
def thermo():
    ep = atoms.get_potential_energy()
    ek = atoms.get_kinetic_energy()
    p  = -np.trace(atoms.get_stress(voigt=False)) / 3 / units.GPa
    print(f"{dyn.nsteps:8d} {dyn.get_time()/units.fs:10.1f} "
          f"{atoms.get_temperature():9.2f} {ep:12.5f} {ek:12.5f} "
          f"{ep+ek:12.5f} {p:12.4f}", flush=True)

dyn = VelocityVerlet(atoms,timestep=10*units.fs)
traj = Trajectory('traj.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.attach(thermo, interval = 20 )
dyn.run(4000)
traj.close()