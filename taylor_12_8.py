# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:14:53 2020

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

z0 = [np.pi/2, 0]

from scipy.integrate import odeint

sol = odeint(osci, z0, t, args = (beta, omega0, omega, gamma))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

plt.plot(t[0:1000], sol[0:1000, 0], 'b', label='$\phi(t)$')
plt.plot(t[0:1000], zero[0:1000], ':k')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# we some initial transient motion here, there is some evidence of period 
# doubling, but with the transient motion it is difficult to distinguish if the 
# motion has settled down. 

plt.plot(t, sol[:, 0], 'b', label='$\phi(t)$')
plt.plot(t, zero, ':k')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# the motion over 50 periods seemingly demonstrates period doubling. To be sure, 
# we'll look at periods 40 - 50 of this motion.

plt.plot(t[4000:5000], sol[4000:5000, 0], 'b', label='$\phi(t)$')
plt.plot(t[4000:5000], zero[4000:5000], ':k')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# After the transients have died out, the period of the attractor is clearly
# 2tau








