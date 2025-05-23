#!/usr/bin/env python3
import os, json, time

STATE_FILE = os.path.expanduser("~/.tamacli/state.json")

if not os.path.exists(STATE_FILE):
    state = {"hunger": 5, "last_update": time.time()}
else:
    with open(STATE_FILE) as f:
        state = json.load(f)

now = time.time()
elapsed = int(now - state["last_update"])
hunger_increase = elapsed // 60
state["hunger"] = min(10, state["hunger"] + hunger_increase)
state["last_update"] = now

with open(STATE_FILE, "w") as f:
    json.dump(state, f)

h = state["hunger"]
if h < 4:
    print("😸")
elif h < 8:
    print("😿")
else:
    print("💀")