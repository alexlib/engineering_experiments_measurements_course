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
% pylab inline
import StringIO
```

```python jupyter={"outputs_hidden": false}
# create two signals: concentration and temperature
c = StringIO.StringIO("""
1.095406121 3.887032952 6.956500526 9.486921797 \
13.96944459 14.86018043 23.19810833 24.53008787 \
24.72311112 37.44113657 38.05523491 54.1881169""")


T = StringIO.StringIO("""91.72763561 70.60278306 \
53.0039356 45.03419592 32.45847839 29.03763728 13.49252686 \
12.0641877 18.91647307 12.01351046 11.49379565 9.671537342 """)

c = loadtxt(c)
T = loadtxt(T)
```

```python jupyter={"outputs_hidden": false}
plot(c,T,'o')
```

```python jupyter={"outputs_hidden": false}
a = -np.log10(T)
plot(c,a,'o')
```

### see the linear part and the "saturated part", use only the linear one

```python jupyter={"outputs_hidden": false}
ind = c < 24
plot(c[ind],a[ind],':o')
```

```python jupyter={"outputs_hidden": false}
polyfit(c[ind],a[ind],1)
```

```python jupyter={"outputs_hidden": false}
plot(c,a,'o')
c1 = linspace(0,60,100)
a1 = 0.037*c1-2.0
plot(c1,a1,'--')
```

```python jupyter={"outputs_hidden": false}
plot(c,T,'o')
a1 = 0.037*c1-2.0
plot(c1,10**(-a1),'--')
```

```python jupyter={"outputs_hidden": false}
print c
print T
```

```python jupyter={"outputs_hidden": false}
plot(c,T,'bo',c[6:8],T[6:8],'rs')
```

```python jupyter={"outputs_hidden": false}
c2 = c.copy()
T2 = T.copy()
mask = ones(c2.shape[0],dtype=bool)
mask[[6,7]] = False
plot(c2[mask],T2[mask],'o')
```

```python jupyter={"outputs_hidden": false}
plot(c2[mask]-c2[0],T2[mask]-T2[0],'o')
```

```python jupyter={"outputs_hidden": true}
c3 = c2[mask] - c2[0]
T3 = T2[0] - T2[mask]
```

```python jupyter={"outputs_hidden": false}
c3
```

```python jupyter={"outputs_hidden": false}
loglog(c3,T3,'o')
```

```python jupyter={"outputs_hidden": false}

```

```python jupyter={"outputs_hidden": true}

```

```python jupyter={"outputs_hidden": true}

```
