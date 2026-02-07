#!/apps/anaconda3/bin/python
import math
path = "/user/xl3593/Desktop/part2_1000_integers.txt"
numbers = []
with open(path, "r") as f:
    for line in f:
        line = line.strip()
        if line:
            numbers.append(int(line))

count = len(numbers)
total = sum(numbers)
average = total / count

variance = sum((x - average) ** 2 for x in numbers) / count
std_dev = math.sqrt(variance)

print("Count:", count)
print("Sum:", total)
print("Average:", average)
print("Standard Deviation:", std_dev)

