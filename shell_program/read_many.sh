#!/bin/bash
# read -p等价于echo -n + read
read -p "what's your name?" first last
echo first: $first
echo last: $last
