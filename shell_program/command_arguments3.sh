#!/bin/bash
# $*把所有参数当作一个单词保存，相当于一个字符串
# $@把所有参数当作同一字符串中的多个独立的单词
var1=$*
var2=$@
echo "var1: $var1"
echo "var2: $var2"
countvar1=1
countvar2=1
for param in "$*"
do 
    echo "first loop param$countvar1: $param"
    countvar1=$[ $countvar1 + 1 ]
done
echo "countvar1: $countvar1"

for param in "$@"
do
    echo "second param$countvar2: $param"
    countvar2=$[ $countvar2 + 1 ]
done
echo "countvar2: $countvar2"
