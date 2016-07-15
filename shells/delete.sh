#! /bin/bash


while true
    do
        find -cmin -1 | xargs rm -f 2>/dev/null
    done