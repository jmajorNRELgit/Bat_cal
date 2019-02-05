# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 07:49:51 2019

@author: jmajor
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = np.abs(a.mean(axis))
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

file =  'C:/Users/jmajor/Desktop/github/Bat_cal/TIM data/TIM_stand_Overnight_1.csv'

df = pd.read_csv(file)

data_range_high = None
range_low = None

times = df['Time'][range_low:data_range_high]
volts = df['Voltage'][range_low:data_range_high]
currents = df['Current'][range_low:data_range_high]
base = df['Ground'][range_low:data_range_high]

print('TEG std: ' + str(np.std(volts[:])))
print('Ground std: ' + str(np.std(base)))
print('Current std: ' + str(np.std(currents)))
print('\n\n')
print('Voltage SNR: ' + str(signaltonoise(volts)))
print('Ground SNR: ' + str(signaltonoise(base)))
print('Current SNR: ' + str(signaltonoise(currents)))
print('\n\n')

#graphs the data
plt.plot(times,volts, 'ro')
plt.plot(times,volts, 'b-')
plt.plot(times, currents, 'o')
plt.plot(times, currents, 'y-')
plt.plot(times, base, 'ro')
plt.plot(times, base, 'g-')
plt.show()

