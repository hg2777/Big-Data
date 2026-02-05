#!/apps/anaconda3/bin/python
from statistics import mean, stdev

path = "/user/xl3594/Desktop/random_integers.txt"

with open(path) as f:
    nums = [int(line) for line in f if line.strip()]

print("count: ", len(nums))
print("sum: ", sum(nums))
print("mean: ", mean(nums))
print("standard deviation: ", stdev(nums))