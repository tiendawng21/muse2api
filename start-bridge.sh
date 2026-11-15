#!/usr/bin/env bash
# Start the muse2api bridge inside the Codespace (background, logged).
# Rescue command if the auto-start did not run:  bash start-bridge.sh
cd "$(dirname "$0")"
nohup .venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 18610 > /tmp/bridge.log 2>&1 &
echo "bridge starting (pid $!) - verify with: curl localhost:18610"
