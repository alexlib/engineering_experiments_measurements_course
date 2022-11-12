#!/usr/bin/env python
# coding: utf-8

# # Outliers

# In[1]:


import numpy as np
import matplotlib.pyplot as pl
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
mpl.rcParams['lines.linewidth']=2
mpl.rcParams['lines.color']='r'
mpl.rcParams['figure.figsize']=(10,8)
mpl.rcParams['font.size']=14
mpl.rcParams['axes.labelsize']=20


# ## Single variable, $x$

# In[2]:


x = np.array([49.3,50.2,49.2,49.8,50.5,49.3,48.9,49.9,50.1,49.2])


# In[3]:


pl.figure()
pl.plot(x,'o')
pl.xlim([-1,8])
pl.ylim([48,52])
pl.ylabel('$x$')
pl.xlabel('$n$')


# ## We use modified Thompson test (based on Student's t-distribution)

# ### Sort the values

# In[4]:


x.sort()


# In[5]:


x


# In[6]:


pl.plot(x,'o')
pl.xlim([-1,8])
pl.ylim([48,52])
pl.ylabel('$x$')
pl.xlabel('$n$')


# Note: we suspect in the sorted list of values the first and the last

# ### get the sample mean and sample standard deviation, get deviations

# In[7]:


x_mean = np.mean(x)
x_std = np.std(x,ddof=1)
print( x_mean)
print (x_std)


# $\delta_i = | x - x_i |$

# In[8]:


delta = abs(x - x_mean)
pl.plot(delta,'o')
pl.xlim([-1,8])
pl.ylim([-.5,1])
pl.ylabel('$\delta$')
pl.xlabel('$n$')
print (delta[0],delta[-1])


# In[ ]:




