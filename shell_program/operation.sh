#!/bin/bash
#输出13
expr 10 + 3

#输出字符串10+3
expr 10+3

expr 10 - 3

#转义
expr 10 \* 3

expr 10 / 3

expr 10 % 3

#将计算结果赋值给变量
num1=$(expr 10 % 3)

#将计算结果赋值给变量
num2=`expr 10 % 3`

echo num1: $num1
echo num2: $num2
