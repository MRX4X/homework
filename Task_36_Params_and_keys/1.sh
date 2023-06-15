if read  -t 3 -p "Введи имя преподавателя дисциплины Python: " name
then 
    echo "Вы правильно ввели имя $name"
else
    echo "Вы отчисленны"
fi

# if read  -t 3 -p "Введи имя преподавателя дисциплины Python: " name
# var1="Олег"
# if [ "$name" == "$var1" ]
# then 
#     echo "Вы правильно ввели имя $name"
# else
#     echo "Вы отчисленны"
# fi