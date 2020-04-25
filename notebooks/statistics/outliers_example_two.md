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

# Outliers

```python jupyter={"outputs_hidden": false}
import numpy as np
import matplotlib.pyplot as pl
%matplotlib inline

import matplotlib as mpl
mpl.rcParams['lines.linewidth']=2
mpl.rcParams['lines.color']='r'
mpl.rcParams['figure.figsize']=(10,8)
mpl.rcParams['font.size']=14
mpl.rcParams['axes.labelsize']=20
```

## Single variable, $x$

```python jupyter={"outputs_hidden": false}
x = np.array([49.3,50.2,49.2,49.8,50.5,49.3,48.9,49.9,50.1,49.2])
```

```python jupyter={"outputs_hidden": false}
pl.figure()
pl.plot(x,'o')
pl.xlim([-1,8])
pl.ylim([48,52])
pl.ylabel('$x$')
pl.xlabel('$n$')
```

## We use modified Thompson test (based on Student's t-distribution)


### Sort the values

```python
x.sort()
```

```python jupyter={"outputs_hidden": false}
x
```

```python jupyter={"outputs_hidden": false}
pl.plot(x,'o')
pl.xlim([-1,8])
pl.ylim([48,52])
pl.ylabel('$x$')
pl.xlabel('$n$')
```

Note: we suspect in the sorted list of values the first and the last


### get the sample mean and sample standard deviation, get deviations

```python jupyter={"outputs_hidden": false}
x_mean = np.mean(x)
x_std = np.std(x,ddof=1)
print( x_mean)
print (x_std)
```

$\delta_i = | x - x_i |$

```python jupyter={"outputs_hidden": false}
delta = abs(x - x_mean)
pl.plot(delta,'o')
pl.xlim([-1,8])
pl.ylim([-.5,1])
pl.ylabel('$\delta$')
pl.xlabel('$n$')
print (delta[0],delta[-1])
```

```python jupyter={"outputs_hidden": true}

```
