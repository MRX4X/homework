count=1

trap "echo 'Ты меня не остановишь'" SIGINT

while true
do
    if [[ $count -gt 10 ]]
    then
        trap "echo ' Тaк уж и быть'; exit" SIGINT
    fi
    echo "Я всё ещё тут"
    sleep 5 
    count=$(( $count + 1 ))
done