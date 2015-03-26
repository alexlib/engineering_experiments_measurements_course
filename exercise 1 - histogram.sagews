︠8690fd77-fcc7-432e-ac78-0f799b309ab6a︠
%auto
typeset_mode(True, display=False)
%default_mode python
︠cdb2e319-49dd-4cc5-9658-552fb345aa4dai︠
%hide
%auto
DATA="foo.data/"
︠0b831f16-66fb-4f87-aad8-dc06cdc3de60︠
from pylab import *
x = array([12.1,12.3,12.2,12.2,12.4,12.3,12.2,12.4,12.2,12.5])
x_mean = mean(x)
x_median = median(x)
x_variance = var(x)
x_std = std(x)
x_modes = histogram(x)
x_mode_ind = argmax(x_modes[0])
x_mode_count = x_modes[0][x_mode_ind]
x_mode_val = x[x_mode_ind]
print "Data:"; print x
print "Mean: %f " % x_mean
print "Median: %f" % x_median
print "Variance: %f" % x_variance
print "STD: %f " % x_std
print "Mode of x %f appears %d times" % (x_mode_val,x_mode_count)
︡8443c617-28c7-474c-adc2-e1bb9bc20277︡{"stdout": "Data:\n[ 12.1  12.3  12.2  12.2  12.4  12.3  12.2  12.4  12.2  12.5]\nMean: 12.280000 \nMedian: 12.250000\nVariance: 0.013600\nSTD: 0.116619 \nMode of x 12.200000 appears 4 times"}︡
︠45d91777-b45d-44a5-862d-7c3a3dbb7279︠
xr = x_mean + x_std*rand(10000)
figure()
n, bins, patches = hist(x, 11, normed=1, facecolor='green', alpha=0.75)

from matplotlib.mlab import normpdf
y = normpdf( bins, x_mean, x_std)
l = plot(bins, y, 'r--', linewidth=2)
savefig('.')
︡afff4b68-3e0b-499e-b47b-e2ffc62c3cff︡{"stderr": "Traceback (most recent call last):    l = plot(bins, y, 'r--', linewidth=2)\n  File \"\", line 1, in <module>\n    \n  File \"/sagenb/sage_install/sage-4.8-sage.math.washington.edu-x86_64-Linux/devel/sagenb-git/sagenb/misc/support.py\", line 481, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\n  File \"/sagenb/sage_install/sage-4.8-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/python.py\", line 53, in eval\n    eval(compile(s, '', 'exec'), globals, globals)\n  File \"\", line 1, in <module>\n    \nNameError: name 'x_mean' is not defined"}︡









