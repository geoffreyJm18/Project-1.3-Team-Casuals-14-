# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:55:59 2024

@author: geoff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# Het leest de opgenomen file 
samplerate, data = read('E1_100Hz1.wav')


tijd = np.arange(len(data)) / samplerate
data = data.astype(np.float64)

#Hier wordt het naar decibels omgerekend
decibel = 20 * np.log10(np.abs(data)) 

#Een plot maken met de gemeten data
plt.figure(figsize=(12, 6))
plt.plot(tijd, decibel)
plt.title('Decibel vs Tijd')
plt.xlabel('Tijd (s)')
plt.ylabel('Decibel (dB)')
plt.grid(True)
plt.show()

gemiddelde = np.median(decibel)

print(gemiddelde)


max_waarde = np.max(decibel)
print (max_waarde)