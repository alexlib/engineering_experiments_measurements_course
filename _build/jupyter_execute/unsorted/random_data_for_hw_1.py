#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys; sys.path.append('../../scripts')
from create_random_data import create_random_set
from random import randint
c, T = create_random_set(randint(5,20))
print('\n'.join('{0:.3f} {1:.3f}'.format(*k) for k in zip(c,T)))


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(c,T,'o',markersize=10)
plt.xlabel('c',fontsize=14)
plt.ylabel('T',fontsize=14)


# In[ ]:





# In[ ]:




