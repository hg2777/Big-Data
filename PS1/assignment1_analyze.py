#!/apps/anaconda3/bin/python

import sys

input_file = sys.argv[1]

characters = ""
with open(input_file, "r") as f:
    for line in f:
        characters += line.strip()

characters = characters.lower()

freq = {}
for ch in characters:
    if ch.isalpha():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

char_sum = 0
checksum = 0
for ch in freq:
    char_sum += freq[ch]
    checksum += freq[ch] * (ord(ch) - ord("a") + 1)

output = ""
for ch in freq:
     output += f"{ch}: {float(freq[ch]) / float(char_sum):.5f}, "
print(output)
print("total sum: " + str(char_sum))
print("checksum: " + str(checksum))

