#!/apps/anaconda3/bin/python

import string


def analyze_file(filename):
    alphabet = string.ascii_lowercase

    # initialize counts manually
    counts = {letter: 0 for letter in alphabet}
    total_letters = 0

    # read file line-by-line
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()

            for ch in line:
                if ch in alphabet:
                    counts[ch] += 1
                    total_letters += 1

    # frequencies
    frequencies = {}
    for letter in alphabet:
        if total_letters > 0:
            frequencies[letter] = counts[letter] / total_letters
        else:
            frequencies[letter] = 0

    # checksum
    checksum = 0
    for i, letter in enumerate(alphabet):
        checksum += (i + 1) * counts[letter]

    return counts, frequencies, total_letters, checksum


def save_results(filename, counts, freqs, total, checksum):
    output_file = filename.replace(".txt", "_summary.txt")

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"Summary for {filename}\n")
        out.write(f"Total letters: {total}\n")
        out.write(f"Checksum: {checksum}\n\n")

        out.write("Letter\tCount\tFrequency\n")

        for letter in string.ascii_lowercase:
            out.write(f"{letter}\t{counts[letter]}\t{freqs[letter]:.6f}\n")

    print(f"Results saved to {output_file}")


def main():
    filename = input("Enter sub-sample file name: ").strip()

    counts, freqs, total, checksum = analyze_file(filename)
    save_results(filename, counts, freqs, total, checksum)


if __name__ == "__main__":
    main()
