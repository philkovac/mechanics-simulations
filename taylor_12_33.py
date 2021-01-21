# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:44:12 2020

@author: rkovac
"""
# bifurcation diagram for the large r (chaotic) behavior of the logistic map. 
# this is pretty cool and did not take a fraction of time I expected to generate.

import numpy as np

x = 0.1

rval = []

xval = [x]

for r in np.arange(2.8, 4, 0.001):
    for j in range(700):
        x = r*x*(1 - x)
        xval.append(x)
    rval.append(xval)
    x = 0.1
    xval = [x]
    
import matplotlib.pyplot as plt

rar = []

for r in np.arange(2.8, 4, 0.001):
    rl = r*np.ones(199)
    rar.append(rl)

for j in range(len(rval)):
    plt.plot(rar[j], rval[j][500:699], 'ok', markersize = '0.05')
    plt.xlabel('r')
    plt.ylabel('x(t)')
    
plt.savefig('logistic_map_bifurcation.png', dpi=900, transparent=False, bbox_inches='tight')
    
# here we can see a single attractor grow as a function of r into a  
# period doubling cascade into chaos.
    