# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:57:23 2024

@author: geoff
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dit zijn al de gemiddeldes van de samengevoegde nagalmtijden.
data = np.array([
    [0.3971686092392542, 0.6419409636561219, 0.4027361234888314, 0.5007612424692915, 0.5451746438950065],
    [0.23212603278584573, 0.4233045836045248,0.3644630767933242, 0.6864611028760655, 0.6584665337188298],
    [0.5204514686621076, 0.4050729591030504, 0.4078569115988901, 0.8308961228481072, 0.4560141240108515],
    [0.4017351243588176, 0.6805909790826762, 0.4208087346860772, 0.3028084738560013, 0.4587464239615436],
    [0.41957596914565487, 0, 0, 0, 0.7351609540236632]
])

#Assen benoemen
labels_x = ['A', 'B', 'C', 'D', 'E'] 
labels_y = ['1', '2', '3', '4', '5'] 

# Data verwerken
df = pd.DataFrame(data, columns=labels_x)


sns.heatmap(df, xticklabels=labels_x, yticklabels=labels_y)

# Plot van 2d heatmap latten zien.
plt.show()