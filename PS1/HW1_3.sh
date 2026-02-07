#!/bin/bash
set -euo pipefail

read -p "Input: " INPUT_FILE


SLICE_PREFIX="./slice_"
OUT_PREFIX="./part_"
SUMMARY="./summary_output.txt"

# 1.2: Take first 125000 lines, then split into 5 files of 25000 lines each
head -n 125000 "$INPUT_FILE" > ./first_125k.txt
split -l 25000 -d -a 1 ./first_125k.txt "$SLICE_PREFIX"

for i in 0 1 2 3 4; do
  mv "${SLICE_PREFIX}${i}" "${SLICE_PREFIX}$((i+1)).txt"
done

# 1.3
for s in 1 2 3 4 5; do
  ./lexical_analysis.py "${SLICE_PREFIX}${s}.txt" "${OUT_PREFIX}${s}.txt" "$s"
done

# 1.4
for s in 1 2 3 4 5; do
  cat "${OUT_PREFIX}${s}.txt" >> "$SUMMARY"
  echo "" >> "$SUMMARY"
done
