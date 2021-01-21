# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:25:28 2020

@author: rkovac
"""

import numpy as np

def osci(z, t, beta, omega0, omega, gamma):
    x, y = z
    return [y, gamma*omega0**2*np.cos(omega*t) - omega0**2*np.sin(x) - 2*beta*y]

omega = 2*np.pi; 

omega0 = 1.5*omega;

beta = omega0/4;

gamma = 1.06;

t = np.arange(0, 15, 0.01)

zero = np.zeros(len(t))

twopie = 2*np.pi*np.ones(len(t))

fourpie = 4*np.pi*np.ones(len(t))

z0 = [0, 0]

from scipy.integrate import odeint

sol = odeint(osci, z0, t, args = (beta, omega0, omega, gamma))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

plt.plot(t, sol[:, 0], 'b', label='$\phi(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# solution for phi(t) agrees with text's figure 12.4 

#comparing solutions with different initial conditions

sol1 = odeint(osci, [np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

sol2 = odeint(osci, [-np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

plt.plot(t, sol[:, 0], '-b', label='$\phi(0) = 0$')
plt.plot(t, sol1[:, 0], '--g', label='$\phi(0) = \pi/2$')
plt.plot(t, sol2[:, 0], '-.r', label='$\phi(0) = -\pi/2$')
plt.plot(t, zero, ':k')
plt.plot(t, twopie, ':k')
plt.plot(t, fourpie, ':k')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# depending on intial conditions, specifically phi(0) = 0, we see drastically
# different initial behavior. Although the penduluum at phi(0) = 0 completes two
# and a half revolutions( gridlines at phi = 0, 2pi, 4pi) it evntually settles 
# down to oscillate about phi = 2pi which is eqivilent to phi = 0. Despite, 
# the intial transient behavior, for the specified drive strength, there is 
# still only one unique periodic attractor - the drive force. 






