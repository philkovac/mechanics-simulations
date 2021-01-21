# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:19:57 2020

@author: rkovac
"""

# solving the second order differential equation for a driven, damped linear 
# oscillator as a system of linear ODEs.

import numpy as np


def osci(z, t, beta, omega0, omega, f0):
    x, y = z
    return [y, f0*np.cos(omega*t) - omega0**2*x - 2*beta*y]

omega = 2*np.pi; 

omega0 = 5*omega;

beta = omega0/20;

f0 = 1000;

t = np.arange(0, 4, 0.01)

z0 = [0, 0]

from scipy.integrate import odeint

sol = odeint(osci, z0, t, args = (beta, omega0, omega, f0))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

# solution for x(t) agree with previosuly found solution found in exercise 5.36.

plt.plot(t, sol[:, 1], 'g', label='y(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

