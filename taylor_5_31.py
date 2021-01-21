# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:20:40 2020

@author: rkovac
"""


import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('seaborn-whitegrid')

t = np.arange(0, 3, 0.01)

# underdamped oscillatory function

def u(x0, v0, beta, omega0):
   return np.e**(-beta*t)*(x0*np.cos((omega0**2-beta**2)**(1/2)*t)
                           +((2*v0 + beta*x0)/(omega0**2-beta**2)**(1/2))*
                           np.sin((omega0**2-beta**2)**(1/2)*t))

# plotting underdamped oscillator for three periods with damping parameter 
# values ranging  beta = 0, 1, 2, 4, 6

plt.plot(t, u(1, 0, 0, 2*np.pi), '-.b', label = r'$\beta$ = 0')
plt.plot(t, u(1, 0, 1, 2*np.pi), '--g', label = r'$\beta$ = 1')
plt.plot(t, u(1, 0, 2, 2*np.pi), ':r', label = r'$\beta$ = 2')
plt.plot(t, u(1, 0, 4, 2*np.pi), '-c', label = r'$\beta$ = 4')
plt.plot(t, u(1, 0, 6, 2*np.pi), '-m', label = r'$\beta$ = 6')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
 
plt.show()

# now for a critically damped oscillator  

def c(x0, v0, omega0):
    return x0*np.e**(-omega0*t) + (x0*omega0 + v0)*t*np.e**(-omega0*t)

plt.plot(t, c(1, 0, 2*np.pi), label = r'$\beta$ = $\omega_0$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()

#comparing a critically damped and ALMOST critically damped oscillator

plt.plot(t, u(1, 0, 6, 2*np.pi), '--m', label = r'$\beta$ = 6')
plt.plot(t, c(1, 0, 2*np.pi), label = r'$\beta$ = $\omega_0$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()

plt.show()

#lastly an we'll compare several overdamped oscillators with increasing damping parameters

def o(x0, v0, beta, omega0):
    return np.e**(-beta*t)*((x0/2 + (x0*beta + v0)/
                             (2*(beta**2-omega0**2)**(1/2)))*
                            np.e**((beta**2 - omega0**2)**(1/2)*t)
                            + (x0/2 - (x0*beta + v0)/(2*(beta**2-omega0**2)**(1/2)))*
                            np.e**(-(beta**2 - omega0**2)**(1/2)*t))

plt.plot(t, o(1, 0, 3*np.pi, 2*np.pi), '-.b', label = r'$\beta$ = 3$\pi$')
plt.plot(t, o(1, 0, 4*np.pi, 2*np.pi), '--g', label = r'$\beta$ = 4$\pi$')
plt.plot(t, o(1, 0, 6*np.pi, 2*np.pi), ':r', label = r'$\beta$ = 6$\pi$')
plt.plot(t, o(1, 0, 8*np.pi, 2*np.pi), '-c', label = r'$\beta$ = 8$\pi$')
plt.plot(t, o(1, 0, 10*np.pi, 2*np.pi), '-m', label = r'$\beta$ = 10$\pi$')
plt.plot(t, o(1, 0, 20*np.pi, 2*np.pi), '-y', label = r'$\beta$ = 20$\pi$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend();

plt.show()

# we see that when an oscillator is signifcantly overdamped, it takes a long
# time to return to equilibrium! 
# this is a bad things for a mechanical system!