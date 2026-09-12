# ASE Crystal and Surface Builders

## 1. The basic idea

ASE (Atomic Simulation Environment) provides builder functions that create atomic structures as `Atoms` objects.

A builder answers:

> What atomic structure do I want?

It does **not** automatically calculate energies or relax the atoms.

```python
from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.61)
```

---

## 2. The ASE `Atoms` object

Almost everything in ASE is stored as an `Atoms` object.

```python
from ase import Atoms

atoms = Atoms(
    'Cu2',
    positions=[[0, 0, 0],
               [1, 1, 1]]
)

print(atoms.positions)
print(atoms.cell)
print(atoms.pbc)
print(atoms.get_tags())
```

Important properties:

```python
atoms.positions   # atomic coordinates
atoms.cell        # simulation cell
atoms.pbc         # periodic boundary conditions
atoms.get_tags()  # integer labels attached to atoms
```

---

# 3. `bulk()` — building bulk crystals

The basic form is:

```python
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61)
```

This builds an FCC Cu crystal.

Common examples:

### FCC

```python
cu = bulk('Cu', 'fcc', a=3.61)
```

### BCC

```python
fe = bulk('Fe', 'bcc', a=2.87)
```

### Diamond

```python
si = bulk('Si', 'diamond', a=5.43)
```

### HCP

```python
mg = bulk('Mg', 'hcp', a=3.21, c=5.21)
```

For cubic crystals, `a` is the lattice constant.

---

# 4. Conventional versus primitive cells

This distinction is very important.

An FCC conventional cubic cell contains 4 atoms:

```text
8 corner atoms × 1/8
+
6 face atoms × 1/2
=
4 atoms
```

A primitive FCC cell contains 1 atom.

If you want the conventional cubic FCC cell:

```python
cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
```

Then:

```python
print(len(cu))
```

returns 4.

---

# 5. Reading a crystal from a CIF

Instead of constructing the crystal yourself, you can read a CIF:

```python
from ase.io import read

atoms = read('Cu.cif')
```

Conceptually:

```text
bulk()
  ↓
you specify the structure

read('file.cif')
  ↓
ASE reads the structure from the file
```

A CIF may contain a primitive cell, conventional cell, or another standardized cell.

---

# 6. `.repeat()` — making supercells

If you already have a structure:

```python
cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
```

you can repeat it:

```python
sc = cu.repeat((2, 2, 2))
```

This means:

```text
2 repeats along cell direction 1
2 repeats along cell direction 2
2 repeats along cell direction 3
```

If the starting cell has 4 atoms:

```text
4 × 2 × 2 × 2 = 32 atoms
```

So:

```python
print(len(sc))
```

gives 32.

### Important distinction

```python
atoms.repeat((2,2,2))
```

means:

> Repeat the **existing cell**.

It does NOT mean:

> Create a 2×2 surface with 2 atomic layers.

---

# 7. What are Miller indices?

Crystal planes are described by:

```text
(h k l)
```

Examples:

```text
(100)
(110)
(111)
(211)
(311)
```

The notation is different from direction notation:

```text
(hkl)  → plane
[hkl]  → direction
```

For cubic crystals:

```text
(hkl) is perpendicular to [hkl]
```

For example:

```text
(111) ↔ [111]
(100) ↔ [100]
(110) ↔ [110]
```

---

# 8. How Miller indices describe a plane

For a cubic lattice with lattice constant `a`, the intercepts of `(hkl)` are proportional to:

```text
x = a/h
y = a/k
z = a/l
```

A zero index means the plane is parallel to that axis.

## (100)

```text
x = a
y = infinity
z = infinity
```

So `(100)` is perpendicular to x.

## (110)

```text
x = a
y = a
z = infinity
```

So `(110)` is parallel to z.

## (111)

```text
x = a
y = a
z = a
```

This is the diagonal plane.

## (211)

```text
x = a/2
y = a
z = a
```

This is a higher-index tilted plane.

### Important

`(211)` does **not** mean:

```text
2 layers in x
1 layer in y
1 layer in z
```

It describes a crystallographic orientation.

---

# 9. Why different surfaces matter

Different Miller-index surfaces expose different arrangements of atoms.

For FCC crystals:

```text
(111) → close-packed surface
(100) → square-like surface
(110) → more open surface
```

Therefore different surfaces can have different:

- surface energies
- adsorption energies
- coordination numbers
- relaxation behavior
- catalytic properties

---

# 10. ASE's dedicated surface builders

ASE provides convenient builders for common surfaces.

Common examples include:

```python
fcc100()
fcc110()
fcc111()

bcc100()
bcc110()
bcc111()

hcp0001()
hcp10m10()
```

The exact arguments available depend on your installed ASE version.

---

# 11. FCC (100)

```python
from ase.build import fcc100

slab = fcc100(
    'Cu',
    size=(2, 2, 3),
    vacuum=10.0
)
```

Here:

```text
Cu       → element
(2,2)    → repetitions in the surface plane
3        → number of layers
10 Å     → vacuum
```

---

# 12. FCC (110)

```python
from ase.build import fcc110

slab = fcc110(
    'Cu',
    size=(2, 2, 3),
    vacuum=10.0
)
```

This constructs an FCC Cu slab exposing the `(110)` surface.

---

# 13. FCC (111)

```python
from ase.build import fcc111

slab = fcc111(
    'Cu',
    size=(2, 2, 3),
    vacuum=8.0
)
```

This is the type of slab you have been working with.

Interpretation:

```text
size=(2,2,3)

2 → surface repetition in direction 1
2 → surface repetition in direction 2
3 → number of atomic layers
```

For this Cu(111) example:

```text
2 × 2 atoms per layer × 3 layers
= 12 atoms
```

---

# 14. BCC surface builders

For BCC Fe:

## BCC (100)

```python
from ase.build import bcc100

slab = bcc100(
    'Fe',
    size=(2, 2, 3),
    vacuum=10.0
)
```

## BCC (110)

```python
from ase.build import bcc110

slab = bcc110(
    'Fe',
    size=(2, 2, 3),
    vacuum=10.0
)
```

## BCC (111)

```python
from ase.build import bcc111

slab = bcc111(
    'Fe',
    size=(2, 2, 3),
    vacuum=10.0
)
```

---

# 15. HCP surface builders

For an HCP material such as Mg:

## HCP (0001)

```python
from ase.build import hcp0001

slab = hcp0001(
    'Mg',
    size=(2, 2, 4),
    vacuum=10.0
)
```

`(0001)` is the HCP basal plane.

Another HCP surface builder is:

```python
from ase.build import hcp10m10

slab = hcp10m10(
    'Mg',
    size=(2, 2, 4),
    vacuum=10.0
)
```

---

# 16. The general `surface()` builder

When you want to specify Miller indices yourself, ASE provides `surface()`.

```python
from ase.build import bulk, surface

cu = bulk('Cu', 'fcc', a=3.61)

slab = surface(
    cu,
    indices=(1, 1, 1),
    layers=4,
    vacuum=10.0
)
```

Here:

```python
indices=(1,1,1)
```

means the `(111)` surface.

---

# 17. General `(100)` surface

```python
from ase.build import bulk, surface

cu = bulk('Cu', 'fcc', a=3.61)

slab = surface(
    cu,
    indices=(1,0,0),
    layers=4,
    vacuum=10.0
)
```

The Miller index is explicitly supplied:

```python
indices=(1,0,0)
```

---

# 18. General `(110)` surface

```python
cu = bulk('Cu', 'fcc', a=3.61)

slab = surface(
    cu,
    indices=(1,1,0),
    layers=4,
    vacuum=10.0
)
```

---

# 19. General `(211)` surface

```python
cu = bulk('Cu', 'fcc', a=3.61)

slab = surface(
    cu,
    indices=(2,1,1),
    layers=6,
    vacuum=10.0
)
```

This creates a slab oriented according to the `(211)` Miller plane.

High-index surfaces such as `(211)` are often useful when studying steps, kinks, and low-coordination sites.

---

# 20. What is a slab?

A slab is a finite number of atomic layers cut from a bulk crystal.

Conceptually:

