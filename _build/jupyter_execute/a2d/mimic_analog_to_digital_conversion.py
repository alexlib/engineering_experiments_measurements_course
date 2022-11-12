#!/usr/bin/env python
# coding: utf-8

# # Mimic A/D conversion

# In[1]:


# from https://dsp.stackexchange.com/questions/33596/analog-to-digital-conversion-using-python

import numpy as np
import matplotlib.pyplot as plt

time_of_view        = 1.; # s.
analog_time         = np.linspace (0, time_of_view, num=100); # s.

sampling_rate       = 21.; # Hz
sampling_period     = 1. / sampling_rate; # s
sample_number       = time_of_view / sampling_period;
sampling_time       = np.linspace (0, time_of_view, int(sample_number));

carrier_frequency   = 9.; # Hz
amplitude           = 1;  # V
phase               = 0;  # deg

quantizing_bits     = 4;
quantizing_levels   = 2 ** quantizing_bits / 2;
quantizing_step     = 1. / quantizing_levels;

def analog_signal (time_point):
    return amplitude * np.cos (2 * np.pi * carrier_frequency * time_point + phase);

sampling_signal     = analog_signal (sampling_time);
quantizing_signal   = np.round (sampling_signal / quantizing_step) * quantizing_step;



fig = plt.figure ()
# plt.plot (analog_time,   analog_signal (analog_time) );
#plt.stem (sampling_time, sampling_signal);
plt.stem (sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()


# In[ ]:





# In[2]:


fig = plt.figure()
plt.plot (analog_time, analog_signal (analog_time) );
#plt.stem (sampling_time, sampling_signal);
plt.stem(sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-');
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude");


# In[ ]:




