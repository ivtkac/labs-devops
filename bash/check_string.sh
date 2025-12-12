#!/bin/bash

SYMBOLS="*!@#$%^&()_+"

str="$1"
declare -A counts=(
  [letters]=0
  [digits]=0
  [symbols]=0
)

for (( i=0; i<${#str}; i++ )); do
  ch="${str:$i:1}"

  case "$ch" in
    [[:alpha:]]) ((counts[letters]++)) ;;
    [[:digit:]]) ((counts[numbers]++)) ;;
    *) [[ "$SYMBOLS" == *"$ch"* ]] && ((counts[symbols]++)) ;;
  esac
done

printf "Numbers: %d Symbols: %d Letters: %d\n" \
    "${counts[numbers]}" "${counts[symbols]}" "${counts[letters]}"
