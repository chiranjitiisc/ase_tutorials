import numpy as np
from ase import Atoms
from ase.io import read,write

box = [50, 50, 50]
n = 500
atoms = read('single_h2o.xyz')
seed = 10
sys = Atoms(cell = box, pbc = True)
rn = np.random.default_rng(seed)

def rotate(atoms,rn):
    a = atoms.copy()
    a.rotate(rn.uniform(0,360),"z",center = "COM")       # azimuth angle (rotation)
    theta = np.rad2deg(np.arccos(2 * rn.random() - 1))   
    a.rotate(theta,"x",center="COM")                     # polar angle rotate around the sphere (tilt)
    a.rotate(rn.uniform(0, 360),"z", center="COM")       # rotation around its own axis (spin)
    return a

for i in range (n):
    trial = rotate(atoms,rn)
    trial.translate(rn.random(3)*box-trial.get_center_of_mass())
    sys+= trial
sys.wrap()

write("data.xyz",sys)