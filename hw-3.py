#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


x = np.linspace(0, 2*np.pi,1000)

y = 5.5*np.cos(2*x) + 5.5
z = 0.02*np.exp(x)
w = 0.25*x**2 + 0.1*np.sin(10*x)


# In[ ]:



plt.plot(x, y, label=r'$y = (a)$')
plt.plot(x, z, label=r'$y = (b)$')
plt.plot(x, w, label=r'$y = (c)$')

plt.xlabel('time in ASTR 119')
plt.ylabel('measures of awesomeness')
plt.xlim([0,2*np.pi])
plt.ylim([-1,10])
plt.legend(loc=1,framealpha=0.95)


# In[ ]:




