#!/bin/bash
count=0

trap "echo ''; echo 'тебе не избежать отчисления'" SIGINT

while true
do
    if [[ $(($count)) > 3 ]]
    then
        trap "echo ''; echo 'ладно, мы и так отчислили достаточно'; exit" SIGINT
    fi
    read -p "Введите имя студента которого хотите отчислить: " name
    echo "Вы отчислили студента: $name"
    count=$(( $count + 1 ))
done