# tamaCLI 🐣

**tamaCLI** is a terminal-based pet that lives right inside your prompt!  
It's like a Tamagotchi, but it bleps at you every time you run a command.

<img width="299" alt="Screenshot 2025-05-22 at 4 57 21 PM" src="https://github.com/user-attachments/assets/7ffcb00e-b07c-4cd3-ae61-dbedb2dc3e11" />

> Terminal got lonely? Not anymore 😼

---

## 💻 What it do:

- Lives in your terminal prompt (no extra steps to run)
- Shows how your pet feels (happy, meh, or 💀)
- Gets hungrier over time
- You can feed it with a command:  
  ```tamacli feed```

---

## 📸 Demo

```cardiffemde@Cardiffs-MacBook-air 😸 ~ %```  
```echo hello```  
```hello```  
```cardiffemde@Cardiffs-MacBook-air 😿 ~ %```  
```tamacli feed```  
```😋 You fed your Tama! Hunger is now 2.```  
```cardiffemde@Cardiffs-MacBook-air 😸 ~ %```

---

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR_USERNAME/tamacli.git
   ```  
   ```bash 
   cd tamacli
   ```

2. **Run the installer**

   Just run this one command to set everything up:  
   ```bash
   bash install.sh
   ```

   This will:  
   – Create your pet's save file  
   – Add TamaCLI to your terminal prompt  
   – Set up the ```tamacli``` command

3. **Apply the changes**

   Reload your terminal or run:  
   ```bash
   source ~/.zshrc
   ```

   That's it! Your pet should now be bleppin' in your terminal like a champ 😸

Now your prompt should show your pet — and it'll get hungry the longer you ignore it 👀

---

## 🍽️ Commands

| Command        | What it does            |
|----------------|--------------------------|
| ```tamacli feed``` | Lowers hunger            |
| more soon...   | like ```play```, ```sleep```, ```stats```? 👀 |

---

## 💾 How it works

- A Python script tracks your pet's hunger in ```~/.tamacli/state.json```
- A shell function shows the pet's mood directly in your prompt
- Every minute, hunger goes up
- Feeding lowers hunger and makes Tama happy again

---

## 📦 Requirements

TamaCLI works on **macOS** and **Linux**! 🐧🍏

- Python 3 (standard library only)
- `jq` (for feeding)

All required dependencies are listed in `requirements.txt`.

### 🛠️ Install dependencies

**macOS (Homebrew):**
```sh
xargs -a requirements.txt brew install
```

**Linux (apt):**
```sh
xargs -a requirements.txt sudo apt-get install -y
```

If you use another OS or package manager, just install the tools listed in `requirements.txt` manually.

---

## 🐾 Future ideas

- Multiple pets / names
- ```play``` and ```sleep```