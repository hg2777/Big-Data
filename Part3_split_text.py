#!/apps/anaconda3/bin/python

def split_file():
    filename = input("Enter the primary input file name: ").strip()

    lines_per_file = 25000
    num_files = 5

    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(num_files):
            output_name = f"sub_input_{i+1}.txt"
            with open(output_name, 'w', encoding='utf-8') as out:
                for _ in range(lines_per_file):
                    line = f.readline()
                    if not line:   # stop if file ends early
                        break
                    out.write(line)

            print(f"Created {output_name}")

    print("Done.")

if __name__ == "__main__":
    split_file()

        