#!/usr/bin/env python3
import os, json, time, sys

STATE_FILE = os.path.expanduser("~/.tamacli/state.json")
DEFAULT_STATE = {
    "hunger": 10,  # 10 is full, 0 is starving
    "last_update": time.time(),
    "name": "Tama",
    "health": 10,
    "last_fed": time.time()
}

# Load or initialize state
def load_state():
    if not os.path.exists(STATE_FILE):
        return DEFAULT_STATE.copy()
    with open(STATE_FILE) as f:
        state = json.load(f)
    # Ensure all keys exist
    for k, v in DEFAULT_STATE.items():
        if k not in state:
            state[k] = v
    return state

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def get_mood(hunger, health):
    if health <= 2:
        return "💀", "dead"
    if hunger >= 8:
        return "😸", "happy"
    elif hunger >= 4:
        return "😿", "meh"
    else:
        return "😾", "hungry"

def tick(state):
    now = time.time()
    elapsed = int(now - state["last_update"])
    if elapsed >= 60:
        # Only decrease hunger by 1 per tick
        state["hunger"] = max(0, state["hunger"] - 1)
        state["last_update"] = now
        # Health decreases if hunger is low
        if state["hunger"] <= 3:
            state["health"] = max(0, state["health"] - 1)
        # Health recovers a bit if hunger is high
        elif state["hunger"] >= 8 and state["health"] < 10:
            state["health"] = min(10, state["health"] + 1)
        save_state(state)
    return state

def print_stats(state):
    print(f"Name: {state.get('name', 'Tama')}")
    print(f"Hunger: {state['hunger']} / 10")
    print(f"Health: {state['health']} / 10")
    emoji, word = get_mood(state['hunger'], state['health'])
    print(f"Mood: {emoji} {word}")
    last_fed = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(state.get('last_fed', time.time())))
    print(f"Last Fed: {last_fed}")

def set_name(state, new_name):
    state["name"] = new_name
    save_state(state)
    print(f"Your pet's name is now: {new_name}")

def doctor(state):
    if state["health"] < 10:
        state["health"] = min(10, state["health"] + 3)
        save_state(state)
        print("🩺 The doctor healed your pet! Health is now:", state["health"])
    else:
        print("🩺 Your pet is already at full health!")

def admin_set(state, statname, value):
    if statname == 'hunger':
        try:
            v = int(value)
            state['hunger'] = max(0, min(10, v))
            save_state(state)
            print(f"[ADMIN] Hunger set to {state['hunger']}")
        except ValueError:
            print("[ADMIN] Invalid value for hunger.")
    elif statname == 'health':
        try:
            v = int(value)
            state['health'] = max(0, min(10, v))
            save_state(state)
            print(f"[ADMIN] Health set to {state['health']}")
        except ValueError:
            print("[ADMIN] Invalid value for health.")
    elif statname == 'name':
        state['name'] = value
        save_state(state)
        print(f"[ADMIN] Name set to {state['name']}")
    else:
        print(f"[ADMIN] Unknown stat: {statname}")

if __name__ == "__main__":
    state = load_state()
    args = sys.argv[1:]
    if args:
        if args[0] == "--stats":
            print_stats(state)
        elif args[0] == "--set-name" and len(args) > 1:
            set_name(state, " ".join(args[1:]))
        elif args[0] == "--doctor":
            doctor(state)
        elif args[0] == "--admin-set" and len(args) > 2:
            admin_set(state, args[1], args[2])
        else:
            # Unknown argument, fallback to mood
            state = tick(state)
            emoji, word = get_mood(state["hunger"], state["health"])
            if state["health"] <= 2 or state["hunger"] <= 2:
                warning = ""
                if state["hunger"] <= 2 and state["health"] <= 2:
                    warning = "please feed & doctor!"
                elif state["hunger"] <= 2:
                    warning = "please feed!"
                elif state["health"] <= 2:
                    warning = "please doctor!"
                print(f"\033[48;5;196m{emoji} {word} {warning}\033[0m")  # red background
            else:
                print(f"\033[48;5;153m{emoji} {word}\033[0m")  # light blue background
    else:
        state = tick(state)
        emoji, word = get_mood(state["hunger"], state["health"])
        if state["health"] <= 2 or state["hunger"] <= 2:
            warning = ""
            if state["hunger"] <= 2 and state["health"] <= 2:
                warning = "please feed & doctor!"
            elif state["hunger"] <= 2:
                warning = "please feed!"
            elif state["health"] <= 2:
                warning = "please doctor!"
            print(f"\033[48;5;196m{emoji} {word} {warning}\033[0m")
        else:
            print(f"\033[48;5;153m{emoji} {word}\033[0m")