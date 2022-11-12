#!/usr/bin/env python
# coding: utf-8

# # Homework no. 1

# ## Question 1
# 
# In our laboratory you will not use the **distance** measurements. There is a tool for this, called **linear variable differential transformer (LVDT)**. 
# 
# 1. Read and summarize the principle of action of LVDT
# 2. An engineer wants to calibrate the LVDT tool, using micrometer. The system looks like this:

# In[1]:


from IPython.display import Image
Image('../img/lvdt.png',width=600)


# Please, describe the system according to the general system scheme: 
# - what is the sensor in Figure 1.12? 
# - what is the signal of the sensor output ?
# - what is the transducer? 
# - what is the signal after transducer? 
# - what kind of signal conditioning the LVDT does?
# - what kind of output there is after the system? 
# - is there a feedback? 

# In[2]:


Image('../img/generalized_measurement_system.png',width=600)


# ## Question 2
# 
# **Calibration and regression**
# 
# Each group runs the notebook to get their own original set of data in terms of two arrays (at least 5-6 samples long): concentration $c$ (in particles per million, ppm) versus transmissivity $T$ (in percents, 100% is completely transparent, i.e. clear water): [LINK](http://mybinder.org/repo/alexlib/engineering_experiments_measurements_course/random_data_for_hw_1.ipynb) (** use Cell -> Run All **) 
# 
# 1. This is a calibration data, the process temperature depends on the concentration. Plot the data $c = f(T)$
# 1. Find the sensitivity, the input range, the output range (full scale output) and the relevant errors. 
# 1. Find out what would be the concentration if in the experiment we measure $T = 35.6\%$

# In[ ]:




