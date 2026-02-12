#!/apps/anaconda3/bin/python

import numpy as np
import glob

total_count = 0
total_sum = 0
means = []
counts = []
variances = []

files = sorted(glob.glob("output_*.txt"))

for file in files:
    with open(file) as f:
        lines = f.readlines()
        count = int(lines[0].split()[1])
        sum_val = float(lines[1].split()[1])
        mean = float(lines[2].split()[1])
        std = float(lines[3].split()[1])

        total_count += count
        total_sum += sum_val
        means.append(mean)
        counts.append(count)
        variances.append(std**2)

overall_mean = total_sum / total_count

overall_var = sum(
    counts[i] * (variances[i] + (means[i] - overall_mean)**2)
    for i in range(5)
) / total_count

overall_std = np.sqrt(overall_var)

with open("final_stats.txt", "w") as f:
    f.write(f"count {total_count}\n")
    f.write(f"sum {total_sum}\n")
    f.write(f"mean {overall_mean}\n")
    f.write(f"stdev {overall_std}\n")

print("Final statistics written to final_stats.txt")
