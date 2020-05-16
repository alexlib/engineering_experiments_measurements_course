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

Define a function to load and execute another notebook in this notebook's namespace

```python
import io
from IPython.nbformat import read

def execute_notebook(nbfile):
    
    with io.open(nbfile) as f:
        nb = read(f,3)
    
    ip = get_ipython()
    
    for cell in nb.worksheets[0].cells:
        if cell.cell_type != 'code':
            continue
        ip.run_cell(cell.input)
```

Run our example [load data](loaddata.ipynb) notebook

```python
execute_notebook("loaddata.ipynb")
```

Now do our 'analysis' on that data

```python
%pylab inline
```

```python
plot(x,s,x,c)
```

```python

```

```python

```
