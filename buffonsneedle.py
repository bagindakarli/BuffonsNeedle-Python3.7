#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

# initialization
n = 100
d = 5.0   # line width
l = 4.5   # needle length

# iteration
n_hits = 0
for i in range(n):
    theta = np.random.rand() * (np.pi/2)
    x = np.random.rand() * d
    if x <= (1 * np.cos(theta)):
        n_hits += 1
pi = ((2*1)/d) * (n/n_hits)

print('N : ', n)
print('d : ', d)
print('l : ', l)
print('n_hits :', n_hits)
print('pi : ', pi)

