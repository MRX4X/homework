#Перенаправьте ввод так чтобы выполнить команды хранящиеся в файле FileForTask1
#если возникнут ошибки перенаправьте в файл errors
#в конце очистите файл не удаляя его
exec 0<FileForTask1
exec 1>answer.txt
exec 2>Error

while read line
do
$line 
done
