#!/bin/bash
fileName=$(ls -1rt ~/Downloads/*.html | tail -n1)
cp "$fileName" ~/repos/mjzbot.github.io/
cd ~/repos/mjzbot.github.io/
python3 gen_index.py
git add -A
git commit -m "auto" --quiet
git push myrepo --quiet
pagename=$(echo "$fileName" | sed 's|.*/||')
echo https://mjzbot.github.io/"$pagename"
