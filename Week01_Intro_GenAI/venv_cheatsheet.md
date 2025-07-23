# Python `venv` Cheatsheet

## What is `venv` and Why Use It?

A Python **virtual environment** (`venv`) is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using `venv` allows you to:
- Isolate project dependencies, avoiding conflicts between packages required by different projects.
- Ensure reproducibility by keeping dependencies consistent across development, testing, and production.
- Avoid requiring administrative privileges to install packages globally.

## Basic `venv` Commands

### 1. Create a Virtual Environment

**Mac/Linux:**
```bash
python3 -m venv myenv
```

**Windows:**
```cmd
python -m venv myenv
```

---

### 2. Activate the Virtual Environment

**Mac/Linux:**
```bash
source myenv/bin/activate
```

**Windows (Command Prompt):**
```cmd
myenv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
myenv\Scripts\Activate.ps1
```

---

### 3. Deactivate the Virtual Environment

**All Platforms:**
```bash
deactivate
```

---

### 4. Remove a Virtual Environment

Just delete the environment folder:
```bash
rm -rf myenv  # Mac/Linux
```
```cmd
rmdir /s myenv  # Windows
```

---

### 5. Check Python Executable Location

```bash
which python  # Mac/Linux
where python  # Windows
```

---

**Tip:** Always activate your virtual environment before installing packages for your project! 