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

# %% jupyter={"outputs_hidden": false}
import numpy as np
import matplotlib.pylab as p

# %% jupyter={"outputs_hidden": false}
# u = np.loadtxt('../../data/data_for_FFT.txt')
data = np.loadtxt('../../data/p40_20.ts')
# data source:
# http://ldvproc.nambis.de/data/ektdata.html 

# %% jupyter={"outputs_hidden": false}
p.plot(data[:500,0],data[:500,1])

# %% jupyter={"outputs_hidden": false}
p.hist(data[:,1],101,density=True);

# %% jupyter={"outputs_hidden": false}
u = data[:,1]

meanu = u.mean()
uf = u - meanu

# %% jupyter={"outputs_hidden": false}
p.plot(uf[:100])


# %% jupyter={"outputs_hidden": false}
def powerspectrum(x):
    s = np.fft.fft(x)
    return np.real(s*np.conjugate(s))



# %% jupyter={"outputs_hidden": false}
specu = powerspectrum(uf)
lenu, = specu.shape

# %% jupyter={"outputs_hidden": false}
p.plot(specu[2:np.int(lenu/2)])

# %% jupyter={"outputs_hidden": false}
