# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:36:43 2020

@author: rkovac
"""


# population fate of the map f(x) = r*sin(pi*x). Investigating the period doubling 
# cascade that occurs in the map.

import numpy as np

#(a)
x = 0.8

r = 0.60

val0 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val0.append(x)
    
#(b)
x = 0.8

r = 0.79

val1 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val1.append(x)

#(c)
    
x = 0.8

r = 0.85

val2 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val2.append(x)
    
#(d)
    
x = 0.8

r = 0.865

val3 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val3.append(x)
    
t = np.arange(0, 21)

import matplotlib.pyplot as plt

plt.plot(t,val0, label = 'r = 0.60')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# for r = 0.6, we have one stable fixed point.

plt.plot(t,val1, label = 'r = 0.79')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# for r = 0.79, two fixed points are present as we see a two-cycle occur.
# In this situation, the two fixed points alternate stability as the attractor 
# becomes the repeller becomes the attractor...

plt.plot(t,val2, label = 'r = 0.85')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# for r = 0.85, four fixed points are present and we see a four-cycle occur. 
# I wonder if the Strogatz book has further discussions on what populations
# can be realistically modeled in this way...?

plt.plot(t,val3, label = 'r = 0.865')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# with r = 0.865, an eight-cycle occurs. these cascades are quite interesting!
# patterns before the chaos... but I don't completely know why this occurs...
