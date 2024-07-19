#!/bin/bash

program="python3 mcst.py"

# Find all files ending with ".in"
test_files=$(find . -type f -name "*.in")

# Iterate over each test file
for input_file in $test_files; do

    # Print test file name
    echo "Testing $input_file"

    # Generate expected output file name
    expected_file="${input_file%.in}.expected"
    
    # Run the program with input from the current test file
    output=$($program < "$input_file")
    
    # Read the expected output from the corresponding .expected file
    expected_output=$(cat "$expected_file")
    
    # Compare the program's output with the expected output
    if [ "$output" != "$expected_output" ]; then
        echo "Test failed..."
        diff <(echo "$expected_output") <(echo "$output")
    else
        echo "Test passed!"
    fi

    echo "-----------------------------------------"
done
