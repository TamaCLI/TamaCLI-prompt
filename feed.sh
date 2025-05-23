#!/bin/bash
STATE=~/.tamacli/state.json

if [ ! -f "$STATE" ]; then
  echo '{"hunger": 5, "last_update": '"$(date +%s)"'}' > "$STATE"
fi

hunger=$(jq '.hunger' "$STATE")
new_hunger=$((hunger - 3))
[ $new_hunger -lt 0 ] && new_hunger=0
jq ".hunger = $new_hunger | .last_update = $(date +%s)" "$STATE" > "$STATE.tmp" && mv "$STATE.tmp" "$STATE"

echo "😋 You fed your Tama! Hunger is now $new_hunger."