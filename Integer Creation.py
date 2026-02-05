# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 01:25:34 2026

@author: hgavr
"""

import random

file = 'problem_set_integers.txt'

with open(file, 'w') as f:
    for _ in range(1000):
        num = random.randint(0, 1000000)
        f.write(f"{num}\n")
print("File created")

    