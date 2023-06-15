#!/bin/bash
# while true
# do
# echo "Введите имя студента:"
while true
do
read -p "Введите имя студента:" var
echo "Отчислен студент - $var"
if [ "$var" == "off" ]
then
break
fi
done
# # if [[$stud_name = "off"]]
# # then
# # break
# # fi