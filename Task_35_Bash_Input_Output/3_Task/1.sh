# напишите скрипт который выводит надпись "Bash - это лучшее что может быть" 20 раз в консоль
# если передан ключ -f то после него идет имя файла в который перенаправляется вывод
#!/bin/bash
case "$1" in
-f) exec 1>$2 ;; 
esac
for (( i=0; i <= 19; i++ ));
do
echo "Bash - это лучшее что может быть"
done
