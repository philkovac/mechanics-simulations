# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:12:32 2020

@author: rkovac
"""


# exploring the chaotic evolution of the logistic map: what populations will 
# converge?

import numpy as np

# (a)

r = 3.5

x = 0.4

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.5

xval0p = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0p.append(x) 
    
diff = []

for j in range(41):
    dl = np.abs(xval0[j] - xval0p[j])
    diff.append(dl)


import matplotlib.pyplot as plt

t = np.arange(0, 41)

plt.plot(t, np.log10(diff))
plt.xlabel('t')
plt.ylabel('log(|x`(t) - x(t)|)')

plt.show()

plt.plot(t, xval0, 'o', label = 'x0 = 0.4')
plt.plot(t, xval0p, 'o', label = 'x0 = 0.5')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# for the specified r parameter, and initial populations, we DO NOT see exponential 
# convergence of the population difference.

# based on the individual popualtion maps, it is clear that despite different 
# initial conditions, the popualtions are drawn to the same attractors (in this
# case, four of them). Due to differing initial conditions however, in particular when 
# each intial condition is close to an attractor, the populations develop antiphased
# with each other. on the other hand, when the initial conditions lie closer to
# one of attractors, the population difference will converge exponentially. Note, 
# there must be more than one attractor for this behavior to develop. 

# Another way of looking at this: If one population begins near a specific fixed point,
# and the other begins near another fixed point, the attractors from these different
# fixed points (which serve as repellers) are different. As a consequence, the popualtions
# will evolve some what antiphased as each unstable fixed point will feed into a 
# given stable fixed point. In order to have convergence in the difference between two 
# populations when period doubling occurs, the populations must begin 
# (or must be attracted to) the same stable fixed point. Otherwise, convergence in the
# population difference will not occur.


#(b)

r = 3.5

x = 0.45

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.5

xval0p = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0p.append(x) 
    
diff = []

for j in range(41):
    dl = np.abs(xval0[j] - xval0p[j])
    diff.append(dl)


import matplotlib.pyplot as plt

t = np.arange(0, 41)

plt.plot(t, np.log10(diff))
plt.xlabel('t')
plt.ylabel('log(|x`(t) - x(t)|)')

plt.show()

plt.plot(t, xval0, 'o', label = 'x0 = 0.4')
plt.plot(t, xval0p, 'o', label = 'x0 = 0.5')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# in (b) we increased one of the intial populations from x0= 0.4 to x0 = 0.45
# and we now see exponential convergence to zero of the populaltion difference. 
# also evident is the four-cycle in this population. 

#testing our hypothesis from part (a)

r = 3.5

x = 0.4

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.45

xval0p = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0p.append(x) 
    
diff = []

for j in range(41):
    dl = np.abs(xval0[j] - xval0p[j])
    diff.append(dl)


import matplotlib.pyplot as plt

t = np.arange(0, 41)

plt.plot(t, np.log10(diff))
plt.xlabel('t')
plt.ylabel('log(|x`(t) - x(t)|)')

plt.show()

plt.plot(t, xval0, 'o', label = 'x0 = 0.4')
plt.plot(t, xval0p, 'o', label = 'x0 = 0.45')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# agrees

r = 3.5

x = 0.4

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.42

xval0p = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0p.append(x) 
    
diff = []

for j in range(41):
    dl = np.abs(xval0[j] - xval0p[j])
    diff.append(dl)


import matplotlib.pyplot as plt

t = np.arange(0, 41)

plt.plot(t, np.log10(diff))
plt.xlabel('t')
plt.ylabel('log(|x`(t) - x(t)|)')

plt.show()

plt.plot(t, xval0, 'o', label = 'x0 = 0.4')
plt.plot(t, xval0p, 'o', label = 'x0 = 0.42')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

#agrees

r = 3.5

x = 0.4

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.8

xval0p = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0p.append(x) 
    
diff = []

for j in range(41):
    dl = np.abs(xval0[j] - xval0p[j])
    diff.append(dl)


import matplotlib.pyplot as plt

t = np.arange(0, 41)

plt.plot(t, np.log10(diff))
plt.xlabel('t')
plt.ylabel('log(|x`(t) - x(t)|)')

plt.show()

plt.plot(t, xval0, 'o', label = 'x0 = 0.4')
plt.plot(t, xval0p, 'o', label = 'x0 = 0.42')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()

# I think I have this!