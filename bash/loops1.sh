#!/bin/bash

str="$1"
res=""

for (( i=${#str}-1; i>=0; i-- )); do
  res+=$(tr "[:upper:][:lower:]" "[:lower:][:upper:]" <<< "${str:$i:1}")
done

echo "$res"
