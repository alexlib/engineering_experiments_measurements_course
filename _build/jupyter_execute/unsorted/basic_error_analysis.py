#!/usr/bin/env python
# coding: utf-8

# # Basic error analysis
# 
# This part is the simplified error analysis that we will extend through the course with the more precise definitions
# and analysis using regressions, calibration, statistics, dynamics, etc.

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# ### Errors
# 1. Systematic errors
# 1. Random errors
# 
# 
# ### Errors
# 1. equipment/tool precision error
# 1. human error
# 1. external environmental effects
# 
# 
# ### Random errors
# 1. tool precision (below the resolution)
# 1. statistical errors
# 

# -----
# 
# ### Example: 
# Digital voltemeter measures 10.32 kV, it means its precision is 0.01kV, however the equipment has a sticker with the 
# statement of the basic calibrated errors and it says 1% of the measured value, i.e. 0.1kV for the given case. We use
# the maximum error contribution $$ \Delta = max ( x_i ) = max(0.1, 0.01) = 0.1 [kV] $$

# ### Statistical errors
# 
# We will study the basics of the statistical analysis (histograms, distributions, statistical tests) but for beginning 
# we can use the simple terms. 
# 
# If we assume that the random errors are distributed randomly from the normal distribution (Gaussian distribution), then
# we can believe that the expected value $ x_0 $ and the deviations $ \sigma $ will describe well the distribution such 
# that in 68% of cases our measured sample is within the range $(x_0 -\sigma, x_0 + \sigma)$. So we believe that our central value is the $x_0$ . 
# 
# Since we always measure only $N$ samples (finite number) we can at best estimate the arithmetic average $\overline{x}$ and standard deviation $S_x$ of the sample. So what we can measure is 
# 
# $$ x_0 \approx \overline{x} = \frac{1}{N} \sum\limits_{i=1}^{N} x_i $$
# 
# $$ \sigma \approx S_x = \sqrt{\frac{1}{N-1} \sum\limits_{i=1}^{N} \left( x_i - \overline{x} \right)^2 } $$
# 
# we can see that $S_x \to \sigma/\sqrt{N}$

# ### Total error estimate
# 
# If we can assume that only these two error sources are present, i.e. the equipment error $\Delta$ and the statistical, 
# random error $\sigma/\sqrt{N}$, then we can estimate the total error using the root-of-sum-squares method (there are also other methods too): $$ \Delta(x) = \sqrt{\Delta^2 + \sigma/N^2 } $$

# ### Example
# 
# Use the linear scale to measure in [cm]: 
#     10.0, 10.0, 9.9, 10.1, 9.6, 9.9, 10.3, 10.1, 10.0 
# 
# precision of the scale is 0.1 cm
# 
# We get $$\overline{x} = 9.99\ \mathrm{cm}$$, $$S = 0.179\ \mathrm{cm}$$
# 
# Then the statistical analysis error is $S/\sqrt{N} = 0.00566\ \mathrm{cm}$
# 
# And the total error estimate is: $$\Delta(x) = \sqrt{0.1^2 + 0.00566^2} = 0.1149\ \mathrm{cm}$$
# 
# and the output of the measurement is $$x = \left( 9.99 \pm 0.012 \right) \mathrm{cm}$$
# 
# note the use of the *significant digits* (we cannot report what we cannot know)

# ### Use of measured values in estimating parameters
# 
# Typically we use several measurements and use functions to combine them into parameters, i.e. $y = f(x_1, x_2)$ 
# 
# Then if we measured $x$ with the error $\Delta_x$, how large would be the error of $\Delta(y)$? 
# 
# The answer is simple $$\Delta_y = \Delta(f) = \left|\frac{df}{dx}\right|\Delta_x$$
# 
# if it's a function of several variables: $y = f(x_1,x_2)$, then: $$\Delta_y=\sqrt{\left(\frac{\partial f}{\partial x_1} \Delta x_1 \right)^2 + \left(\frac{\partial f}{\partial x_2} \Delta x_2 \right)^2}$$

# ### Example
# 
# 
# Volume of a cylinder is measured using the radius $r = 5.0 \pm 0.1$ cm and its height, $h = 1.30 \pm 0.1$ cm. The volume is estimated using $$V = \pi r^2 h $$
# 
# Therefore we got $ V = 1020.98 $ cm$^3$ and the error is estimated according to the derivatives. 
# 
# $$ \frac{\partial V}{\partial r} = 2 \pi r h$$ 
# $$ \frac{\partial V}{\partial h} = \pi r^2 $$
# 
# $$\Delta(V) = \sqrt{(2\pi r \Delta r)^2 + (\pi r^2 \Delta h)^2}  = 41.58 \mathrm{cm}^3 $$
# 
# $$ V = 1021.0 \pm 41.6 \mathrm{cm}^3 $$

# ### Note: if $x_1$ and $x_2$ are dependent, then 
# 
# $$\Delta_y=\left|\frac{\partial f}{\partial x_1} \Delta x_1 \right| + \left|\frac{\partial f}{\partial x_2} \Delta x_2 \right| $$
