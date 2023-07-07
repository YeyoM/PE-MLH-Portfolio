#!/bin/bash

# Kill tmux sessions
tmux kill-server

echo "Entering project"
# Enter to the project
cd PE-MLH-Portfolio
 
echo "Updating git repo"
# Update git repo
git fetch && git reset origin/main --hard 

echo "Installing py req"
# Enter venv and install requirements
source python3-virtualenv/bin/activate && pip install -r requirements.txt

echo "Starting tmux"
# Start new tmux session and run flask
tmux new-session -d -s prod 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
