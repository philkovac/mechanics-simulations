# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:09:36 2020

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

gamma = 1.084;

t = np.arange(0, 17, 0.01)

from scipy.integrate import odeint

sol1 = odeint(osci, [0, 0], t, args = (beta, omega0, omega, gamma))

sol2 = odeint(osci, [0.00001, 0], t, args = (beta, omega0, omega, gamma))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


plt.plot(t, sol1[:, 0], ':g', label='$\phi(0) = 0$')
plt.plot(t, sol2[:, 0], '-.r', label='$\phi(0) = 0.00001$')
plt.legend(loc='lower right')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

plt.plot(t, np.log10(np.abs(sol2[:, 0]- sol1[:, 0])), '-k', label='$\Delta\phi$')
plt.xlabel('t')
plt.ylabel('$\\Delta\phi(t)$')
plt.show()

# with the drive strength of gamma = 1.084, we see that the log of the phase difference 
# between the two oscillators diverges (changes by five order of magnitude)
# over the first seven periods of the driver. The motion of the pendulum is 
# therefore chaotic and highly sensitive to initial conditions. 
# This chaotic character is challenging to see in the plot of the position of 
# the pendulum vs. time. 

# interestingly, after the first seven periods of the driver, the oscillator 
# seems to settle down into period 3 nonchaotic motion as evidenced by the plot 
# of the position of the pendulum and the log of the phase difference plot. This
# behavior continues until at least 70 driver periods. 


