exec 3> done

echo "Приветмир" >&3

for file in ./2_Task/*
do
cat $file >&3
done

echo "Скрипт завершил работу"