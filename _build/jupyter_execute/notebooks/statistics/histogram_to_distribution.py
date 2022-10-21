#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


x = random.normal(10.0, 3.0,size=200)


# In[3]:


plot(x)
xlabel('time',fontsize=16)
ylabel(r'$x$',fontsize=16)


# In[4]:


h = hist(x)
xlabel('bins of x')
ylabel('frequency of x')


# In[5]:


# make it yourself
pos = h[1][:-1]+diff(h[1])/2.
frequency = h[0]
bar(pos,frequency,width=1.4)


# In[6]:


# now we can normalize:
probability = frequency/sum(frequency)
bar(pos,probability,width=1.4)
xlabel('bins of x')
ylabel('probability')


# In[7]:


dx = diff(pos)[0]
print(('{:.2f}'.format(dx)))


# In[8]:


density = probability/dx
bar(pos,density,width=1.4)
xlabel('bins of x')
ylabel('probability density')


# In[9]:


z = (pos - x.mean())/x.std()


# In[10]:


# probability density function 
pdf = x.std() * density


# In[11]:


from scipy.stats import norm

y = norm.pdf( z, 0, 1)
bar(z,pdf,alpha=.3,width=.4),
zi = arange(-3,3,.1)
yi = norm.pdf( zi, 0, 1)
plot(zi, yi, 'k--', linewidth=2)
xlabel(r'$z$',fontsize=16)
ylabel(r'pdf', fontsize=16);

