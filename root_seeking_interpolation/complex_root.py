#! /usr/bin/env python3
#
from f9 import f9
from f9 import f9p
from newton3 import newton3
import numpy as np
import matplotlib.pyplot as plt

NPTS = 100
x = np.linspace(-2, 2, NPTS)
y = np.linspace(-2, 2, NPTS)
omega = np.zeros(3, dtype=np.complex_)
omega[0] = -1  # red
omega[1] = (1 + np.sqrt(3) * 1j) / 2  # orange
omega[2] = (1 - np.sqrt(3) * 1j) / 2  # purple

z = np.zeros((NPTS, NPTS), dtype=np.complex_)

for k in range(0, NPTS):
  for m in range(0, NPTS):
    z[k, m] = x[k] + y[m] * 1j

z = z.flatten()

which = []
for k in range(0, len(z)):
  root, num_iters = newton3 ( f9, f9p, z[k], maxIts = 500 )
  whichRoot = np.argmin(np.abs(root - omega))
  if whichRoot == 0:
    which += ['red']
  elif whichRoot == 1:
    which += ['orange']
  elif whichRoot == 2:
    which += ['purple']
  else:
    print('You have a bug')

plt.scatter(z.real, z.imag, color=which)
plt.scatter(omega.real, omega.imag)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.savefig ( 'exercise10.jpg' )
plt.show ( )
plt.close ( )

