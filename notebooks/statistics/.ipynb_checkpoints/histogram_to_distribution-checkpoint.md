---
jupyter:
  jupytext:
    formats: ipynb,py,md
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

```python jupyter={"outputs_hidden": false}
%pylab inline
```

```python jupyter={"outputs_hidden": false}
x = random.normal(10.0, 3.0,size=200)
```

```python jupyter={"outputs_hidden": false}
plot(x)
xlabel('time',fontsize=16)
ylabel(r'$x$',fontsize=16)
```

```python jupyter={"outputs_hidden": false}
h = hist(x)
xlabel('bins of x')
ylabel('frequency of x')
```

```python jupyter={"outputs_hidden": false}
# make it yourself
pos = h[1][:-1]+diff(h[1])/2.
frequency = h[0]
bar(pos,frequency,width=1.4)
```

```python jupyter={"outputs_hidden": false}
# now we can normalize:
probability = frequency/sum(frequency)
bar(pos,probability,width=1.4)
xlabel('bins of x')
ylabel('probability')
```

```python jupyter={"outputs_hidden": false}
dx = diff(pos)[0]
print(('{:.2f}'.format(dx)))
```

```python jupyter={"outputs_hidden": false}
density = probability/dx
bar(pos,density,width=1.4)
xlabel('bins of x')
ylabel('probability density')
```

```python jupyter={"outputs_hidden": true}
z = (pos - x.mean())/x.std()
```

```python jupyter={"outputs_hidden": true}
# probability density function 
pdf = x.std() * density
```

```python jupyter={"outputs_hidden": false}
from scipy.stats import norm
y = mlab.normpdf( z, 0, 1)
bar(z,pdf,alpha=.3,width=.4),
zi = arange(-3,3,.1)
yi = mlab.normpdf( zi, 0, 1)
plot(zi, yi, 'k--', linewidth=2)
xlabel(r'$z$',fontsize=16)
ylabel(r'pdf', fontsize=16)
```

```python jupyter={"outputs_hidden": false}

```

```python jupyter={"outputs_hidden": true}

```
