#! /bin/bash
git pull
kill -9 $(lsof -t -i:1080)
nohup python3 app.py
DISPLAY=:0 chromium-browser "$(hostname -I | awk '{print $1}'):1080" --start-fullscreen --disable-session-crashed-bubble