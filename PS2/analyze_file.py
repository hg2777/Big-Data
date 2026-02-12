#!/apps/anaconda3/bin/python

import numpy as np
import sys

file_id = sys.argv[1]

input_file = f"input_{file_id}.txt"
output_file = f"output_{file_id}.txt"

data = np.loadtxt(input_file)

count = len(data)
sum_val = np.sum(data)
mean = np.mean(data)
std = np.std(data)

with open(output_file, "w") as f:
    f.write(f"count {count}\n")
    f.write(f"sum {sum_val}\n")
    f.write(f"mean {mean}\n")
    f.write(f"stdev {std}\n")

print(f"Processed {input_file}")
