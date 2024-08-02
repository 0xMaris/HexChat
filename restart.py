##!/bin/bash

pushover_user_key=""
pushover_api_key=""

echo "Script started at $(date)" 

while true; do
    echo "Killing HexChat process at $(date)"
    pkill hexchat

    # Wait a moment to ensure the process is completely terminated
    sleep 5

    echo "Restarting HexChat at $(date)" 
    # Restart HexChat with commands to connect to a network, running HexChat in the background
    nohup hexchat &

    curl -s \
        -F "token=$pushover_api_key" \
        -F "user=$pushover_user_key" \
        -F "message=HexChat has been reinitialized at $(date)" \
        https://api.pushover.net/1/messages.json
    
    # Wait for an amount of time (14400 seconds)
    echo "Sleeping for 4 hours at $(date)" 
    sleep 14400

done