```text
        vacuum
  ─────────────────

       layer 1
  ● ● ● ● ● ● ●

       layer 2
  ● ● ● ● ● ● ●

       layer 3
  ● ● ● ● ● ● ●

  ─────────────────
        vacuum
```

The slab is periodic parallel to the surface but has empty space in the direction normal to the surface.

---

# 21. Vacuum

For example:

```python
slab = fcc111(
    'Cu',
    size=(2,2,3),
    vacuum=8.0
)
```

`vacuum=8.0` adds approximately 8 Å of empty space normal to the slab.

The purpose is to separate one periodic slab from its periodic image.

Conceptually:

```text
┌──────────────────────┐
│       VACUUM         │
│                      │
│======================│
│      Cu SLAB         │
│======================│
│                      │
│       VACUUM         │
└──────────────────────┘
```

---

# 22. Layer tags

Surface builders such as `fcc111()` provide useful layer tags.

Check them:

```python
print(slab.get_tags())
```

For a 3-layer slab, you may see something like:

```text
[3 3 3 3 2 2 2 2 1 1 1 1]
```

The exact ordering should always be checked in your actual structure.

The tags are simply integer labels.

They are not physical quantities.

---

# 23. Selecting atoms using tags

Suppose:

```python
tags = slab.get_tags()
```

Then:

```python
top = tags == 1
```

creates a Boolean mask.

For example:

```text
tags:
[3 3 3 3 2 2 2 2 1 1 1 1]

tags == 1:
[False False False False
 False False False False
 True  True  True  True]
```

`top` therefore tells NumPy which atoms to select.

---

# 24. Understanding `positions`

ASE stores positions as rows:

```text
[x, y, z]
```

For example:

```python
slab.positions
```

has the structure:

```text
             x       y       z

atom 0     [x0      y0      z0]
atom 1     [x1      y1      z1]
atom 2     [x2      y2      z2]
...
```

The column numbers are:

```text
0 → x
1 → y
2 → z
```

Therefore:

```python
slab.positions[top, 2]
```

means:

> select the rows where `top` is `True`, then select column 2.

So it returns the z coordinates of the selected atoms.

---

# 25. Moving selected atoms

```python
slab.positions[top, 2] -= 0.2
```

means:

```text
select atoms using top
        ↓
select their z coordinate
        ↓
subtract 0.2
```

If the selected z values were:

```python
[9.0, 9.0, 9.0, 9.0]
```

they become:

```python
[8.8, 8.8, 8.8, 8.8]
```

Other atoms are unchanged.

---

# 26. Fixing atoms using tags

Tags can also be used to define constraints.

Suppose:

```text
tag 1 → top
tag 2 → middle
tag 3 → bottom
```

To fix everything except the top layer:

```python
from ase.constraints import FixAtoms

tags = slab.get_tags()

mask = tags > 1

slab.set_constraint(
    FixAtoms(mask=mask)
)
```

Now:

```text
top       → free
middle    → fixed
bottom    → fixed
```

---

# 27. Relaxing the slab

Attach a calculator:

```python
from ase.calculators.emt import EMT

slab.calc = EMT()
```

Then use BFGS:

```python
from ase.optimize import BFGS

opt = BFGS(slab)
opt.run(fmax=0.05)
```

`fmax=0.05` means the optimization stops when the largest force on movable atoms is below:

```text
0.05 eV/Å
```

---

# 28. Measuring interlayer spacing

Use tags to select layers:

```python
tags = slab.get_tags()

top = tags == 1
second = tags == 2
```

Get their z coordinates:

```python
z_top = slab.positions[top, 2]
z_second = slab.positions[second, 2]
```

Average them:

```python
z_top_average = z_top.mean()
z_second_average = z_second.mean()
```

Then:

```python
d12 = z_top_average - z_second_average
```

is the distance between the first and second layers.

---

# 29. Bulk (111) spacing

For a cubic crystal:

```text
d111 = a / sqrt(3)
```

In Python:

```python
from math import sqrt

a = 3.61

d111 = a / sqrt(3)

print(d111)
```

This gives approximately:

