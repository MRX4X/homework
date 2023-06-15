#!/bin/bash
case "$1" in
-f) exec 1>$2 ;; 
esac
for (( i=0; i <= 19; i++ ));
do
echo "Bash - это лучшее что может быть"
done