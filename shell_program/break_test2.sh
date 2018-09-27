#!/bin/bash
flag=0
while (( flag < 10 ))
do 
    for (( innerFlag=0; innerFlag < 5; innerFlag++ ))
    do
        if (( $innerFlag == 2 ))
        then
            break
        fi
        echo "innerFlag=$innerFlag" 
    done
    echo "outerFlag=$flag"
done
