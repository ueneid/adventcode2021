#!/bin/bash

function run() {
    day=$1
    input=$2
    if [ "$input" = "" ]; then
        input="sample"
    fi
    if [ ! -f "./$day/$input.txt" ]; then
        echo "Cannot find file: ./$day/$input.txt"
        exit 1
    fi

    cat "./$day/$input.txt" | python $day/answer.py
}

run $@