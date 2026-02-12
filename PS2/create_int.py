import random

file = 'input_5000.txt'

with open(file, 'w') as f:
    for _ in range(5000):
        num = random.randint(0, 10000)
        f.write(f"{num}\n")
