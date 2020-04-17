---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python [conda env:mdd] *
    language: python
    name: conda-env-mdd-py
---

<!-- #region slideshow={"slide_type": "slide"} -->
# Statistics example
## Testing for normal distribution
### pressure transducer calibration example

Given: 20 trials of pressure reading using a pressure transducer

True pressure: $10.000 \pm 0.001$ kPa  
Acceleration = 0  
Vibration = 0  
Ambient temperature = $20 \pm 1^\circ$C
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
%pylab inline

from IPython.display import Image
from IPython.core.display import HTML 
Image(filename = "../../img/pressure_calibration_table.png", width=300)
```

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
P = array([10.02, 10.20, 10.26, 10.20, 10.22, 10.13, 9.97, 10.12, 10.09, 9.90, \
     10.05, 10.17, 10.42, 10.21, 10.23, 10.11, 9.98, 10.10, 10.04, 9.81])

figure(figsize=(8,4))
plot(P,'o',markersize=10)
plot(P.mean()*ones(size(P)),'r--',lw=2)
plot(10*ones(size(P)),'k-',lw=2)
text(6.,P.mean()+.05,'Average',fontsize=14,color='r')
text(5.,10.01,'True',fontsize=14)
xlabel('trial')
ylabel(r'$P$ [kPa]') 
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Calculate the descriptive statistics 

1. Average: 

    $$\tilde{\mu} = \frac{1}{N}\sum\limits_{k=1}^{N} x_k$$

2. Standard deviation: 

    $$\tilde{\sigma} = \sqrt{\frac{1}{N-1}\sum\limits_{k=1}^{N} (x_k - \tilde{\mu})^2 }$$  

3. Root-mean-square, r.m.s. : 

    $$x_{\mathrm{rms}} = \sqrt{\frac{1}{N}\sum\limits_{k=1}^{N} (x_k - \tilde{\mu})^2 }$$  



<!-- #endregion -->

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
mu = P.mean()
sigma = P.std(ddof=1) # note the definition, remember to check if the equations are right
rms = sqrt(mean((P-mu)**2))
print('average = %6.3f (kPa)' % mu)
print('standard deviation = %6.3f (kPa)' % sigma)
print('r.m.s.= %6.3f (kPa)' % rms)
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Prepare the histogram


Choice of the bin size has been repeated until 0.05 kPa was found to work well.
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
figure(figsize=(8,4))
# We prepare histogram with the $\Delta P = 0.05$ kPa
bins = arange(9.7,10.5,0.05)
n,bins,patches = hist(P,bins=bins)
# bin centers for the plot
x = bins[:-1]+0.5*diff(bins)[0]

# Let's see if it fits normal distribution
from scipy.stats import norm
# if you didn't estimate the mu, sigma above
param = norm.fit(P) # param[0] = sample mean, param[1] = sample std.
# pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])

pdf_fitted = norm.pdf(x,loc=mu,scale=sigma)

plot(x,pdf_fitted,'r-',lw=3)
xlabel(r'$P$ [kPa]')
ylabel('Frequency')
```

<!-- #region slideshow={"slide_type": "slide"} -->
## The normal, Gaussian distribution can be tested using higher order moments:

Skewness and kurtosis are like average (1st order) and standard deviation (2nd order), but for 3rd and 4th order statistics. 
One shows how symmetric the distribution is and another how flat (tall) it is. Gaussian distribution values are known, 
or can be quickly estimated taken some really random distribution. 
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}

import scipy.stats as st

print("skewness = %f, kurtosis = %f" % (st.skew(P), st.kurtosis(P)))
# let's compare it to the values of larger random values sample:
tmp = norm.rvs(loc=param[0],scale=param[1],size=100000)
print("Normal distribution skewness -> %f, kurtosis -> %f" % (st.skew(tmp), st.kurtosis(tmp)))
```

<!-- #region slideshow={"slide_type": "slide"} -->
## Estimate the $\chi^2$ and test the hypothesis

1. First for every column in the histogram, compare the value of the column with the fitted distribution
2. Then count the number of columns (left zeros or right zeros are not counted), in our case it is 13
<!-- #endregion -->

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
chi_sq = sum((n - pdf_fitted)**2/(pdf_fitted))
print('chi_square = %6.4f' % chi_sq)

# degrees of freedom = number of non-zero bins - 3, count 13, zero between two values count.
print(f"n = {n}")
print(f" dof = {13 - 3}")
dof = 10
```

```python slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
from scipy.stats import chi2

# one-sided Chi^2 test
pval = 1 - chi2.cdf(chi_sq, dof)
print("Confidence level is: %3.1f percent" % (pval*100))
```

```python jupyter={"outputs_hidden": false}
Image(filename = "img/xsquare.png", width=300)
```

```python jupyter={"outputs_hidden": true}

```
