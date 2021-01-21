# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:43:37 2020

@author: rkovac
"""
# iterating the "map" f(x) = cos(x) for various initial conditions. 

import numpy as np

a = 0

p = [a]

for j in range (1, 30):
    a = np.cos(a)
    p.append(a)
    
b = np.pi/2

q = [b]

for j in range (1, 30):
    b = np.cos(b)
    q.append(b)
    
c = np.pi

r = [c]

for j in range (1, 30):
    c = np.cos(c)
    r.append(c)
    
d = -np.pi

s = [d]

for j in range (1, 30):
    d = np.cos(d)
    s.append(d)
    
e = -np.pi/2

u = [e]

for j in range (1, 30):
    e = np.cos(e)
    u.append(e)
    
import matplotlib.pyplot as plt

t = np.arange(1, 31)
    
plt.plot(t,p, label = 'x0 = 0')
plt.plot(t,q, label = 'x0 = $\pi/2$')
plt.plot(t,r, label = 'x0 = $\pi$')
plt.plot(t,s, label = 'x0 = $-\pi$')
plt.plot(t,u, label = 'x0 = $-\pi/2$')
plt.xlabel('t')
plt.ylabel('cos(t)')
plt.legend()

plt.show()

# despite the different intiial conditions, by iterating the map, we suprisingly
# see a single fixed attractor at! The value of the attractor is x = 0.739085

print(p[29])
print(q[29])
print(r[29])
print(s[29])
print(u[29])

tp = np.arange(-1, 1, 0.01)


plt.plot(tp, np.cos(tp))
plt.plot(tp,tp)

plt.show()
# by plotting y= f(x) with y = x, we see the reason for the stable fixed point 
# at x = 0.739085. This is the value where f(x) = x, and as |-sin(0.739085)| = 0.6736
# < 1, this fixed point is stable. 
