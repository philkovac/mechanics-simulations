# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:15:03 2020

@author: rkovac
"""

# bifurcation diagram for the logistic map. My first bifurcation diagram!


import numpy as np

x = 0.1

rval = []

xval = [x]

for r in np.arange(0, 3.55, 0.01):
    for j in range(60):
        x = r*x*(1 - x)
        xval.append(x)
    rval.append(xval)
    x = 0.1
    xval = [x]
    
import matplotlib.pyplot as plt

rar = []

for r in np.arange(0, 3.55, 0.01):
    rl = r*np.ones(9)
    rar.append(rl)

for j in range(len(rval)):
    plt.plot(rar[j], rval[j][50:59], 'ok', markersize = '1')
    plt.xlabel('r')
    plt.ylabel('x(t)')
    
# here we can see a single attractor at x = 0 grow to a variable single attractor
# as a function of r followed by a period doubling cascade.
    