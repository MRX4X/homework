#!/bin/bash
if [ -n "$1" ]
then
read -p "Введите логин:" log
read -p "Введите пароль:" par
echo "Логин - $log" >> user.txt
echo "Пароль - $par" >> user.txt
echo "Вы успешно зарегистрировались"
else
echo "А что вы тут делайте?"
fi

