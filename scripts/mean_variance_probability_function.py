
# coding: utf-8

# # Statistical parameters using probability density function
# ### Given probability density function, $p(x)$
# 
# $ p = 2x/b^2$, $0 < x < b$
# 
# ### The mean value of $x$ is estimated analytically:
# $\overline{x} = \int\limits_0^b x\, p(x)\, dx = \int\limits_0^b 2x^2/b^2 = \left. 2x^3/3b^2\right|_0^b =2b^3/3b^2 = 2b/3$
# 
# 
# ### the median
# median: $ \int\limits_0^m p(x)\,dx = 1/2 = \int\limits_0^m 2x/b^2\,dx = \left. x^2/b^2 \right|_0^m = m^2/b^2 = 1/2$, $m = b/\sqrt(2)$
# 
# ### the second moment
# second moment: $x^{(2)} = \int\limits_0^b x^2\, p(x)\, dx = \int\limits_0^b 2x^3/b^2 = \left. x^4/2b^2\right|_0^b =b^4/2b^2 = b^2/2$
# 
# ### the variance is the second moment less the squared mean value
# $var(x) = x^{(2)} - \overline{x}^2 = b^2/2 - 4b^2/9 = b^2/18$
# 
# 

# In[42]:

def p(x,b):
    return 2*x/(b**2)


# In[59]:

b = 2
x = linspace(0,b,200)
y = p(x,b) 


# In[63]:

plot(x,y)
xlabel('$x$')
ylabel('$p(x)$')


# In[61]:

# approximate using the numerical integration
print trapz(y*x,x)
print 2.*b/3


# In[62]:

print trapz(y*x**2,x)
print b^2/18


# In[64]:

import sympy


# In[113]:

sympy.var('x,b,p,m')
p = 2*x/b**2
print p


# In[114]:

sympy.integrate(p*x,(x,0,b))


# In[115]:

sympy.integrate(p*x**2,(x,0,b))


# In[119]:

sympy.integrate(p,(x,0,m))


# In[124]:

sympy.solve(m**2/b**2 - 0.5,m)


# In[ ]:



