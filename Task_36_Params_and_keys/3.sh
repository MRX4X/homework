#Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
write_file=$1
file=$2
touch $file
echo "$write_file" > $file
