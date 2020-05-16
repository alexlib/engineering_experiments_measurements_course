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

```python
# from https://dsp.stackexchange.com/questions/33596/analog-to-digital-conversion-using-python

import numpy as np
import matplotlib.pyplot as plt

time_of_view        = 1.; # s.
analog_time         = np.linspace (0, time_of_view, num=100); # s.

sampling_rate       = 20.; # Hz
sampling_period     = 1. / sampling_rate; # s
sample_number       = time_of_view / sampling_period;
sampling_time       = np.linspace (0, time_of_view, int(sample_number));

carrier_frequency   = 9.;
amplitude           = 1;
phase               = 0;

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
plt.stem (sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-',use_line_collection=True);
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
```

```python
fig = plt.figure ()
plt.plot (analog_time,   analog_signal (analog_time) );
#plt.stem (sampling_time, sampling_signal);
plt.stem (sampling_time, quantizing_signal, linefmt='r-', markerfmt='rs', basefmt='r-',use_line_collection=True);
plt.title("Analog to digital signal conversion")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
```

```python
quantizing_signal
```

```python

```
