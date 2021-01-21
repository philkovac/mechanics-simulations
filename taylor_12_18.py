# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:42:24 2020

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

t = np.arange(0, 20, 0.01)

from scipy.integrate import odeint

sol1 = odeint(osci, [0, 0], t, args = (beta, omega0, omega, gamma))

sol2 = odeint(osci, [1, 0], t, args = (beta, omega0, omega, gamma))


import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


plt.plot(t, sol1[:, 0], ':g', label='$\phi(0) = 0$')
plt.plot(t, sol2[:, 0], '-.r', label='$\phi(0) = 1$')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# plot does not appear to reveal chaotic motion, but we need to rely on the 
# log of the phase difference plot to be sure.


plt.plot(t, np.log(np.abs(sol2[:,0] - sol1[:, 0])), label='$\phi(t) + 2\pi t$')
plt.xlabel('t')
plt.ylabel('$\log(\Delta\phi(t))$')
plt.show()

# based on the log of the phase difference, for the specified drive strength, the
# pendulum does not undergo chaotic motion as evidenced by the linearly decreasing
#phase differnce between drive periods 0 and ~10. 
#

