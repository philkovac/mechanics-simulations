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

gamma = 0.3;

t = np.arange(0, 7, 0.01)

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

plt.plot(t, np.log10(np.abs(sol2[:, 0]- sol1[:, 0])), '-k', label='$\log(\Delta\phi$)')
plt.xlabel('t')
plt.ylabel('$\\Delta\phi(t)$')
plt.show()

# here is an example of a drive strength that leads to nonchaotic behavior. 
# As seen, the final motion of the pendulum is insensitive to initial conditions
# as the final motion settles down to an osciallation about zero fro both pendulums. 
# Further, we see that the phase difference bewteen the pendulum's with different 
# intial conditionsc converges to zero expontially as seen in the plot of the
# log of the phase difference. 

