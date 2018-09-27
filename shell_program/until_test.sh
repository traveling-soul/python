#!/bin/bash
flag=0
until (( $flag > 10  ))
do 
    echo $flag
    flag=$[ $flag + 1 ]
done
