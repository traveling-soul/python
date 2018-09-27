#!/bin/bash
echo "input:"
read num
case $num in
1)
    echo "num=1";;
2)
    echo "num=2";;
3)
    echo "num=3";;
4)
    echo "num=4";;
*)
    echo "default";;
esac
