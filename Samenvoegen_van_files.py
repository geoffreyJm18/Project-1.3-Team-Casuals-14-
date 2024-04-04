# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:41:58 2024

@author: geoff
"""
# De file van de nagalmtijden openen
with open("nagalmtijden.py", "r") as f:
    lines = f.readlines()

for i in range(0, len(lines), 3):
    chunk = lines[i:i+3]
    
    # Voegt elke 3 lijnen van nagalmtijden.py samen
    with open(f"data_{i//3}.py", "w") as f_out:
        for line in chunk:
            f_out.write(line)
            

print("Done!")
