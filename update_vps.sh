#!/bin/bash

# Auto-updater for VPS receiver
cd /opt/lagswitch || { echo "[!] /opt/lagswitch not found"; exit 1; }

echo "[+] Pulling latest changes..."
git pull origin main || { echo "[!] Git pull failed"; exit 1; }

echo "[+] Installing dependencies..."
pip3 install -r requirements.txt

echo "[+] Restarting receiver..."

# Kill old process
pkill -f vps_lagswitch_receiver.py

# Relaunch
nohup python3 vps_lagswitch_receiver.py &

echo "[+] Receiver updated and restarted."
