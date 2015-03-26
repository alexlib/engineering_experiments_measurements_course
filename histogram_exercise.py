# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>
from pylab import *
data = loadtxt('thermocouples.dat',skiprows=1)
t = data[:,0]
T = data[:,1]
plot(t,T)
show()

# <codecell>

print 1 + 3.3*log10(len(t))
print 2*len(t)**(0.33)

# <codecell>

J = 11
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
show()

# <codecell>

J = 19
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
show()

# <codecell>

J = 15
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
show()

# <codecell>

# vertical normalization
p = n/1000.
plot(x,p)

# <codecell>

# area normalization
f = p/diff(x)[0]
plot(x,f)
show()

# <codecell>

# horizontal normalization
z = (x - T.mean())/T.std()
plot(z,f)
show()

# <codecell>

def gaussian(x,mu,sig):
    return 1/(sig*sqrt(2*pi))*exp(-((x-mu)**2)/(2*sig**2))

plot(z,f,z,gaussian(z,0,1),'r')
show()

# <codecell>

import scipy.stats as st

print "T skewness = %f, kurtosis = %f" % (st.skew(T), st.kurtosis(T))
tmp = randn(1000,1)
print "Normal distribution skewness = %f, kurtosis = %f" % (st.skew(tmp), st.kurtosis(tmp))

# <codecell>

# area under the curve
print "Area under the curve = %f " % trapz(f,x)

# <codecell>


