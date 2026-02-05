#!/bin/bash

read -p "Input: " input

split -l 25000 "$input" x

for f in xaa xab xac xad xae; do
    ./assignment1_analyze.py "$f" > "$f.out"
done

i=1
for f in x*.out; do
    echo "Sample $i" >> "assignment1.txt"
    cat "$f" >> "assignment1.txt"
    i=$((i+1))
done

