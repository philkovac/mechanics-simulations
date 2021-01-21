# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:07:45 2020

@author: rkovac
"""
import matplotlib.pyplot as plt 

import numpy as np

plt.style.use('seaborn-whitegrid')

t = np.arange(0, 4, 0.01)

omega0 = 5*2*np.pi; 

omega = 2*np.pi; 

beta = 2*np.pi/4;

omega1 = np.sqrt(omega0**2 - beta**2);

f0 = 1000; 

x0 = 2;

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

Bonex = B1(0, A0, delta0);

Boney = B1(2, A0, delta0);

Btwox = B2(0, v0, A0, delta0, omega, omega1, beta)

Btwoy = B2(2, v0, A0, delta0, omega, omega1, beta)

def x(A0, omega, delta0, beta, Bonex, Btwox, omega1):
    return A0*np.cos(omega*t - delta0) + np.exp(-beta*t)*(Bonex*np.cos(omega1*t) 
                                                         + Btwox*np.sin(omega1*t))

def y(A0, omega, delta0, beta, Boney, Btwoy, omega1):
    return A0*np.cos(omega*t - delta0) + np.exp(-beta*t)*(Boney*np.cos(omega1*t) 
                                                         + Btwoy*np.sin(omega1*t))

plt.plot(t, x(A0, omega, delta0, beta, Bonex, Btwox, omega1), '--b', label = 'x0 = 0')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()

plt.plot(t, y(A0, omega, delta0, beta, Boney, Btwoy, omega1), '-.r', label = 'x0 = 2')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()

plt.plot(t, x(A0, omega, delta0, beta, Bonex, Btwox, omega1), '--b', label = 'x0 = 0')
plt.plot(t, y(A0, omega, delta0, beta, Boney, Btwoy, omega1), '-.r', label = 'x0 = 2')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend() 

plt.show()

# comparing the same driven damped linear oscillator with different initial conditions,
# we see the despite the first few periods of varying behavior, the oscialltor is always
# attracted to the driven frequency AND amplitude. THIS IS SUPRISING AND REVEALING!.

    