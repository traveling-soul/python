#!/bin/bash
num1=100
num2=200
#if test $num1 -gt $num2
if [ $num1 -gt $num2 ]
#注意里面的圆括号两边有空格
#if (( num1 > num2 ))
then
    echo "num1 > num2"
else
    echo "num1 <= num2"
fi
