#!/bin/bash

echo "Step 1: Generating input files"

jid1=$(grid_run --grid_submit=batch --grid_mem=1G ./generate_input.py | awk '{print $3}')

echo "Step 1 JobID: $jid1"

echo "Step 2: Analyzing input (parallel process)"

jid2=$(grid_run --grid_submit=batch --grid_array=1-5:1/5 --grid_mem=1G --grid_hold=$jid1 ./analyze_file.py | awk '{print $3}' | cut -d'.' -f1)

echo "Step 2 JobID: $jid2"

echo "Step 3: Post process"

jid3=$(grid_run --grid_submit=batch --grid_mem=1G --grid_hold=$jid2 ./postprocess.py | awk '{print $3}')

echo "Step 2 JobID: $jid3"