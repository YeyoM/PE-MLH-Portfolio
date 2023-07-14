#!/bin/bash

echo "Entering project"
# Enter to the project
cd /root/PE-MLH-Portfolio
 
echo "Updating git repo"
# Update git repo
git fetch && git reset origin/main --hard 

echo "Installing py req"
# Enter venv and install requirements
source python3-virtualenv/bin/activate && pip install -r requirements.txt

systemctl restart myportfolio
