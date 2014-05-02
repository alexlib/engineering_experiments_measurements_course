

import numpy as np
import matplotlib.pyplot as plt
fs = 200.0 #Hz
N = 256 # points
T = N/fs # 256/200Hz = 1.28s
t = np.arange(0.0,T,T/N)
y = 1.0*np.sin(2*np.pi*10*t) # 10 Hz pure sine wave of -1 to 1 Volt
plt.plot(t,y,'b-o')
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.axes().set_aspect(0.15)
plt.savefig('.')

df =1.0/T # 1/1.28s = 0.781 Hz
# create frequency axis
freq = np.arange(0.0,fs/2,df) 

# Apply FFT
sp = np.fft.fft(y)
# Use the result
# use modulus and the first half only
F = abs(sp[:freq.shape[0]])
# divide each amplitude by (N/2) so that corrected one corresponds to the 
# amplitude of the signal 
F = abs(F)/(N/2)
# also divide the first (f = 0Hz) by 2 to correspond properly to the DC offset
F[0] = F[0]/2.0

plt.figure()
plt.plot(freq, F) 
plt.axes().set_aspect('auto')
plt.savefig('.')


# Let us try to minimize the leakage problem
fs = 1000.0 #Hz
N = 256 # points
T = N/fs
t = np.arange(0.0,T,T/N)
y = 1.0*np.sin(2*np.pi*10*t) # 10 Hz pure sine wave of -1 to 1 Volt
plt.figure()
plt.plot(t,y,'b-o')
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.axes().set_aspect(0.05)
plt.savefig('.')

# now repeat the spectral analysis
df =1.0/T # 1/1.28s = 0.781 Hz
# create frequency axis
freq = np.arange(0.0,fs/2,df) 

# Apply FFT
sp = np.fft.fft(y)
# Use the result
# use modulus and the first half only
F = abs(sp[:freq.shape[0]])
# divide each amplitude by (N/2) so that corrected one corresponds to the 
# amplitude of the signal 
F = abs(F)/(N/2)
# also divide the first (f = 0Hz) by 2 to correspond properly to the DC offset
F[0] = F[0]/2.0

plt.figure()
plt.plot(freq, F) 
plt.axes().set_aspect('auto')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Spectrum amplitude [V]')
plt.savefig('.')

# Let us try to minimize the leakage problem sampling close to the Nyquist
fs = 25.0 #Hz
N = 256 # points
T = N/fs
t = np.arange(0.0,T,T/N)
y = 1.0*np.sin(2*np.pi*10*t) # 10 Hz pure sine wave of -1 to 1 Volt
plt.figure()
plt.plot(t,y,'b-o')
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.axes().set_aspect(1)
plt.savefig('.')

# now repeat the spectral analysis
df =1.0/T 
# create frequency axis
freq = np.arange(0.0,fs/2,df) 

# Apply FFT
sp = np.fft.fft(y)
# Use the result
# use modulus and the first half only
F = abs(sp[:freq.shape[0]])
# divide each amplitude by (N/2) so that corrected one corresponds to the 
# amplitude of the signal 
F = abs(F)/(N/2)
# also divide the first (f = 0Hz) by 2 to correspond properly to the DC offset
F[0] = F[0]/2.0

plt.figure()
plt.plot(freq, F) 
plt.axes().set_aspect('auto')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Spectrum amplitude [V]')
plt.savefig('.')

 # Let us try to minimize the leakage problem sampling close to the Nyquist
fs = 25.0 #Hz
N = 512 # points
T = N/fs
t = np.arange(0.0,T,T/N)
y = 1.0*np.sin(2*np.pi*10*t) # 10 Hz pure sine wave of -1 to 1 Volt
plt.figure()
plt.plot(t,y,'b-o')
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.savefig('.')

# now repeat the spectral analysis
df =1.0/T 
# create frequency axis
freq = np.arange(0.0,fs/2,df) 

# Apply FFT
sp = np.fft.fft(y)
# Use the result
# use modulus and the first half only
F = abs(sp[:freq.shape[0]])
# divide each amplitude by (N/2) so that corrected one corresponds to the 
# amplitude of the signal 
F = abs(F)/(N/2)
# also divide the first (f = 0Hz) by 2 to correspond properly to the DC offset
F[0] = F[0]/2.0

plt.figure()
plt.plot(freq, F) 
plt.axes().set_aspect('auto')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Spectrum amplitude [V]')
plt.savefig('.')

# Perfect FFT
# Let us try to minimize the leakage problem
fs = 25.6 #Hz
N = 256 # points
T = N/fs
t = np.arange(0.0,T,T/N)
y = 1.0*np.sin(2*np.pi*10*t) # 10 Hz pure sine wave of -1 to 1 Volt
plt.figure()
plt.plot(t,y,'b-o')
plt.xlabel('Time [sec]')
plt.ylabel('Voltage [V]')
plt.savefig('.')

# now repeat the spectral analysis
df =1.0/T 
# create frequency axis
freq = np.arange(0.0,fs/2,df) 

# Apply FFT
sp = np.fft.fft(y)
# Use the result
# use modulus and the first half only
F = abs(sp[:freq.shape[0]])
# divide each amplitude by (N/2) so that corrected one corresponds to the 
# amplitude of the signal 
F = abs(F)/(N/2)
# also divide the first (f = 0Hz) by 2 to correspond properly to the DC offset
F[0] = F[0]/2.0

plt.figure()
plt.plot(freq, F) 
plt.axes().set_aspect('auto')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Spectrum amplitude [V]')
plt.savefig('.')

plt.show()

