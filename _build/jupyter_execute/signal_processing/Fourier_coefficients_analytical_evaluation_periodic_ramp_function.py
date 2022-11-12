#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
from sympy.plotting import plot
# init_printing(pretty_print=True,use_latex=True)
# %matplotlib inline
# import matplotlib.pyplot as plt
from numpy import arange


# In[2]:


f,t,T,G = symbols('f t T G')


# In[3]:


f = G*t-G/2
print ('f =', f)


# In[4]:


p = plot((f.subs(G,25),(t,0,1)),((f-25).subs(G,25),(t,1,2)),((f-50).subs(G,25),(t,2,3)), \
         ylabel = '$f = 25 t$ [V]', xlabel = '$t$ [sec]', xlim=(0,3), figsize=(10,8))


# In[5]:


c0 = integrate(f,(t,0,T))*(1/T)
print(c0) 
print (c0.subs([(G,25),(T,1)]))


# In[6]:


a1 = (2/T)*integrate(f*sin(2*pi*1*t),(t,0,T))


# In[7]:


print(a1)
print( a1.subs([(T,1),(pi, 3.14),(G,25)]))


# In[8]:


a,b = [],[]
for n in range(10):
    a.append((2/T)*integrate(f*sin(n*pi*t),(t,0,T)))
    b.append((2/T)*integrate(f*cos(n*pi*t),(t,0,T)))


# In[9]:


a[9], b[9]


# In[10]:


c = []
for n in range(1,10):
    print( a[n])
    expr = sqrt(a[n]**2 + b[n]**2)
    expr = expr.subs([(T,1),(pi, 3.14),(G,25)])
    # print expr
    # val = lambdify(t,expr,'numpy')
    c.append(expr)


# In[11]:


import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(10,8))
ax.bar(-.5+arange(1,10),c,alpha=.5)
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_xlabel('$n$',fontsize=16)
ax.set_ylabel('Fourier coefficients $a_n^2 + b_n^2$',fontsize=16)


# In[ ]:




