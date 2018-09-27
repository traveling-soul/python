#!/bin/bash
num1=10
num2=3
echo "num1 + num2=$[$num1 + $num2]"
echo "num1 + num2=$[$num1+$num2]"

echo "num1 - num2=$[$num1-$num2]"

echo "num1 * num2=$[$num1 * $num2]"

echo "num1 > num2=$[$num1>$num2]"
echo "num1 < num2=$[$num1<$num2]"

#将运算结果赋值给变量
num3=$[$num1 / $num2]
echo "num3=$num3"
