exec 0<FileForTask1
exec 1>answer.txt
exec 2>Error

while read line
do
$line 
done
