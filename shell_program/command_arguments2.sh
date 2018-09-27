#!/bin/bash
# $#获取参数个数
for (( index=0; index <= $#; index++ ))
do
    echo ${!index}
done
