#!/bin/bash

cp "passwd" "passwd_new"

awk -F: -v OFS=: '$1=="saned" {$7="/bin/bash"}1' passwd_new > temp && mv temp passwd_new

sed -i '/^avahi:/s,/usr/sbin/nologin,/bin/bash,' passwd_new

awk -F: -v OFS=: '{print $1, $3, $5, $7}' passwd_new > temp && mv temp passwd_new

sed -i '/daemon/d' passwd_new

awk -F: -v OFS=: '$3 % 2 == 0 {$7="/bin/zsh"}1' passwd_new > temp && mv temp passwd_new
