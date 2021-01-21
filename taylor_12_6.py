# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:25:17 2020

@author: rkovac
"""

# solving the second order nonlinear inhomogeneous differential equation for a driven, damped linear 
# oscillator as a system of linear ODEs.

import numpy as np

def osci(z, t, beta, omega0, omega, gamma):
    x, y = z
    return [y, gamma*omega0**2*np.cos(omega*t) - omega0**2*np.sin(x) - 2*beta*y]

omega = 2*np.pi; 

omega0 = 1.5*omega;

beta = omega0/4;

gamma = 0.9;

t = np.arange(0, 6.01, 0.01)

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

# solution for x(t) agree with previosuly found solution found in exercise 5.36.

#comparing solutions with different initial conditions

sol1 = odeint(osci, [np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

sol2 = odeint(osci, [-np.pi/2, 0], t, args = (beta, omega0, omega, gamma))

plt.plot(t, sol[:, 0], '-b', label='$\phi(0) = 0$')
plt.plot(t, sol1[:, 0], ':g', label='$\phi(0) = \pi/2$')
plt.plot(t, sol2[:, 0], '-.r', label='$\phi(0) = -\pi/2$')
plt.legend(loc='upper right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# despite the signifant difference in initial conditions and hence inital
# transient behavior, after about two periods, all solutions approach the 
# same periodic attractor - the driving force. This would be a neat experiment
# to perform and simulate!




