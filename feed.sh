#!/bin/bash
STATE=~/.tamacli/state.json

if [ ! -f "$STATE" ]; then
  echo '{"hunger": 10, "last_update": '"$(date +%s)"', "name": "Tama", "health": 10, "last_fed": '"$(date +%s)"'}' > "$STATE"
fi

hunger=$(jq '.hunger' "$STATE")
new_hunger=$((hunger + 3))
[ $new_hunger -gt 10 ] && new_hunger=10
jq ".hunger = $new_hunger | .last_update = $(date +%s) | .last_fed = $(date +%s)" "$STATE" > "$STATE.tmp" && mv "$STATE.tmp" "$STATE"

echo "😋 You fed your Tama! Hunger is now $new_hunger."