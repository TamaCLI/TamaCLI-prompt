# 🍺 How to Install Homebrew on macOS

Homebrew is a package manager for macOS that makes it super easy to install stuff like ``python`` and ``jq``.

---

## 🛠️ Step-by-Step

1. **Open your Terminal**

You can press ``Cmd + Space`` and type ``Terminal`` to open it.

2. **Run the install command**

Paste this into your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. **Follow the on-screen instructions**

It might ask for your Mac password. That’s normal!

---

## ✅ After It's Installed

Once Homebrew is set up, you can use it to install dependecies like this:

```bash
brew install python jq
```

see more about installing dependecies here: [manual-install.md.](guides/manual-install.md)

---

## 🧠 Test if it worked

Try these commands:

```bash
brew --version
```

If it returns a version number, you're good to go!
and learn how to install dependecies manually [here!](guides/manual-install.md)

---

Need help? Visit the official Homebrew website:  
[https://brew.sh](https://brew.sh)