# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:28:54 2020

@author: rkovac
"""


# bifurcation diagram for the large r (chaotic) behavior of the sine map. 
# this is pretty cool and did not take a fraction of time I expected to generate.

import numpy as np

x = 0.1

rval = []

xval = [x]

for r in np.arange(0.6, 1, 0.0001):
    for j in range(600):
        x = r*np.sin(np.pi*x)
        xval.append(x)
    rval.append(xval)
    x = 0.1
    xval = [x]
    
import matplotlib.pyplot as plt

rar = []

for r in np.arange(0.6, 1, 0.0001):
    rl = r*np.ones(199)
    rar.append(rl)

for j in range(len(rval)):
    plt.plot(rar[j], rval[j][400:599], 'ok', markersize = '0.01')
    plt.xlabel('r')
    plt.ylabel('x(t)')
    
plt.savefig('sine_map_bifurcation.png', dpi=900, transparent=False, bbox_inches='tight')
    
# here we can see a single attractor grow as a function of r followed by a 
# period doubling cascade into chaos.
    