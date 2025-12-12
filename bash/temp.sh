#!/bin/bash

temp="$1"

unit="${temp: -1}"
val="${temp%?}"

case "$unit" in
  "C")
    val=$((val+273))
    unit="K"
    ;;
  "K")
    val=$((val-273))
    unit="C"
    ;;
esac

echo "$val$unit"
