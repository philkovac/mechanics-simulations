# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:40:55 2020

@author: rkovac
"""
#demonstration of the fixed points in the map f(x) = r*sin(pi*x)

import numpy as np

x = np.arange(0, 1, 0.01)

r = np.arange(0, 1, 0.1)

import matplotlib.pyplot as plt

plt.plot(x, x)
plt.plot(x, r[1]*np.sin(np.pi*x), label = 'r = 0.1')
plt.plot(x, r[2]*np.sin(np.pi*x), label = 'r = 0.2')
plt.plot(x, (1/np.pi)*np.sin(np.pi*x), label = 'r = 1/$\pi$')
plt.plot(x, r[5]*np.sin(np.pi*x), label = 'r = 0.5')
plt.plot(x, r[8]*np.sin(np.pi*x), label = 'r = 0.8')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
