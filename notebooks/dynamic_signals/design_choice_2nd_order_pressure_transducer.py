# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
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
# # Example of pre-measurement design
#
# ## Pressure transducer choice of parameters
#
# We require to choose a pressure transduced such that we could measure a signal up to 100 Hz with a dynamic 
# error of up to 5%. 
#
# The pressure transducers available in the lab is measured to have damping of $\zeta = 0.5$ and ringing frequency of 1200 Hz. 

# %% slideshow={"slide_type": "skip"} jupyter={"outputs_hidden": false}
# %pylab inline
from scipy import signal
import numpy as np

# %% slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
# Define transfer function
fd = 1200 # Hz
fn = fd/(np.sqrt(1-0.5**2))
wn = fn/(2*np.pi) # rad/s
z=0.5     # damping
k = 1 		# sensitivity


sys = signal.lti(k*wn**2,[1,2*z*wn, wn**2])

# step function output
t,y = sys.step(N=1000)

figure(figsize=(8,6))
plot(t,y)
title('Step response of a pressure transducer')
xlabel('$t$ [sec]')
ylabel('E [V]')


# %% slideshow={"slide_type": "skip"} jupyter={"outputs_hidden": false}
# note that sampling is sufficient, if not we need to apply the D/A reconstruction
# or interpolations, which will add more noise and uncertainty to the system identification

# %% slideshow={"slide_type": "slide"} jupyter={"outputs_hidden": false}
# Create Bode plot
w, mag, phase = signal.bode(sys)

fig,ax = subplots(2,1,figsize=(8,10))
ax[0].semilogx(w/wn, mag)    # Bode magnitude plot
# ax[0].plot(w/wn,mag)
ax[0].set_ylabel('Magnitude (dB)',fontsize=16)
ax[1].semilogx(w/wn, phase)  # Bode phase plot
# ax[1].plot(w/wn, phase)  # Bode phase plot
ax[1].set_ylabel('Phase (deg)',fontsize=16)
ax[1].set_xlabel('$\omega/\omega_n$',fontsize=16)
# fig.savefig('bode_pressure_transducer.png',dpi=200)

# %%
