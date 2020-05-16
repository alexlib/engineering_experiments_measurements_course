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
# Define a function to load and execute another notebook in this notebook's namespace

# %%
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


# %% [markdown]
# Run our example [load data](loaddata.ipynb) notebook

# %%
execute_notebook("loaddata.ipynb")

# %% [markdown]
# Now do our 'analysis' on that data

# %%
# %pylab inline

# %%
plot(x,s,x,c)

# %%

# %%
