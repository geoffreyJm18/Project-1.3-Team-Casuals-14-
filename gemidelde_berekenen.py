# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:38:34 2024

@author: geoff
"""

import statistics

# Het open de output van de Samenvoegen_van_files en bereken de gemiddeldes ervaan
with open("data_42.py") as f:
    lines = f.readlines()
    numbers = [float(x.strip()) for x in lines]

   
    average = sum(numbers) / len(numbers)
    pop_std_dev = statistics.pstdev(numbers)

    with open("E5_440_gem_std.py", "w") as outfile:
        print(average, file=outfile)
        print(pop_std_dev, file=outfile)