# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 2
#     language: python
#     name: python2
# ---

# # Engineering Experiments and Instrumentation
#
# This repository holds some Jupyter/IPython notebooks which are part of the course material for the exercises accompanying the lecture "Engineering Experiments and Instrumentation" at [School of Mechanical Engineering](http://engineering.tau.ac.il/School-of-Mechanical-Engineering), [Tel Aviv University](http://www.tau.ac.il).

# The exercises are split into the following units.
# Most of them build upon knowledge from previous units, so you should do them in order:
#
# ### Introduction and theory
# 1. [Generalized measurement system](general_measurement_system_analysis.ipynb)
# 1. [Basic error analysis](basic_error_analysis.ipynb)
#
# ### Calibration (typical errors, regression)
# 1. [Regression analysis - explanation](introduction_linear_regression.ipynb)
# 1. [Calibration of non-linear relations](calibration_non_linear_relations.ipynb)
# 1. [Hysteresis error analysis](hysteresis_error_analysis.ipynb)
# 1. [Sensitivity coefficient](sensitivity_analysis.ipynb)
# 1. [Hysteresis and regression for calibration](calibration_error_analysis_pressure.ipynb)
# 1. [Linearity error analysis - calibration](Lineariy_error_example.ipynb)
# <!--- 1. [LVDT calibration](lvdt_calibration.ipynb) --->
# 1. [Calibration and uncertainty analysis - virtual experiment](full_calibration_analysis_example_2.ipynb)
# 1. [Pressure transducer calibration example](pressure_calibration_example.ipynb)
#
#
# ### Statistics (histograms, statistical tests, outliers)
#
# 1. [Basic Statistics](basic_statistics.ipynb)
# 1. [Central limit theorem illustration](Central_limit_theorem_illustration.ipynb)
# 1. [Testing for normal distribution, chi^2](chi_square_test_example.ipynb)
# 1. [Probability Distributions and the Central Limit Theorem](distributions.ipynb)
# 1. [Histogram analysis example](histogram_example.ipynb)
# 1. [Histograms](histograms.ipynb)
# 1. [Student t-distribution](t-distribution.ipynb)
# 1. [Outliers analysis](outliers_example.ipynb)
# 1. [Outliers of pairs (x,y) analyis](outliers_example_pairs.ipynb)
# 1. [Various random variables, log-normal, log-log-normal](various_random_variables.ipynb)
#
# ### Dynamical systems (1st order, 2nd order)
# 1. [First order dynamical system responses](first_order_time_response.ipynb)
# 1. [Step response](step_response.ipynb)
# 1. [Estimate parameters 2nd order system](2nd_order_system_step_function_log_decrement.ipynb)
#
#
# ### Fourier analysis, frequency content, spectrum
#
# 1. [Analytical approach to Fourier coefficients of a periodic ramp function](Fourier_coefficients_analytical_evaluation_periodic_ramp_function.ipynb)
# 1. [Fourier transform of a pure sine wave](Fourier_transforms_pure_sine.ipynb)
# 1. [Frequency content (spectrum) of a periodic signal](Frequency_content_of_a_periodic_signal.ipynb)
# 1. [Using FFT to filter noise](FFT_based_filtering.ipynb)
#
#
#
#
# ### Sampling, aliasing, A/D, D/A conversion
# 1. [Digital to Analog D/A reconstruction](Reconstruction_periodic_signal_Cardinal_series.ipynb)
# 1. [Sampling, aliasing, clipping](sampling_aliasing_examples.ipynb)
#
#
# ### Various measurement concepts
# 1. [Doppler effect demonstration](doppler.ipynb)
# 1. [Particle Image Velocimetry](piv.ipynb)
#

# ## Getting Started
#
# The Jupyter/IPython notebooks for each topic are available as [static web pages](http://nbviewer.ipython.org/github/alexlib/engineering_experiments_measurements_course/) as well as for interactive use with [Jupyter](http://jupyter.org/) (formerly known as [IPython](http://ipython.org/)), to be [downloaded from Github](http://github.com/alexlib/engineering_experiments_measurements_course).
#
# Use [Git](http://git-scm.org/) to download the files (or download the [zip file](https://github.com/spatialaudio/communication-acoustics-exercises/archive/master.zip)), use the Python package management system [pip](http://www.pip-installer.org/) to install a few Python libraries that we will use and then start the IPython notebook:
#
#     git clone https://github.com/alexlib/engineering_experiments_measurements_course.git 
#     cd engineering_experiments_measurements_course
#     ipython notebook
#     
# This will open a new view in your web browser with a list of notebooks.
# Click on [intro.ipynb](intro.ipynb) (or any of the other available notebooks) and enjoy!
# If you are new to Git, have a look at this [introduction to Git](http://mg.rtfd.org/git.html).
#
# Alternatively, you can also download individual notebook files (with the extension `.ipynb`) and open them in IPython.
# Note that some exercises make use of additional files (audio files etc.) which you'll then also have to download manually.
#
# We use so far Python 2, we will move to Python 3 soon. 
#
# If you don't have Python installed already, you should download and install a Python distribution which already includes all the libraries we'll need, e.g. [Anaconda](https://www.continuum.io/downloads)

# ## Interactive Online Version
#
# If you don't feel like installing Jupyter/IPython, but still want to try out the notebooks, you can [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/alexlib/engineering_experiments_measurements_course) and start playing around immediately.
#
# Note, however, that your changes will not be preserved.
# Once you close your browser, everything will be lost! But you can download the notebook for later reuse.

# ## External Links
#
# This file is created following a very nice IPython notebook course on http://nbviewer.ipython.org/github/spatialaudio/communication-acoustics-exercises/
#
# to which we are thankful. 

# ## Copyright Information
#
# <p xmlns:dct="http://purl.org/dc/terms/">
#   <a rel="license"
#      href="http://creativecommons.org/publicdomain/zero/1.0/">
#     <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
#   </a>
#   <br />
#   To the extent possible under law,
#   <span rel="dct:publisher" resource="[_:publisher]">the person who associated CC0</span>
#   with this work has waived all copyright and related or neighboring
#   rights to this work.
# </p>
