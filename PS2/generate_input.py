#!/apps/anaconda3/bin/python

import random

num_files = 5
nums_per_file = 1000

for i in range(1, num_files + 1):
    filename = f"input_{i}.txt"
    
    with open(filename, "w") as f:
        for _ in range(nums_per_file):
            f.write(str(random.randint(0, 10000)) + "\n")
