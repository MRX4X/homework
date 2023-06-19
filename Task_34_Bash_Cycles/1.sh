#Напишите скрипт который выводит все исполняемые файлы в системе
#!/bin/bash
for file in /denis/*
do
if [ -x "$file" ]
then
echo "$file"
fi
done
