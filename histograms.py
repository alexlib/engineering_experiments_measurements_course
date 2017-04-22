
# coding: utf-8

# ## Why do we need first to see the histogram? 
# 1. Not all measurements results are random
# 2. Not all random variables 'born equal'
# 3. Not every algrebraic average gives the 'mean'
# 4. Central limit theorem is a very powerful thing:
# https://www.youtube.com/watch?v=jvoxEYmQHNM

# In[37]:

get_ipython().magic(u'pylab inline')


# In[38]:

from scipy import stats


# In[39]:

X = stats.poisson(2.0)
smpl = X.rvs(size=20)/10.0
plot(smpl,'o')
aveX = smpl.mean()
stdX = smpl.std()
plot([0,20],[aveX,aveX],'-',lw=2)
ylim([-.2,.7])
print 'Average %4.3f' % aveX
print 'STD %4.3f' % stdX


# In[40]:

hist(smpl,bins=5)
plot([aveX, aveX],[0,10],'r-',lw=2)
xlabel(r'$x,\; \bar{x}$',fontsize=16)
ylabel('Probability count',fontsize=16)


# ### Can we write that our distribution is $ \bar{x} \pm S_x$ ? 
