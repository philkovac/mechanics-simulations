# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:38:16 2020

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

twopi = 2*np.pi*np.ones(len(t))

fourpi = 4*np.pi*np.ones(len(t))

ntwopi = -2*np.pi*np.ones(len(t))

z0 = [0, 0]

from scipy.integrate import odeint

sol = odeint(osci, z0, t, args = (beta, omega0, omega, gamma))

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

plt.plot(t[0:3000], sol[0:3000, 0], 'b', label='$\phi(t)$')
plt.plot(t[0:3000], zero[0:3000], ':k')
plt.plot(t[0:3000], twopi[0:3000], ':k')
plt.plot(t[0:3000], fourpi[0:3000], ':k')
plt.plot(t[0:3000], ntwopi[0:3000], ':k')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# results agree with figure 12.5. Incredibly interesting and unpredicatble 
# initial motion. Within the first ten periods of the driver, the penduluum 
# undergoes about 2 and a half revolutions counter-clockwise, then one clockwise,
# then one counter-clockwise and again one clockwise. In periods ~ 10 - 17 of 
# we see this pattern again, but somewhat centered about -2pi, not + 2pi. 
# finally, after 17 periods of motion of the driver, the penduluum appears to 
# to settle on an attractor oscillating about -2pi. 

plt.plot(t, sol[:, 0], 'b', label='$\phi(t)$')
plt.plot(t, zero, ':k')
plt.plot(t, ntwopi, ':k')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# the motion over 50 periods seemingly demonstrates period doubling. To be sure, 
# we'll look at periods 40 - 50 of this motion.

plt.plot(t[4000:5000], sol[4000:5000, 0], 'b', label='$\phi(t)$')
plt.plot(t[4000:5000], zero[4000:5000], ':k')
plt.plot(t[4000:5000], ntwopi[4000:5000], ':k')
plt.ylim(-9, -2.5)
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('$\phi(t)$')
plt.show()

# After the transients have died out, the period of the attractor is clearly
# 2tau

