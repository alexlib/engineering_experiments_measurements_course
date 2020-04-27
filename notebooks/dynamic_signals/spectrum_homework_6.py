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
import matplotlib.pyplot as pl
# %matplotlib inline
from matplotlib import rcParams
rcParams.update({'figure.figsize': (10, 8)})
rcParams.update({'font.size': 14})


# %% jupyter={"outputs_hidden": false}
fs = 100 # Hz
y = np.loadtxt('../../data/FFT_Example_data_with_window.txt')
t = np.linspace(0,len(y)/fs,len(y))

# %% jupyter={"outputs_hidden": false}
pl.plot(t,y)
pl.xlabel('$t$ [sec]',fontsize=16)
pl.ylabel('$y$ [V]',fontsize=16)

# %% jupyter={"outputs_hidden": false}
# subtract the DC:
yf = y - np.mean(y)

# %% jupyter={"outputs_hidden": false}
pl.plot(t,yf)
pl.xlabel('$t$ [sec]',fontsize=16)
pl.ylabel('$y - DC(y) $ [V]',fontsize=16)


# %% jupyter={"outputs_hidden": false}
def spectrum(y,Fs):
    """
    Plots a Single-Sided Amplitude Spectrum of a sampled
    signal y(t), sampling frequency Fs (lenght of a signal 
    provides the number of samples recorded)
    
    Following: http://goo.gl/wRoUn
    """
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(np.int(n/2))] # one side frequency range
    Y = 2*np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(np.int(n/2))]
    return frq, Y

def plotSignal(t,y,frq,Y):
    """ plots the time signal Y(t) and the 
    frequency spectrum Y(fs)
    Inputs:
        t - time 
        y - signal
    Outputs:
        t - time signal, [sec]
        Y - values, [Volt]
    Usage:
        plotSignal(t,y,fs)
    """

    # Plot
    pl.figure()
    pl.subplot(2,1,1)
    pl.plot(t,y,'b-')
    pl.xlabel('$t$ [s]',fontsize=16)
    pl.ylabel('$Y$ [V]',fontsize=16)
    # axes().set_aspect(0.2)
    # title('sampled signal')
    pl.subplot(2,1,2)
    pl.plot(frq,abs(Y),'r') # plotting the spectrum
    pl.xlabel('$f$ (Hz)',fontsize=16)
    pl.ylabel('$|Y(f)|$',fontsize=16)


# %% jupyter={"outputs_hidden": false}
frq,Y = spectrum(yf,fs) 
plotSignal(t,yf,frq,Y)

# %% jupyter={"outputs_hidden": false}

# %% jupyter={"outputs_hidden": false}
