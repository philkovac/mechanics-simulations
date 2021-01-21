# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:11:16 2020

@author: rkovac
"""

import matplotlib.pyplot as plt 

import numpy as np

plt.style.use('seaborn-whitegrid')

t = np.arange(0, 12, 0.01)

omega = 2*np.pi; 

omega0 = 0.25*omega; 

beta = 0.2*omega0;

omega1 = np.sqrt(omega0**2 - beta**2);

f0 = 1000; 

x0 = 0;

v0 = 0;

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

plt.plot(t, x(A0, omega, delta0, beta, Bone, Btwo, omega1), '-.b')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()

#now the driver osciallations are higher frequency than the damped osciallator frequency. 
# by two oscillations at the damped frequency the oscillator has settled to the attractor
# frequency of the driver.

# we can also plot the particular and homogenous solutions separately along with the 
# complete solutions

def p(A0, omega, delta0):
    return A0*np.cos(omega*t - delta0)

def h(beta, Bone, Btwo, omega1):
    return np.exp(-beta*t)*(Bone*np.cos(omega1*t) + Btwo*np.sin(omega1*t))

plt.plot(t, p(A0, omega, delta0), '-.b', label = 'particular')
plt.plot(t, h(beta, Bone, Btwo, omega1), '--r', label = 'homogenous')
plt.plot(t, x(A0, omega, delta0, beta, Bone, Btwo, omega1), '-m', label = 'complete')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()
    
# the three different plots here tell it all. The driving frequency (particualr solution) 
#is constant. The homogenous solution is transitory and damps out. The sum of these two 
# yields quite interesting dynamics. 