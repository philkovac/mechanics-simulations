# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:44:46 2020

@author: rkovac
"""

import matplotlib.pyplot as plt 

import numpy as np

plt.style.use('seaborn-whitegrid')

t = np.arange(0, 20*np.pi, 0.01)

omega = 1; 

omega0 = 0.9999999999; 

beta = 0.1;

omega1 = np.sqrt(omega0**2 - beta**2);

f0 = 0.4; 

x0 = 0;

v0 = 6;

def A(f0, omega0, omega, beta):
    return np.sqrt((f0**2)/((omega0**2 - omega**2)**2 + 4*beta**2*omega**2))

A0 = A(f0, omega0, omega, beta);
    
def delta(omega0, omega, beta):
   return np.arctan(2*beta*omega/(omega0**2 - omega**2))

delta0 = delta(omega0, omega, beta);

def B1(x0, A0, delta0):
  return x0 - A0*np.cos(delta0)

def B2(x0, v0, A0, delta0, omega, omega1, beta):
    return (1/omega1)*(v0 - A0*omega*np.sin(delta0) + beta*(x0 - A0*np.cos(delta0)))

Bone = B1(x0, A0, delta0);

Btwo = B2(x0, v0, A0, delta0, omega, omega1, beta)

def x(A0, omega, delta0, beta, Bone, Btwo, omega1):
    return A0*np.cos(omega*t - delta0) + np.exp(-beta*t)*(Bone*np.cos(omega1*t) 
                                                         + Btwo*np.sin(omega1*t))

plt.plot(t, x(A0, omega, delta0, beta, Bone, Btwo, omega1), '-m')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()

def p(A0, omega, delta0):
    return A0*np.cos(omega*t - delta0)

def h(beta, Bone, Btwo, omega1):
    return np.exp(-beta*t)*(Bone*np.cos(omega1*t) + Btwo*np.sin(omega1*t))

plt.plot(t, p(A0, omega, delta0), '-.b', label = 'particular')
plt.plot(t, h(beta, Bone, Btwo, omega1), '--r', label = 'homogenous')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(loc = 'best')

plt.show()
    
# as the driving and natural freqeuncy are equal, complete destructive interference is
# possible. This occurs at about t = 15. As shown by the particular and homogenous 
# solutions plot, all of the transitory nature of the complete solution is due to the 
# homogenous part of the solution. We see by about t = 45, that the oscillation has 
# returned to the unpertured driving frequency and amplitude. 
