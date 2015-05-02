from __future__ import division
import numpy as np
from numpy.random import randn
# create signal
def create_signal(fs,N):
	""" create signal with gaussian noise"""
	dt = 1/fs
	t = np.linspace(0,N*dt,N)
	# print t
	y = 1.0*np.sin(2*np.pi*10*t) + 1.5*np.sin(2*np.pi*35.7*t)
	# print y
	noise = randn(len(t)) - randn() # normal(0,1,N)
	# print noise
	sig = y + noise
	# print sig
	return t,sig

