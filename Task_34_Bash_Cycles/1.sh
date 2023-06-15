#!/bin/bash
for file in /denis/*
do
if [ -x "$file" ]
then
echo "$file"
fi
done