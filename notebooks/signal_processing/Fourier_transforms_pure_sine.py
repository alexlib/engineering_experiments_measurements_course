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
# # Fourier transforms 
#
# ## From very naive approximations of the spectrum to more complex examples:
#

# %% jupyter={"outputs_hidden": false}
from scipy import fft
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

# %% [markdown]
# ## Two basic ploting functions that repeat the actuall spectral analysis:

# %% jupyter={"outputs_hidden": false}
import sys
sys.path.append('../../scripts')
from signal_processing import *

# %% [markdown]
# ## More elaborate example, demonstration of a leakage effect:

# %% jupyter={"outputs_hidden": false}
# We sample a signal at fs = 200 Hz and record 256 points"

# true values
A = 1.0 # Volt, amplitude
ff = 10.0 # Hz, signal frequency, zero harmonics


# We will work with different sampling frequencies
# and different lengths of records:

fs = 200.0 #Hz
N = 256 # points

plotSignal(A,ff,fs,N)

# %% [markdown]
# ### Note:
# 1. leakage at around 10 Hz
# 2. peak is below 1 Volt
# 3. we can get the spectrum up to half of sampling frequency
# 4. frequency resolution is $\Delta f = 1/T = 0.781$ Hz
#
# ### Let us try to minimize the leakage:
# #### Let's first increase the sampling rate, stay with N = 256

# %% jupyter={"outputs_hidden": false}
fs = 1000.0 #Hz
N = 256 # points
plotSignal(A,ff,fs,N)

# %% [markdown]
# ### Note:
# 1. resolution in time is great BUT:
# 1. resolution in frequency is worse, $\Delta f = 1/T = 1/0.25 = 3.91$ Hz
# 2. we see up to 500 Hz, but have here only 128 useful points
# 3. leakage is severe, the peak amplitude is about 0.66 Volt
# 4. peak location is now 11.7 Hz
#
#
# <span style="color:red"> **MORE IS NOT NECESSARILY BETTER** </span>
#
# ###Let us try to minimize the leakage problem sampling closer to the Nyquist frequency

# %% jupyter={"outputs_hidden": false}
fs = 25.0 #Hz
N = 256 # points
plotSignal(A,ff,fs,N)

# %% [markdown]
# ### Note:
# 1. sine does not seem to be a sine wave, time resolution is bad for Nyquist frequency
# 2. frequency resolution is better, about 0.1 Hz
# 3. peak is about 0.75 Volt, less leakage but still strong
# 4. peak location is close, 9.96 Hz
#
# ### Let's get more points, keep same sampling frequency

# %% jupyter={"outputs_hidden": false}
fs = 25.0 #Hz
N = 512 # points
plotSignal(A,ff,fs,N)

# %% [markdown]
# ### Note: 
# 1. time sampling is much longer, $T = N/f_s = 512/(25 Hz) = 20.48$ s
# 2. peak is narrow, at 10.01 Hz
# 3. resolution is good, much lower leakage, value is close to 0.9 Volt
#
# ### Still, how to get the *perfect* spectrum? Use tricks, for instance, sample at a specific frequency: 

# %% jupyter={"outputs_hidden": false}
fs = 25.6 #Hz
N = 256 # points
plotSignal(A,ff,fs,N)

# %% jupyter={"outputs_hidden": false}
# After you know the real value, you can save a lot of time:
fs = 25.6 #Hz
N = 64 # points
plotSignal(A,ff,fs,N)
