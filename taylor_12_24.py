# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:06:18 2020

@author: rkovac
"""


# population fate of the map f(x) = r*sin(pi*x) . Do these results agree with what was
# found in problem 12.23?

import numpy as np

#(a)
x = 0.3

r = 0.1

val0 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val0.append(x)
    
#(b)
x = 0.3

r = 0.5

val1 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val1.append(x)

#(c)
    
x = 0.3

r = 0.78

val2 = [x]

for j in range (20):
    x = r*np.sin(np.pi*x)
    val2.append(x)
    
t = np.arange(0, 21)

import matplotlib.pyplot as plt

plt.plot(t,val0, label = 'r =0.1')
plt.plot(t,val1, label = 'r =0.5')
plt.plot(t,val2, label = 'r =0.78')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

print(val1[20])

print(val2[15:20])

# the plot shows the different attractors (end fates) for the populations beginning 
# with the same initial population x0, but with differing growth parameters r. 
# as expected, when r < 1/pi ~ 0.318, there is a single stable fixed point at x* = 0. 
# once r excceds 0.318, a new stable fixed point is born as shown for r = 0.5. The value
# of this fixed point appears to be x* = 0.5 based on numerical calculations.
# upon further increasing r, a period doubling occurs where the fixed point part (b) 
# and a new fixed point alternate as the attractor for the population. The third fixed
# point to emerge is x* = 0.779971 found numerically. Can one find the latter fixed points
# analytically?

