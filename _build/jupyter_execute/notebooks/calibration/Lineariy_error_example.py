#!/usr/bin/env python
# coding: utf-8

# # Linearity error example

# In[1]:


import numpy as np
import matplotlib.pyplot as pl
get_ipython().run_line_magic('matplotlib', 'inline')

pl.rcParams['figure.figsize'] = 10, 8 
pl.rcParams['font.size'] = 18


# In[2]:


x = np.r_[np.linspace(20,220,10), np.linspace(180,0,9)]
y = np.array([20,40,59,77,97,117,137,156,175,195,176,156,136,117,97,78,58,39,20])


# In[3]:


print(f'x = {x}')
print(f'y = {y}')


# In[4]:


pl.plot(x,y,'--o')
pl.xlabel(r'$x$')
pl.ylabel(r'$y$')


# In[5]:


# create best fit
p = np.polyfit(x,y,1)
print (p)
y_fit = np.polyval(p,x)


# In[6]:


pl.plot(x,y,'ro',x,y_fit,'b--')
pl.xlabel(r'$x$')
pl.ylabel(r'$y$')
pl.legend(('data','fit'),loc='best')


# In[7]:


print (f'measured y = {y}')
print (f'estimated y = {y_fit}')


# # Linearity error
# $\epsilon_L = |y_L - y|$
# 
# $\epsilon_{L_{max}} = max(\epsilon_L)$
# 
# $r_0 = y_{max} - y_{min}$
# 
# $\% \epsilon_{L_{max}} = \frac{\epsilon_{L_{max}}}{r_0}\times 100$
# 

# In[8]:


epsilon_L = abs(y - y_fit)
epsilon_L_max = max(epsilon_L)
r0 = max(y) - min(y)
percent_epsilon_L_max = epsilon_L_max/r0 * 100.


# In[9]:


pl.errorbar(x,y_fit,10*epsilon_L)
pl.xlabel(r'$x$')
pl.ylabel(r'$y$')

print ('max error is %4.3f' % epsilon_L_max)
print ('the range is %4.3f' % r0)
print ('Linearity error is %3.2f%s' % (percent_epsilon_L_max,'%'))


# In[ ]:




