# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:19:27 2020

@author: rkovac
"""


# exploring the chaotic evolution of the logistic map. 

import numpy as np

# (a)

r = 2.6

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

# for the specified r parameter, in (a) we see exponential convergence to zero

#(b)

r = 3.3

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

# despite the presence of a two-cycle, we still see (a quicker!) exponential 
# convergence to 0 for the  population difference for the specified r in (b)

# (c)

r = 3.6

x = 0.4

xval0 = [x]

for j in range(40):
    x = r*x*(1 - x)
    xval0.append(x)
    
x = 0.400001

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

# in part (c) we see quite different behavior. Importantly we began the popualtions 
# within 10^-5 of each other. Even with this, the popualtion difference diverges
# gaining four orders of magnitude over 40 populations. Let's look at one of these
# chaotic populations. 

plt.plot(t, xval0)
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()

# what populations (or under what conditions) behave this way?
