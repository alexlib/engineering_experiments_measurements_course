## Engineering Experiments and Instrumentation
Python snippets used in Lectures and laboratory experiments

Click the [index.ipynb](https://github.com/alexlib/engineering_experiments_measurements_course/blob/master/index.ipynb) file to see its rendered by Github and IPython notebook viewer or if you want to **play** with the interactive notebooks, use Binder applicaiton:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/alexlib/engineering_experiments_measurements_course/master?filepath=index.ipynb)



This repository holds some Jupyter/IPython notebooks which are part of the course material for the exercises accompanying the lecture "Engineering Experiments and Instrumentation" at [School of Mechanical Engineering](http://engineering.tau.ac.il/School-of-Mechanical-Engineering), [Tel Aviv University](http://www.tau.ac.il).

The exercises are split into the following units.
Most of them build upon knowledge from previous units, so you should do them in order:

### Introduction and theory
1. [Generalized measurement system](general_measurement_system_analysis.ipynb)
1. [Basic error analysis](basic_error_analysis.ipynb)

### Calibration (typical errors, regression)
1. [Regression analysis - explanation](introduction_linear_regression.ipynb)
1. [Calibration of non-linear relations](calibration_non_linear_relations.ipynb)
1. [Hysteresis error analysis](hysteresis_error_analysis.ipynb)
1. [Sensitivity coefficient](sensitivity_analysis.ipynb)
1. [Hysteresis and regression for calibration](calibration_error_analysis_pressure.ipynb)
1. [Linearity error analysis - calibration](Lineariy_error_example.ipynb)
<!--- 1. [LVDT calibration](lvdt_calibration.ipynb) --->
1. [Calibration and uncertainty analysis - virtual experiment](full_calibration_analysis_example_2.ipynb)
1. [Pressure transducer calibration example](pressure_calibration_example.ipynb)


### Statistics (histograms, statistical tests, outliers)

1. [Statistics](notebooks/statistics/Lecture_5.ipynb)

1. [Outliers analysis](outliers_example.ipynb)
1. [Outliers of pairs (x,y) analyis](outliers_example_pairs.ipynb)
1. [Various random variables, log-normal, log-log-normal](various_random_variables.ipynb)

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
