#!/apps/anaconda3/bin/python
import sys
import string

in_path = sys.argv[1]
out_path = sys.argv[2]
sample_no = sys.argv[3]

letters = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
counts = {ch: 0 for ch in letters}
total_letters = 0

with open(in_path, "r", errors="ignore") as f:
    for line in f:
        for ch in line.lower():
            if ch in counts:
                counts[ch] += 1
                total_letters += 1

# Frequencies (not counts)
if total_letters == 0:
    freqs = {ch: 0.0 for ch in letters}
else:
    freqs = {ch: counts[ch] / total_letters for ch in letters}

# Checksum
checksum = 0
for i, ch in enumerate(letters, start=1):
    checksum += i * counts[ch]

with open(out_path, "w") as out:
    out.write(f"Sample {sample_no}\n")
    for ch in letters:
        out.write(f"{ch}: {freqs[ch]}\n")
    out.write(f"total_letters: {total_letters}\n")
    out.write(f"checksum: {checksum}\n")

