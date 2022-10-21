#!/usr/bin/env python
# coding: utf-8

# ## Amplitude, frequency, period, and phase

# A periodic function can be characterized by the properties: amplitude, frequency, period, and phase. Let's exemplify these properties for a pediodic function composed by a single frequency, the sine wave or sinusoid [trigonometric function](http://en.wikipedia.org/wiki/Trigonometric_functions):
# 
# $$ x(t) = Asin(2 \pi f t + \phi) $$
# 
# Where $A$ is the amplitude, $f$ the frequency, $\phi$ the phase, and $T=1/f$ the period of the function $x(t)$.  
# 
# We can define $\omega=2\pi f = 2\pi/T$ as the angular frequency, then:
# 
# $$ x(t) = Asin(\omega t + \phi) $$
# 
# Let's visualize this function:

# In[1]:


from __future__ import division, print_function  # for version compatibility
get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


t = linspace(-2, 2, 101)                    # time vector
qi = 1 * sin(2*t) + 0.3*sin(20*t)
qo1 = 0.93 * sin(2*t - 21.8/180*pi) + 0.072 * sin(20*t - 76./180*pi)
qo2 = 1 * sin(2*t - 0.23/180*pi) + 0.3 * sin(20*t - 2.3/180*pi)


# In[3]:


figure(figsize=(10,8))
plot(t,qi,'bo',t,qo1,'r-.',t,qo2,'g-',lw=2)
grid('on')
xlabel('$t$',fontsize=18)
ylabel('$q_i,q_o$',fontsize=18)
show()


# In[ ]:




