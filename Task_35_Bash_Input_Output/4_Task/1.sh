for (( i = 0; i < 31; i++ )); do
if [ $(( $i % 2 )) -eq 0 ]; then
    echo $i >>$1
else
  echo $i
fi
done