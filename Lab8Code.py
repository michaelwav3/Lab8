#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:26:22 2025

@author: michaelwav3
"""

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,101)
A = 10000
alpha = 0.001
B = 150000
beta = 0.5

#Note that the Ae and Be diverge, A and alpha takes over as -beta*t approaches 0 as 
#t approaches infinity, so A must be very small relative to B and alpha must be
#very small relative to beta for the best fit to the experimental data set


viral_load =  A*np.exp(alpha * time) + B*np.exp(-beta * time)

plt.figure()
plt.plot(time, viral_load, label="HIV Model")
plt.xlabel("Time (s)")
plt.ylabel("Viral Load")
plt.title("HIV Viral Load over Time")
plt.legend()
plt.show()

data = np.loadtxt('HIVSeries.csv', delimiter=',')
time_data = data[:, 0] #days
viral_data = data[:, 1] #viral load

plt.figure()
plt.plot(time_data, viral_data, 'r', label="Experimental Data")
plt.xlabel("Time (days)")
plt.ylabel("Viral Load")
plt.title("Experimental HIV Viral Load")
plt.legend()
plt.show()

viral_load2 =  A*np.exp(alpha * time_data) + B*np.exp(-beta * time_data)

plt.figure()
plt.plot(time_data, viral_data, 'r', label="Experimental Data")
plt.plot(time_data, viral_load2, 'b', label="Model Data")
plt.xlabel("Time (days)")
plt.ylabel("Viral Load")
plt.title("Experimental HIV Viral Load")
plt.legend()
plt.show()
