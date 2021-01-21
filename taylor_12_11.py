# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:08:28 2020

@author: rkovac
"""


import numpy as np

import matplotlib.pyplot as plt

x = np.array([1, 2, 3])

y = np.array([np.log(0.0130), np.log(0.0028), np.log(0.0006)])

m, b = np.polyfit(x, y, 1)

plt.plot(x,y, 'o')
plt.plot(x, m*x+b)
plt.xlabel('n')
plt.ylabel('$\ln(\Delta\gamma$)')

Feigenbaum_delta = np.exp(-m)

#pretty damn close for three data points!