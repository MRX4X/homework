#!/bin/bash
for entry in $(cat ./FileforTask)
do
echo $entry
IFS=';' read -ra my_array <<< "$entry"
for str in "${my_array[@]}"
do
echo $str
done
done