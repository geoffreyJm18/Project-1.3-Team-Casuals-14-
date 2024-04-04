# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:20:59 2024

@author: geoff
"""

import numpy as np
import scipy.interpolate as formula
from scipy.io.wavfile import read
import glob
import csv

#Deze file berekent de nagalmtijden 
directory = './' 

with open("nagalmtijden.py", "w", newline='') as output_file:
    writer = csv.writer(output_file)
    all_files = glob.glob(directory + '*.wav')
    for file in all_files:
        print(f'Processing file {file}')
        samplerate, data = read(file)
        tijd = np.arange(len(data)) / samplerate
        data = data.astype(np.float64)
        decibels = 20 * np.log10(np.abs(data))
        max_value = np.max(decibels)
        db_drop = max_value - 30
        x = decibels
        y = tijd
        interp_func = formula.interpolate.interp1d(x, y)
        x_interpolated2 = interp_func(db_drop)
        x_interpolated = interp_func(max_value)
        echo_time = (x_interpolated2 - x_interpolated) * 2
        writer.writerow([abs(echo_time)])

print('Done')