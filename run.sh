#! /usr/bin/env bash

program="python3 mst.py"

# Find all files ending with ".in"
test_files=$(find . -type f -name "*.in")

# Iterate over each test file
for input_file in $test_files; do
    echo $input_file
    $program < $input_file
    echo
done