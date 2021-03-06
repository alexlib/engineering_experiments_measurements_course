[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/alexlib/engineering_experiments_measurements_course) 

## Engineering Experiments and Instrumentation
Python snippets used in Lectures and laboratory experiments. 

You can run and test all the notebooks using the great MyBinder service. Press the button:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/alexlib/engineering_experiments_measurements_course/master)



This repository holds some Jupyter/IPython notebooks which are part of the course material for the exercises accompanying the lecture "Engineering Experiments and Instrumentation" at [School of Mechanical Engineering](http://engineering.tau.ac.il/School-of-Mechanical-Engineering), [Tel Aviv University](http://www.tau.ac.il).

The exercises are split into the following units.
Most of them build upon knowledge from previous units, so you should do them in order:

### Introduction and theory
1. [Generalized measurement system](general_measurement_system_analysis.ipynb)
1. [Basic error analysis](basic_error_analysis.ipynb)

### Calibration (typical errors, regression)
1. [Regression analysis](notebooks/calibration/regression_analysis.ipynb)
1. [Regression analysis - detailed explanation](notebooks/calibration/introduction_linear_regression.ipynb)
1. [Calibration of non-linear relations](notebooks/calibration/calibration_non_linear_relations.ipynb)
1. [Hysteresis error analysis](notebooks/calibration/hysteresis_error_analysis.ipynb)
1. [Sensitivity coefficient](notebooks/calibration/sensitivity_analysis.ipynb)
1. [Hysteresis and regression for calibration](notebooks/calibration/calibration_error_analysis_pressure.ipynb)
1. [Linearity error analysis - calibration](notebooks/calibration/Lineariy_error_example.ipynb)
<!--- 1. [LVDT calibration](lvdt_calibration.ipynb) --->
1. [Calibration and uncertainty analysis - virtual experiment](notebooks/calibration/full_calibration_analysis_example_2.ipynb)
1. [Pressure transducer calibration example](notebooks/calibration/pressure_calibration_example.ipynb)


### Statistics (histograms, statistical tests, outliers)
1. [Statistics](notebooks/statistics/Lecture_5.ipynb)
1. [Outliers analysis](notebooks/statistics/outliers_example.ipynb)
1. [Outliers of pairs (x,y) analyis](notebooks/statistics/outliers_example_pairs.ipynb)
1. [Various random variables, log-normal, log-log-normal](notebooks/statistics/various_random_variables.ipynb)

### Dynamical systems (1st order, 2nd order)
1. [First order dynamical system responses](first_order_time_response.ipynb)
1. [Step response](step_response.ipynb)
1. [Estimate parameters 2nd order system](2nd_order_system_step_function_log_decrement.ipynb)


### Fourier analysis, frequency content, spectrum

1. [Analytical approach to Fourier coefficients of a periodic ramp function](Fourier_coefficients_analytical_evaluation_periodic_ramp_function.ipynb)
1. [Fourier transform of a pure sine wave](Fourier_transforms_pure_sine.ipynb)
1. [Frequency content (spectrum) of a periodic signal](Frequency_content_of_a_periodic_signal.ipynb)
1. [Using FFT to filter noise](FFT_based_filtering.ipynb)




### Sampling, aliasing, A/D, D/A conversion
1. [Digital to Analog D/A reconstruction](Reconstruction_periodic_signal_Cardinal_series.ipynb)
1. [Sampling, aliasing, clipping](sampling_aliasing_examples.ipynb)


### Various measurement concepts
1. [Doppler effect demonstration](doppler.ipynb)
1. [Particle Image Velocimetry](piv.ipynb)



## Copyright Information

<p xmlns:dct="http://purl.org/dc/terms/">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <span rel="dct:publisher" resource="[_:publisher]">the person who associated CC0</span>
  with this work has waived all copyright and related or neighboring
  rights to this work.
</p>
