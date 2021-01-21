# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:56:58 2020

@author: rkovac
"""


# solving the second order nonlinear inhomogeneous differential equation for a driven, 
# damped nonlinear oscillator as a system of linear ODEs.

import numpy as np

def osci(z, t, beta, omega0, omega, gamma):
    x, y = z
    return [y, gamma*omega0**2*np.cos(omega*t) - omega0**2*np.sin(x) - 2*beta*y]

omega = 2*np.pi; 

omega0 = 1.5*omega;

beta = omega0/4;

gamma = 1.3;

t = np.arange(0, 10, 0.01)

from scipy.integrate import odeint

sol1 = odeint(osci, [0, 0], t, args = (beta, omega0, omega, gamma))


import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


plt.plot(t, sol1[:, 0], '-g', label='$\phi(0) = 0$')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# first plot shows evidence of a conintually counterclockwise revolving pendulum. 
# The pendulum's arrival at its starting point (2 pi, 4 pi, 6 pi, ...) occurs 
# at the driver's period. 

plt.plot(t, sol1[:, 0] + 2*np.pi*t, label='$\phi(t) + 2\pi t$')
plt.xlabel('t')
plt.ylabel('$\phi(t) + 2\pi t$')
plt.show()

# each drive period, the position of the pendulum decreases (as it's rotating 
# counterclockwise) by 2 pi. By adding this quantity back to the position of 
# the pendulum, we see the periodic rolling motion as the pendulum is phase
#locked with the driver. 

