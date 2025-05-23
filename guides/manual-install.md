# 📦 TamaCLI Manual Install Guide

This guide is for people who prefer installing everything manually, without using ``requirements.txt``.

---

## 🐍 Python

- TamaCLI only uses Python’s **standard library**
- No extra packages needed
- Just make sure you have ``python3`` installed

---

## 🐚 Shell Tools

TamaCLI depends on the following shell tool:

- ``jq`` – used in shell scripts to edit your pet’s JSON save file

---

## 🔧 How to Install Everything Manually

### On macOS (with Homebrew)

If you don’t have Homebrew, install it here:  
[install-homebrew.md](guides/install-homebrew.md)

Then run:

``brew install python jq``

### On Debian/Ubuntu Linux

``sudo apt-get update``  
``sudo apt-get install -y python3 jq``

---

Once you’ve installed these tools, you’re ready to run:  
``bash install.sh``  
and start chillin’ with your terminal pet 😸