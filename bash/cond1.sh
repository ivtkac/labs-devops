#!/bin/bash

IFS=',' read -r -a array <<< "$1"

sum=0
for num in "${array[@]}"; do
  if ! (( num % 2 )); then
    sum=$((sum+num)) 
  fi
done

echo "$sum"