```text
2.084 Å
```

This can be compared with the relaxed surface interlayer spacing.

---

# 30. Surface relaxation

If:

```python
d_bulk = a / sqrt(3)
d_slab = z_top_average - z_second_average
```

then:

```python
change = (d_slab - d_bulk) / d_bulk * 100
```

Interpretation:

```text
change < 0 → contraction
change > 0 → expansion
```

---

# 31. Molecule builder

ASE can also build molecules:

```python
from ase.build import molecule

water = molecule('H2O')
```

Then:

```python
print(water)
print(water.positions)
```

The molecule builder is different from crystal builders because molecules are finite objects rather than periodic bulk crystals.

---

# 32. Nanotubes

ASE can construct nanotubes.

For example:

```python
from ase.build import nanotube

tube = nanotube(5, 5, length=4)
```

The two numbers describe the nanotube's chiral indices.

---

# 33. A complete Cu(111) example

```python
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.visualize import view

# Build
slab = fcc111(
    'Cu',
    size=(2,2,3),
    vacuum=8.0
)

# Look at tags
tags = slab.get_tags()
print(tags)

# Fix middle and bottom layers
mask = tags > 1
slab.set_constraint(FixAtoms(mask=mask))

# Calculator
slab.calc = EMT()

# Relax
opt = BFGS(slab)
opt.run(fmax=0.05)

# Visualize
view(slab)
```

The workflow is:

```text
BUILD
  ↓
INSPECT
  ↓
GET TAGS
  ↓
SELECT LAYERS
  ↓
APPLY CONSTRAINT
  ↓
CALCULATOR
  ↓
BFGS
  ↓
ANALYZE
```

---

# 34. The most important difference to remember

## `bulk()`

Creates a bulk crystal:

```python
cu = bulk('Cu', 'fcc', a=3.61)
```

## `.repeat()`

Repeats the current cell:

```python
cu2 = cu.repeat((2,2,2))
```

## `fcc111()`

Creates an FCC (111) slab:

```python
slab = fcc111('Cu', size=(2,2,3), vacuum=8)
```

## `surface()`

Lets you explicitly specify a Miller-index orientation:

```python
slab = surface(
    cu,
    indices=(2,1,1),
    layers=6,
    vacuum=10
)
```

---

# 35. Quick Miller-index reference

| Miller index | Basic interpretation |
|---|---|
| `(100)` | plane normal to x |
| `(010)` | plane normal to y |
| `(001)` | plane normal to z |
| `(110)` | plane parallel to z |
| `(101)` | plane parallel to y |
| `(011)` | plane parallel to x |
| `(111)` | diagonal plane cutting all three axes equally |
| `(211)` | higher-index tilted plane |
| `(311)` | higher-index tilted plane |

Remember:

```text
(hkl) → plane
[hkl] → direction
```

For cubic crystals:

```text
(hkl) ⟂ [hkl]
```

---

# 36. A useful mental model

Keep these operations separate:

```text
              BUILDING
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
      BULK    SURFACE   MOLECULE
       │         │
     bulk()   fcc111()
       │         │
    repeat()  tags/layers
                 │
                 ↓
             CONSTRAINT
                 │
                 ↓
              RELAX
                 │
                 ↓
               BFGS
```

Think of the roles this way:

```text
Builder:
"What structure do I want?"

Tags:
"Which atoms are which?"

Mask:
"Which atoms do I want to select?"

Constraint:
"Which atoms am I allowing to move?"

Calculator:
"What are the energies and forces?"

Optimizer:
"How should the atoms move to reach a lower-energy structure?"
```

---

# 37. Recommended learning order

For learning ASE, work through these in order:

1. `Atoms`
2. `bulk()`
3. primitive vs conventional cells
4. `.repeat()`
5. Miller indices
6. `fcc100()`, `fcc110()`, `fcc111()`
7. `surface()`
8. vacuum
9. tags
10. Boolean masks
11. `FixAtoms`
12. calculators
13. BFGS relaxation
14. interlayer relaxation
15. surface energy
16. adsorption on surfaces

Once these are clear, most basic ASE slab scripts become much easier to read.
