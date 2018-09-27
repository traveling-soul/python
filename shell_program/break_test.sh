#!/bin/bash
for (( flag=0; flag <= 10; flag++ ))
do
    if (( $flag == 5 ))
    then
        break
    fi
    echo $flag
done
