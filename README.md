# auth.id
Attempt Auth face (open) gui-password lock

# OpenfaceID

This is a repo for open code face verfication methodology

## Features
-Accurate face verification
-GDM-password (open GUI - Ubuntu 25.04) lock
-Local host
-Huggingface framework (hub upload)

## Setup

### 1. Clone the repository
```bash
git clone <repo-url>
pip3 -r install pypi_reque.txt
parse README using codex/gemini cli and follow tutorial of CLI Agent to Prod
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv OpenFaceID
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Dependecies

```
insightface
face_recognition
cv2
```

## Running Tests
```/usr/bin/bash & /usr/bin/{venv}/python3 
bash pamy.sh
python3 face_verify.py
```

## Notes & issues
- Slow on lower-end machines (Mojo python Opt (that is, exclude the python virtual machine) - would be useful)
-Might crash on screen-lock and halt the program in total (restarting is recommended) 
- Requires great lighting 

#kudos decvb for repo README Template