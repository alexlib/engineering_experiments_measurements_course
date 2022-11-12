#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as pl
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = np.loadtxt('../data/sizedistribution.dat');
vals = data[:,1]
num = data[:,0]


# In[3]:


pl.plot(num,vals)


# Isn't it clear that the plot is not like "random variable" ?

# In[4]:


pl.hist(vals,21)


# In[5]:


pl.hist(np.log(vals),21)


# In[6]:


newvals = np.log(vals)


# In[7]:


pl.plot(num,newvals)


# In[8]:


print("Wrong:")
print ("Average =  %.3f" %np.mean(vals))
print ("Standard Deviation = %.3f" %np.std(vals))

print ("Correct:")
print ("Average =  %.3f" % np.exp(np.mean(newvals)))
print ("Standard Deviation = %.3f" % np.exp(np.std(newvals,ddof=1)))


# In[9]:


from scipy.stats import lognorm, norm
param = norm.fit(newvals)


# In[10]:


x = np.linspace(np.min(newvals),np.max(newvals),100)
# fitted distribution
pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])


# In[11]:


pl.figure()
pl.plot(x,pdf_fitted,'r-')
pl.hist(newvals,density=1,alpha=.3)


# In[12]:


print(param) # log normal
print(np.exp(param))


# In[ ]:




