#!/bin/bash
flag=0
#while test $flag -le 10
#while [ $flag -le 10 ]
while (( flag <= 10 ))
do
    echo $flag
    flag=$[$flag + 1]
done
