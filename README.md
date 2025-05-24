# tamaCLI 🐣

**tamaCLI** is a terminal-based pet that lives right inside your prompt!  
It's like a Tamagotchi, but it bleps at you every time you run a command.

<img width="299" alt="Screenshot 2025-05-22 at 4 57 21 PM" src="https://github.com/user-attachments/assets/7ffcb00e-b07c-4cd3-ae61-dbedb2dc3e11" />

> Terminal got lonely? Not anymore 😼

## 💻 Features

- Lives in your terminal prompt (no extra steps to run)
- Shows how your pet feels (happy, meh, or 💀)
- Gets hungrier over time
- Feed it with simple commands!

## 📸 Demo

```
user@computer 😾 hungry ~ % tamacli feed
😋 You fed your Tama! Hunger is now 6.
user@computer 😿 meh ~ % tamacli feed
😋 You fed your Tama! Hunger is now 9.
user@computer 😸 happy ~ %
```

## 🚀 Installation

### Prerequisites

TamaCLI works on **macOS** and **Linux**! 🐧🍏

You'll need:
- Python 3 (standard library only)
- `jq` (for JSON handling)

### Install Dependencies

**On macOS:**
```bash
brew install jq python3
```

**On Linux (Debian/Ubuntu):**
```bash
sudo apt-get install jq python3
```

Need help? Check out our guides:
- [How to Install Homebrew](guides/install-homebrew.md) (for macOS users)
- [Manual Installation Guide](guides/manual-install.md) (for other systems)

### Install tamaCLI

1. Clone the repository:
   ```bash
   git clone https://github.com/TamaCLI/TamaCLI-prompt.git
   cd TamaCLI-prompt
   ```

2. Run the installer:
   ```bash
   bash install.sh
   ```

3. Apply changes:
   ```bash
   source ~/.zshrc
   ```

That's it! Your pet should now be bleppin' in your terminal like a champ 😸

## 🍽️ Commands

| Command | What it does |
|---------|-------------|
| `tamacli feed` | Feed your pet when hungry |
| More soon... | Like `play`, `sleep`, `stats`? 👀 |

## 💾 How it Works

- A Python script tracks your pet's hunger in `~/.tamacli/state.json`
- A shell function shows the pet's mood directly in your prompt
- Hunger increases over time
- Feeding makes your pet happy again!

## 🐾 Future Ideas

- Multiple pets/names
- `play` and `sleep` commands
- More interactions and stats

## Disclaimer
TamaCLI is an independent project that is not affiliated with, endorsed by, or related to Tamagotchi, Bandai Namco Entertainment, or any of their trademarks or products. This project is purely for fun. Thanks for visiting!
