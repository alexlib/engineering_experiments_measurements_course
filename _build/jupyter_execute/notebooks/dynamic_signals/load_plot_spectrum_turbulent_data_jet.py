#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pylab as p


# In[2]:


# u = np.loadtxt('../../data/data_for_FFT.txt')
data = np.loadtxt('../../data/p40_20.ts')
# data source:
# http://ldvproc.nambis.de/data/ektdata.html 


# In[3]:


p.plot(data[:500,0],data[:500,1])


# In[4]:


p.hist(data[:,1],101,density=True);


# In[5]:


u = data[:,1]

meanu = u.mean()
uf = u - meanu


# In[6]:


p.plot(uf[:100])


# In[7]:


def powerspectrum(x):
    s = np.fft.fft(x)
    return np.real(s*np.conjugate(s))


# In[8]:


specu = powerspectrum(uf)
lenu, = specu.shape


# In[9]:


p.plot(specu[2:np.int(lenu/2)])


# In[ ]:




