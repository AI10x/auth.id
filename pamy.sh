#!/bin/bash

#add to /lib/security

source ~/genai/localqa/src/venv/bin/activate


sudo rm ~/genai/capture.jpg

ffmpeg -f v4l2 -i /dev/video0 -vframes 1 -q:v 2 ~/genai/capture.jpg


# Imagine 'data.txt' has the same content as the Python example.

echo "--- Method 1: Using grep and an if statement ---"
# We can check the entire output at once. 'grep -q' is silent and just sets the exit code.
# It returns 0 (success) if "ERROR" is found, which the 'if' statement executes on.




if  python3 /lib/security/far.py | grep -q "TRUE"; then
    echo "test"
    exit 0
else
    exit 1
fi



