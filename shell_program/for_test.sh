#!/bin/bash
#for str in a b c d e
#do 
#    echo $str
#done

#list="a,b,c,d,e"
#for str in $list
#do
#    echo $str
#done

#定义一个变量保存IFS的值
oldIFS=$IFS
#修改IFS的值
IFS=$','
list="a,b,c,d,e"
list2="a b c d e"
for var in $list
do
    echo $var
done

for var2 in $list2
do
    echo $var2
done
#还原IFS的值
IFS=$oldIFS

