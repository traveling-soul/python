#!/bin/bash
var1="test"
var2="Test"
#test 使用>或<要转义
#if test $var1 = $var2
#注意里面的中括号两边有空格
if [[ var1 = var2 ]]
then
    echo "equal"
else
    echo "not equal"
fi
