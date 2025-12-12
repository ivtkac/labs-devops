#!/bin/bash

count="$1"

if [[ $count -eq 1 ]]; then
  mkdir -p "folder_a"
  echo "1 folder created: folder_a"
  exit
fi

folders=()
pos=0
for letter in {a..z}; do
  if [[ $pos -eq $count ]]; then
    break
  fi
  new_dir="folder_$letter"
  mkdir -p "$new_dir"

  folders+=("$new_dir")
  ((pos++))
done

printf "%d folders created: " "$count"
printf "%s" "${folders[0]}"
printf ", %s" "${folders[@]:1}"
printf "\n"
