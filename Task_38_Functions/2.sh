#Напишите программу считающую и обрабатывающую индекс массы тела.
#В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
#от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
#Формула определения ИМТ: index = weight / (height * height)
function imt() {
    echo $(( $2 / ( $1 * $1 ))
}

function check() {
    if [[ $1 -lt 18,5 ]]
    then
        echo "Недостаточный вес"
    elif [[ $1 -gt 18,5 ]] && [[ $1 -lt 25  ]]
    then
        echo "ИМТ в норме"
    else
        echo "Избыточный вес"
    fi
}

read -p "Weight: " weight
read -p "Height: " height

result=$( imt height weight  )
check $result
