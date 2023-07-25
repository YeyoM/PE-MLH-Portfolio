#!/bin/bash

echo "Entering project"
# Enter to the project
cd /root/PE-MLH-Portfolio
 
echo "Updating git repo"
# Update git repo
git fetch && git reset origin/main --hard 

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build
