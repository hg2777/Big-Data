#!/bin/bash
set -e
python create_int.py
split -l 1000 -d input_5000.txt input_part_
