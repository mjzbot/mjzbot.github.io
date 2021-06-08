#!/bin/bash
fileName=$(ls -1rt ~/Downloads/*.html | tail -n1)
cp "$fileName" ~/repos/mjzbot.github.io/
cd ~/repos/mjzbot.github.io/
git add -A; and git commit -m "auto"; and git push myrepo
