# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python [conda env:mdd] *
#     language: python
#     name: conda-env-mdd-py
# ---

# %% [markdown]
# ## Introduction to linear regression
#
# Based on the example given in http://onlinestatbook.com/2/regression/intro.html

# %% jupyter={"outputs_hidden": false}
import numpy as np
import matplotlib.pyplot as pl
# %pylab inline 
# allows to use everything from Numpy and Matplotlib like in Matlab, without np. and plt.

from IPython.display import Image 
# allows to show images from the web: Image(filename='hysteresis_example.png',width=400)

# %% jupyter={"outputs_hidden": false}
# Let's use some simple example of two variables, x,y
x = array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 2.0, 1.30, 3.75, 2.25])

# %% jupyter={"outputs_hidden": false}
plot(x,y,'o',markersize=10)
xlim([0.0, 6.0])
ylim([0.0, 4.0])
xlabel('$x$',fontsize=16)
ylabel('$y$',fontsize=16)

# %% [markdown]
# In simple linear regression, the topic of this section, the predictions of Y when plotted as a function of X form a straight line.
# Linear regression consists of finding the best-fitting straight line through the points. The best-fitting line is called a regression line. The black diagonal line in Figure 2 is the regression line and consists of the predicted score on Y for each possible value of X. The vertical lines from the points to the regression line represent the errors of prediction.

# %% jupyter={"outputs_hidden": false}
# Image(url='http://onlinestatbook.com/2/regression/graphics/reg_error.gif')
Image(filename='../../img/reg_error.png',width=400)

# %% [markdown]
# The error of prediction for a point is the value of the point minus the predicted value (the value on the line). Table 2 shows the predicted values (Y') and the errors of prediction (Y-Y'). For example, the first point has a Y of 1.00 and a predicted Y (called Y') of 1.21. Therefore, its error of prediction is -0.21.
#
# The formula for the regression line is 
#
# $$ y' = b \cdot x + a $$
#
# Let's assume we try some values of $a,b$: 
#
# $$ y' = 0.425\, x + 0.758 $$

# %% jupyter={"outputs_hidden": false}
b = 0.425
a = 0.785

ytag = x*b + a
print("y'" % ytag)
print('original y:' % y)

# %% jupyter={"outputs_hidden": false}
e = ytag - y
print('Errors:' % e)

# %% [markdown]
# ### Computing the Regression Line
#
# In the age of computers, the regression line is typically computed with statistical software. However, the calculations are relatively easy, and are given here for anyone who is interested. The calculations are based on the statistics shown in Table 3. $M_x$ is the mean of $X$, $M_y$ is the mean of $Y$, $S_x$ is the standard deviation of $X$, $S_y$ is the standard deviation of $Y$, and $r$ is the correlation between $X$ and $Y$.
#
# ### Formulae for standard deviations and correlation
#
# $$ S_x = \frac{1}{N} \sum (x-\bar{x})^2 $$
#
# $$ S_y = \frac{1}{N} \sum (y-\bar{y})^2 $$
#
# $$ R = \frac{1}{S_x S_y} \sum (x-\bar{x})(y - \bar{y}) $$
#

# %% jupyter={"outputs_hidden": false}
Mx = mean(x)
My = mean(y)
Sx = std(x,ddof=1) # note the ddof=1 which means N-1 
Sy = std(y,ddof=1)
Sxy = corrcoef(x,y)
R = Sxy[0,1] # off-diagonal is the correlation coefficient
print('%4.3f %4.3f %4.3f %4.3f %4.3f' % (Mx,My,Sx,Sy,R))

# %% [markdown]
# $$ b = R \; Sy/Sx $$
# $$ a = \bar{y} - b \bar{x} $$

# %% jupyter={"outputs_hidden": false}
b = R*Sy/Sx; print('b = %4.3f' % b)
a = My - b*Mx; print('a = %4.3f'% a)

# %% [markdown]
# ## Regression analysis
# Following the recipe of http://www.answermysearches.com/how-to-do-a-simple-linear-regression-in-python/124/

# %% jupyter={"outputs_hidden": false}
# # %load ../../scripts/linear_regression.py
from numpy import sqrt

def linreg(X, Y):
    """
    Summary
        Linear regression of y = ax + b
    Usage
        real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
    """
    N = len(X)

    if N != len(Y):  raise(ValueError, 'unequal length')

    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y

    det =  Sx * Sx - Sxx * N # see the lecture

    a,b = (Sy * Sx - Sxy * N)/det, (Sx * Sxy - Sxx * Sy)/det

    meanerror = residual = residualx = 0.0

    for x, y in zip(X, Y):
        meanerror = meanerror + (y - Sy/N)**2
        residual = residual + (y - a * x - b)**2
        residualx = residualx + (x - Sx/N)**2

    RR = 1 - residual/meanerror
    # linear regression, a_0, a_1 => m = 1
    m = 1
    nu = N - (m+1)

    sxy = sqrt(residual / nu)

    # Var_a, Var_b = ss * N / det, ss * Sxx / det

    Sa = sxy * sqrt(1/residualx)
    Sb = sxy * sqrt(Sxx/(N*residualx))


    # We work with t-distribution, ()
    # t_{nu;\alpha/2} = t_{3,95} = 3.18

    print("Estimate: y = ax + b")
    print("N = %d" % N)
    print("Degrees of freedom $\\nu$ = %d " % nu)
    print("a = %.2f $\\pm$ %.3f" % (a, 3.18*Sa/sqrt(N)))
    print("b = %.2f $\\pm$ %.3f" % (b, 3.18*Sb/sqrt(N)))
    print("R^2 = %.3f" % RR)
    print("Sxy = %.3f" % sxy)
    print("y = %.2f x + %.2f $\\pm$ %.2fV" % (a, b, 3.18*sxy/sqrt(N)))
    return a, b, RR, sxy

