

#!/bin/bash

echo "🐣 Installing TamaCLI..."

# Create pet data directory
mkdir -p ~/.tamacli

# Create initial pet state if it doesn't exist
if [ ! -f ~/.tamacli/state.json ]; then
  echo '{"hunger": 5, "last_update": '"$(date +%s)"'}' > ~/.tamacli/state.json
  echo "🌱 Created initial pet state."
fi

# Make sure feed script is executable
chmod +x ~/TamaCLI-prompt/feed.sh

# Check if ~/.zshrc exists
if [ ! -f ~/.zshrc ]; then
  touch ~/.zshrc
fi

# Append setup to .zshrc if not already present
if ! grep -q "TamaCLI setup" ~/.zshrc; then
  cat << 'EOF' >> ~/.zshrc

# === TamaCLI setup ===
setopt prompt_subst

function pet_status {
  python3 ~/TamaCLI-prompt/pet_status.py
}

export PS1='%n@%m $(pet_status) %1~ %# '

function tamacli() {
  case "$1" in
    feed)
      ~/TamaCLI-prompt/feed.sh
      ;;
    *)
      echo "TamaCLI commands: feed"
      ;;
  esac
}
# === End TamaCLI setup ===

EOF
  echo "✅ Added TamaCLI setup to your ~/.zshrc"
else
  echo "⚠️ TamaCLI setup already in ~/.zshrc"
fi

echo "✅ Done! Please run: source ~/.zshrc"