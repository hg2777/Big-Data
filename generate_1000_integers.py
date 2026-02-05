import random

file = 'part2_1000_integers.txt'

with open(file, 'w') as f:
    for _ in range(1000):
        num = random.randint(0, 1000000)
        f.write(f"{num}\n")