#выведите отдельные слова из файла filefortask2.txt в столбик
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
