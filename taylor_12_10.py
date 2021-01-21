# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:56:37 2020

@author: rkovac
"""


import numpy as np

def osci(z, t, beta, omega0, omega, gamma):
    x, y = z
    return [y, gamma*omega0**2*np.cos(omega*t) - omega0**2*np.sin(x) - 2*beta*y]

omega = 2*np.pi; 

omega0 = 1.5*omega;

beta = omega0/4;

gamma = 1.073;

t = np.arange(0, 50, 0.01)

zero = np.zeros(len(t))

twopie = 2*np.pi*np.ones(len(t))

fourpie = 4*np.pi*np.ones(len(t))

from scipy.integrate import odeint

#comparing solutions with different initial conditions

sol0 = odeint(osci, [0, 0], t, args = (beta, omega0, omega, gamma))

sol1 = odeint(osci, [np.pi, 0], t, args = (beta, omega0, omega, gamma))

sol2 = odeint(osci, [np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

sol3 = odeint(osci, [-np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

sol4 = odeint(osci, [-np.pi, 0], t, args = (beta, omega0, omega, gamma))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

plt.plot(t, sol0[:, 0], '-b', label='$\phi(0) = 0$')
plt.plot(t, sol4[:, 0], '-m', label='$\phi(0) = -pi$')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

plt.plot(t, sol1[:, 0], '-g', label='$\phi(0) = \pi$')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

plt.plot(t, sol2[:, 0], '-.r', label='$\phi(0) = \pi/2$')
plt.plot(t, sol3[:, 0], ':k', label='$\phi(0) = -\pi/2$')
plt.legend(loc='lower right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

#once again, quite different and unpredictable intial behavior of the driven damped
# penduluum. For the specified drive stength, all that changes between each 
# scenario are the initial conditions. 
