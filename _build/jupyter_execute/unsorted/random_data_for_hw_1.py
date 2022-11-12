#!/usr/bin/env python
# coding: utf-8

# # Run the random data generator and plot the scatter

# In[1]:


get_ipython().run_line_magic('run', '../scripts/create_random_data')


# In[2]:


from random import randint
c, T = create_random_set(randint(5,20))
print('\n'.join('{0:.3f} {1:.3f}'.format(*k) for k in zip(c,T)))


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(c,T,'o',markersize=10)
plt.xlabel('c',fontsize=14)
plt.ylabel('T',fontsize=14)


# In[ ]:





# In[ ]:





# In[ ]:




