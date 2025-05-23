# tamaCLI 🐣

**tamaCLI** is a terminal-based pet that lives right inside your prompt!  
It’s like a Tamagotchi, but it bleps at you every time you run a command.

<img width="299" alt="Screenshot 2025-05-22 at 4 57 21 PM" src="https://github.com/user-attachments/assets/7ffcb00e-b07c-4cd3-ae61-dbedb2dc3e11" />

> Terminal got lonely? Not anymore 😼

---

## 💻 What it do:

- Lives in your terminal prompt (no extra steps to run)
- Shows how your pet feels (happy, meh, or 💀)
- Gets hungrier over time
- You can feed it with a command:  
  ``tamacli feed``

---

## 📸 Demo

``cardiffemde@Cardiffs-MacBook-air 😸 ~ %``  
``echo hello``  
``hello``  
``cardiffemde@Cardiffs-MacBook-air 😿 ~ %``  
``tamacli feed``  
``😋 You fed your Tama! Hunger is now 2.``  
``cardiffemde@Cardiffs-MacBook-air 😸 ~ %``

---

## 🛠️ Setup Instructions

1. **Download the repo**  
   ``git clone https://github.com/YOUR_USERNAME/tamacli.git``  
   ``cd tamacli``

2. **Install TamaCLI**  
   ``bash install.sh``

3. **Reload your shell**  
   ``source ~/.zshrc``

Now your prompt should show your pet — and it’ll get hungry the longer you ignore it 👀

---

## 🍽️ Commands

| Command        | What it does            |
|----------------|--------------------------|
| ``tamacli feed`` | Lowers hunger            |
| more soon...   | like ``play``, ``sleep``, ``stats``? 👀 |

---

## 💾 How it works

- A Python script tracks your pet's hunger in ``~/.tamacli/state.json``
- A shell function shows the pet's mood directly in your prompt
- Every minute, hunger goes up
- Feeding lowers hunger and makes Tama happy again

---

## 📦 Requirements

- macOS or Linux
- Python 3
- ``jq`` (for feeding)

---

## 🐾 Future ideas

- Multiple pets / names
- ``play`` and ``sleep`` commands
- Death + rebirth system 😳
- Animations? Maybe? idk

---

Made with blep by [Card](https://github.com/Cardsea) 💖

