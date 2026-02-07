#!/usr/bin/env python3
"""
Created on Wed Feb  4 02:05:35 2026

@author: hgavr
"""

import numpy as np
int_list = list()
with open('problem_set_integers.txt', 'r') as f:
    for line in f:
        int_list.append(int(line.strip()))

print(f'Count is {len(int_list)}')
print(f'Sum is {np.sum(int_list)}')
print(f'Average is {np.mean(int_list)}')
print(f'Standard deviation is {np.std(int_list)}')  