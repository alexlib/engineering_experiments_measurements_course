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

```python jupyter={"outputs_hidden": false}
import numpy as np
import matplotlib.pylab as p
```

```python jupyter={"outputs_hidden": false}
# u = np.loadtxt('../../data/data_for_FFT.txt')
data = np.loadtxt('../../data/p40_20.ts')
# data source:
# http://ldvproc.nambis.de/data/ektdata.html 
```

```python jupyter={"outputs_hidden": false}
p.plot(data[:500,0],data[:500,1])
```

```python jupyter={"outputs_hidden": false}
p.hist(data[:,1],101,density=True);
```

```python jupyter={"outputs_hidden": false}
u = data[:,1]

meanu = u.mean()
uf = u - meanu
```

```python jupyter={"outputs_hidden": false}
p.plot(uf[:100])
```

```python jupyter={"outputs_hidden": false}
def powerspectrum(x):
    s = np.fft.fft(x)
    return np.real(s*np.conjugate(s))

```

```python jupyter={"outputs_hidden": false}
specu = powerspectrum(uf)
lenu, = specu.shape
```

```python jupyter={"outputs_hidden": false}
p.plot(specu[2:np.int(lenu/2)])
```

```python jupyter={"outputs_hidden": false}

```
