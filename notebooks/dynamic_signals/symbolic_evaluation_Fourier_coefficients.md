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
from sympy import *
init_printing(pretty_print=True,use_latex=True)
%matplotlib inline
import matplotlib.pyplot as plt
```

```python jupyter={"outputs_hidden": false}
f,t,T,G = symbols('f t T G')
```

```python jupyter={"outputs_hidden": false}
f = G*t
print('f = ', f)
```

```python jupyter={"outputs_hidden": false}
plot((f.subs(G,25),(t,0,1)),((f-25).subs(G,25),(t,1,2)),((f-50).subs(G,25),(t,2,3)), ylabel='f = 25 t [V]',xlabel='t [sec]',xlim = (0,3))
```

```python jupyter={"outputs_hidden": false}
c0 = integrate(f,(t,0,T))*(1/T)
print(c0) 
print(c0.subs([(G,25),(T,1)]))
```

```python jupyter={"outputs_hidden": false}
a1 = (2/T)*integrate(f*sin(2*pi*t),(t,0,T))
```

```python jupyter={"outputs_hidden": false}
print(a1)
print(a1.subs([(T,1),(pi, 3.14),(G,25)]))
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
    print(a[n])
    expr = (a[n]**2 + b[n]**2)
    expr = expr.subs([(T,1),(pi, 3.14),(G,25)])
    # print expr
    # val = lambdify(t,expr,'numpy')
    c.append(expr)
```

```python jupyter={"outputs_hidden": false}
plt.figure()
plt.bar(range(1,10),c)
plt.xlabel('n')
plt.ylabel('Fourier coefficients $a_n^2 + b_n^2$')
```

```python jupyter={"outputs_hidden": false}

```
