import numpy as np

# create signal
def create_signal(fs,N):
	""" create signal with gaussian noise"""
	dt = 1./fs
	t = np.linspace(0,N*dt,N)
	y = 1.0*np.sin(2*np.pi*10*t) + 1.5*np.sin(2*np.pi*35.7*t)
	noise = np.random.normal(0,1,N)
	y += noise
	return t, y

