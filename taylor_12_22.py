# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# demonstrating the "basin of attraction" for the map f(x) = x^2. 
# the stable fixed point lies at x = 0. There is an unstable fixed point at x = 1. 
# see ipad notability notes for more info.

import numpy as np

xval =[]

for j in range (19):
    x = -0.9 + 0.1*j
    y = [x]
    for j in range(1,20):
        x = x**2
        y.append(x)
    xval.append(y)
    
t = np.arange(1,21)

import matplotlib.pyplot as plt

plt.plot(t, xval[0])
plt.plot(t, xval[1])
plt.plot(t, xval[2])
plt.plot(t, xval[3])
plt.plot(t, xval[4])
plt.plot(t, xval[5])
plt.plot(t, xval[6])
plt.plot(t, xval[7])
plt.plot(t, xval[8])
plt.plot(t, xval[9])
plt.plot(t, xval[10])
plt.plot(t, xval[11])
plt.plot(t, xval[12])
plt.plot(t, xval[13])
plt.plot(t, xval[14])
plt.plot(t, xval[15])
plt.plot(t, xval[16])
plt.plot(t, xval[17])
plt.plot(t, xval[18])
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()

# with intial population values from -0.9 to 0.9, after twenty generations, the 
# population always converges to the fixed attractor x=0. This range of initial
# populations consitutes the "basin of attraction" What occurs if we consider
# initial popualtions outside of the basin of attraction? 

val =[]

for j in range (10):
    f = 1 + 0.1*j
    g = [f]
    for j in range(1,11):
        f = f**2
        g.append(f)
    val.append(g)
    
t = np.arange(1,12)
    
plt.plot(t, val[0])
plt.plot(t, val[1])
plt.plot(t, val[2])
plt.plot(t, val[3])
plt.plot(t, val[4])
plt.plot(t, val[5])
plt.plot(t, val[6])
plt.plot(t, val[7])
plt.plot(t, val[8])
plt.plot(t, val[9])
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()

# with initial population values outside of the basin of attraction, the population
# after about ten generations diverges to infinity.
