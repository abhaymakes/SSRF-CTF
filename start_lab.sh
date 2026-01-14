#!/bin/bash

RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
NC='\e[0m'


get_pid() {
  lsof -t -i :$1
}


kill_port() {
  PID=$(get_pid $1)
  if [ -n "$PID" ]; then
    echo -e "${RED}[*] Port $1 is in use. Killing process with PID $PID...${NC}"
    kill -9 $PID
  fi
}


kill_port 12345
kill_port 1999

echo -e "${GREEN}[*] Starting lab...${NC}"
echo -e "${BLUE}[*] Setting up virtual environment...${NC}"
python -m venv env
echo -e "${GREEN}[*] Environment setup successfully!${NC}"
echo -e "${BLUE}[*] Activating environment...${NC}"
source ./env/bin/activate
echo -e "${BLUE}[*] Installing requirements.py${NC}"
pip install -r requirements.txt
echo -e "${BLUE}[*] Requirements installed successfully!${NC}"

export FLASK_APP=main.py
flask run --port 12345 &
echo -e "${GREEN}[*] Running target server at 127.0.0.1:12345${NC}"

export FLASK_APP=flag_target.py
flask run --port 1999 &
echo -e "${GREEN}[*] Running flag server at 127.0.0.1${NC}"

echo -e "${GREEN}[*] Happy Hunting!${NC}"
