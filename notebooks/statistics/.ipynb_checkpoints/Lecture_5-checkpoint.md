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

<!-- #region cell_id="503f3c89-bab9-4dae-8e5e-13edfacdbdf7" tags=[] -->
## Lecture 5 - probability and statistics

In this notebook we will collect all the examples from Lecture 5 ``Probability and statistics''
<!-- #endregion -->

<!-- #region cell_id="7d4008bf-991b-4402-be9f-b8aa404aabd3" -->
## Histogram
<!-- #endregion -->

```python cell_id="647465f2-af83-49a9-93b7-162af714cb35" jupyter={"outputs_hidden": false}
import numpy as np                   # numerical stuff
from matplotlib import pyplot as plt # plotting functions
plt.style.use('fivethirtyeight')

%matplotlib inline
```

```python cell_id="dffa2fcc-1e14-4b4a-9a85-7f2c78779783" jupyter={"outputs_hidden": false}
# let's create some data
x = np.array([12.1,12.3,12.2,12.2,12.4,12.3,12.2,12.4,12.2,12.5])
```

```python cell_id="dffa2fcc-1e14-4b4a-9a85-7f2c78779783" jupyter={"outputs_hidden": false}
# create histogram using matplotlib and store the histogram output
x_modes = plt.hist(x) #note that we did not specify number of bins
```

```python cell_id="90e59b5f-b6b9-4728-9bff-f263a8ba1dd4" jupyter={"outputs_hidden": false}
# the output in x_modes

# which bin has most samples? 
x_mode_ind = np.argmax(x_modes[0])

# how many counts in the top column? 
x_mode_count = x_modes[0][x_mode_ind]

# what is the value of most frequent sample: 
x_mode_val = x[x_mode_ind]


print(f"Data: {x}")
print(f"Mean: {np.mean(x):.2f}, Median: {np.median(x):.2f} STD: {np.std(x):.2f}")
print(f"Mode: {x_mode_val} appears {x_mode_count} times" )
```

<!-- #region cell_id="4c263150-206a-4304-8104-7c4ff33414a8" -->
## Let's create our own histogram 
<!-- #endregion -->

```python cell_id="b02c5113-6020-4341-bb36-39558e9f0bcf" jupyter={"outputs_hidden": false}
nbins = 7 # better then the default choice 


hist_vals = np.zeros(nbins)
min_val = x.min() - 0.05
max_val = x.max() + 0.05
for d in x: # for every item
    # find which bin it belongs 
    bin_number = int(nbins * ((d - min_val) / (max_val - min_val)))
    
    # add a counter
    hist_vals[bin_number] += 1
```

```python cell_id="b02c5113-6020-4341-bb36-39558e9f0bcf" jupyter={"outputs_hidden": false}
# let's plot some columns
plt.bar(np.linspace(min_val,max_val,nbins),hist_vals,width = 0.05)
plt.xlim([min_val-.1,max_val+.1]);
```

<!-- #region cell_id="1cc37d28-bc22-4483-a97e-10848cbcdd0e" tags=[] -->
##### From sample to population statistics 
or from a histogram to the probability density function

1. [More histogram examples](histogram_example.ipynb)

1. [Histograms, chi^2 test](histogram_example.ipynb)
1. [chi^2 test of normal distribution using SciPy stats](chi_square_test_example.ipynb)
1. [Central limit theorem illustration](Central_limit_theorem_illustration.ipynb)
1. [Probability Distributions and the Central Limit Theorem](distributions.ipynb)

1. [Student t-distribution](t-distribution.ipynb)

#### Next lecture 
1. [Outliers analysis](outliers_example.ipynb)
1. [Outliers of pairs (x,y) analyis](outliers_example_pairs.ipynb)
1. [Various random variables, log-normal, log-log-normal](various_random_variables.ipynb)
<!-- #endregion -->

```python cell_id="71df2001-06c6-485b-bfa2-5e5effbb5de0" tags=[]
#
```
