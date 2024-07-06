#!/bin/bash
fileName=$(ls -1rt ~/Downloads/*.html | tail -n1)
cp "$fileName" ~/repos/mjzbot.github.io/
cd ~/repos/mjzbot.github.io/
tree -H "." -L 1 --noreport --houtro "" --dirsfirst --charset utf-8 --ignore-case --timefmt "%d-%b-%Y %H:%M" -I "index.html" -T "Collections" -s -D -o index.html
git add -A
git commit -m "auto" --quiet
git push myrepo --quiet
pagename=$(echo "$fileName" | sed 's|.*/||')
echo https://mjzbot.github.io/"$pagename"