# %% jupyter={"outputs_hidden": false}
a, b, RR, sxy = linreg(x,y)

# %% [markdown]
# ### Standardized Variables
#
# The regression equation is simpler if variables are **standardized** so that their means are equal to 0 and standard deviations are equal to 1, for then $b = r$ and $a = 0$. This makes the regression line:
#
# $$ Z_y = (R)(Z_x) $$
#
# where $Z_y = y - \bar{y}$, $Z_x = x - \bar{x}$, $R$ is the correlation, Note that the slope of the regression equation for standardized variables is $R$.

# %% jupyter={"outputs_hidden": false}
figure(figsize=(10,8))
plot(x,y,'o',markersize=8)
xlim([0.0, 6.0])
ylim([0.0, 4.0])
xlabel('$x$',fontsize=16)
ylabel('$y$',fontsize=16)
plot(x,ytag,'-',lw=2)
legend((r'$y$',r"$y'$"),fontsize=16)

# %% [markdown]
# # Estimate $a,b$ and also $\Delta a$ and $\Delta b$
#
# We start with the list of $N$ points $x_i,y_i$ and we assume that the errors in $\Delta x \ll \Delta y$. Our goal is to minimize the sum of all the deviations, $d_i = y_i - (a x_i + b)$
#
# For that, we shall minimize the sum of square errors: $$ S^2 = \sum\limits_{i=1}^{N} d_i^2 = \sum\limits_{i=1}^{N} \left( y_i - a x_i - b \right)^2$$
#
# In order to find those we need to derive $S^2$ by $b$ and by $a$ and solving for zero we get two equations that provide us the minimum. The equations we get are: $$a = \frac{1}{A}\left(N S_{xy} - S_y S_x \right) $$ $$b = \frac{1}{A} \left(S_{xx} S_{y} - S_{xy} S_x \right) $$ 
# where
# $$S_x = \sum\limits_{i=1}^{N} x_i $$
# $$S_y = \sum\limits_{i=1}^{N} y_i $$
# $$S_{xx} = \sum\limits_{i=1}^{N} x_i^2 $$
# $$S_{yy} = \sum\limits_{i=1}^{N} y_i^2 $$
# $$S_{xy} = \sum\limits_{i=1}^{N} x_i y_i $$
# $$A \equiv N S_{xx} - S_x^2 $$
#
#
# Then we can measure both $a$ and $\Delta a$: $$ \Delta a = \sigma_y \sqrt{N/A} $$ $$\Delta b = \sigma_y \sqrt{S_{xx}/A}$$
#
# and the error is $$\Delta y = \frac{1}{N} \sum\limits_{i=1}^{N} \Delta y_i $$ and the deviation of the errors is 
# $$ \sigma_y = \sqrt{\frac{1}{N-2}\sum d_i^2} = $$ 
# $$ = \sqrt{\frac{1}{N-2}\left(S_{yy} + a^2 S_{xx} +Nb^2 - 2aS_{xy} -2bS_{y} + 2abS_x \right) }$$

# %% [markdown]
# ### Example

# %% jupyter={"outputs_hidden": false}
import numpy as np
x = np.arange(2.,11.)
y = np.array([14.5, 16.0, 18.5, 20.0, 22.5, 24.5, 26.0, 27.0, 29.0])

# %% [markdown]
# ### let's assume $\Delta x = 0$, $\Delta y = 0.2$

# %% jupyter={"outputs_hidden": false}


Sx = np.sum(x)
Sy = np.sum(y)
Sxx = np.sum(x**2)
Syy = np.sum(y**2)
Sxy = np.sum(x*y)
N = x.size
A = N*Sxx - Sx**2

# %% jupyter={"outputs_hidden": false}
a = 1./A*(N*Sxy - Sy*Sx)
b = 1./A*(Sxx*Sy - Sxy*Sx)
print('a,b = %3.2f,%3.2f' % (a,b))

# %%
d = (y - (a*x + b))

# %% jupyter={"outputs_hidden": false}
pl.plot(x,y,'o',x,a*x+b,'--')

# %% jupyter={"outputs_hidden": false}
sigma = np.sqrt((1./(N-2)*np.sum(d**2)))
print('sigma_y = %4.3f' % sigma)

# %% jupyter={"outputs_hidden": false}
delta_y = 0.2
delta_a = sigma * np.sqrt(N/A); print('\\Delta a = %4.3f' % delta_a)
delta_b = sigma * np.sqrt(Sxx/A); print('\\Delta b = %4.3f' % delta_b)

# %% [markdown]
# ### Final result is:
#
# $$ a = 1.84 \pm 0.06 $$ 
# $$ b = 10.95 \pm 0.46 $$

# %%
