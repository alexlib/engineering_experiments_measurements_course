---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python jupyter={"outputs_hidden": false}
from sympy import *
init_printing(pretty_print=True,use_latex=True)
%matplotlib inline
import matplotlib.pyplot as plt
from numpy import arange
```

```python jupyter={"outputs_hidden": false}
f,t,T,G = symbols('f t T G')
```

```python jupyter={"outputs_hidden": false}
f = G*t
print ('f =', f)
```

```python jupyter={"outputs_hidden": false}
p = plot((f.subs(G,25),(t,0,1)),((f-25).subs(G,25),(t,1,2)),((f-50).subs(G,25),(t,2,3)), \
         ylabel = '$f = 25 t$ [V]', xlabel = '$t$ [sec]', xlim=(0,3), figsize=(10,8))
```

```python jupyter={"outputs_hidden": false}
c0 = integrate(f,(t,0,T))*(1/T)
print(c0) 
print (c0.subs([(G,25),(T,1)]))
```

```python jupyter={"outputs_hidden": false}
a1 = (2/T)*integrate(f*sin(2*pi*t),(t,0,T))
```

```python jupyter={"outputs_hidden": false}
print(a1)
print( a1.subs([(T,1),(pi, 3.14),(G,25)]))
```

```python jupyter={"outputs_hidden": false}
a,b = [],[]
for n in range(10):
    a.append((2/T)*integrate(f*sin(n*pi*t),(t,0,T)))
    b.append((2/T)*integrate(f*cos(n*pi*t),(t,0,T)))
```

```python jupyter={"outputs_hidden": false}
a[9], b[9]
```

```python jupyter={"outputs_hidden": false}

c = []
for n in range(1,10):
    print( a[n])
    expr = sqrt(a[n]**2 + b[n]**2)
    expr = expr.subs([(T,1),(pi, 3.14),(G,25)])
    # print expr
    # val = lambdify(t,expr,'numpy')
    c.append(expr)
```

```python jupyter={"outputs_hidden": false}
fig,ax = plt.subplots(figsize=(10,8))
ax.bar(-.5+arange(1,10),c,alpha=.5)
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_xlabel('$n$',fontsize=16)
ax.set_ylabel('Fourier coefficients $a_n^2 + b_n^2$',fontsize=16)
```

```python jupyter={"outputs_hidden": false}

```
