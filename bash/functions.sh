#!/bin/bash

pow() {
  local a="$1"
  local b="$2"

  echo $(( "$a" ** "$b" ))
}

shortest() {
  local min_len=${#1}
  local res=("$1")

  shift
  for str in "$@"; do
    if [[ ${#str} -lt $min_len ]]; then
      min_len=${#str}
      res=("$str")
    elif [[ ${#str} -eq $min_len ]]; then
      res+=("$str")
    fi
  done

  printf "%s\n" "${res[@]}"
}

print_log() {
  local msg="$1"
  echo "[$(date +"%Y-%m-%d %H:%M")] $msg"
}
