name=""
if [ "$1" = "-n" ]; 
then
    name="$2"
    shift; shift;
fi

echo "студент $name"
echo "$@ отчислен"