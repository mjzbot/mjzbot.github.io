#!/bin/bash
fileName=$(ls -1rt ~/Downloads/*.html | tail -n1)
cp "$fileName" ~/repos/mjzbot.github.io/
cd ~/repos/mjzbot.github.io/
git add -A
git commit -m "auto"
git push myrepo
pagename=$(echo "$fileName" | sed 's|.*/||')
echo https://mjzbot.github.io/"$pagename"
