# Напишите скрипт который выводит фамилии студентов с надписью отчислен.
# При нажатии ctrl+c скрипт должен выводить надпись "тебе не избежать отчисления"
# Если нажать ctrl+c после 3 отчисленного студента печатается надпись "ладно, мы и так отчислили достаточно"
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
