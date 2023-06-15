function check_pass() {
    num_student=$1
    i=1
    while [ $(( $i - 1 )) -ne $num_student ]
    do
        echo -n "Введите баллы для ученика $i: "
        read score
        if [ $score -ge 50 ]
        then
            echo "True"
        else
            echo -n "False " 
            echo "Вы отчислены"
        fi
        ((i++))
    done
}

read -p "Введите количество учеников: " num_students

check_pass $num_students