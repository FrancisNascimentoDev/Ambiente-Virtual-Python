
# 🐍 Python Virtual Environment Setup for VS Code

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

> 🇧🇷 **Prefere português? [Clique aqui para a versão em português](README.pt.md)**

Easily create a Python virtual environment and configure VS Code to use it automatically. This setup is ideal for personal projects, scripts, APIs, and microservices.

---

## 🧭 Table of Contents

- [📦 What's Included](#-whats-included)
- [🚀 How to Use](#-how-to-use)
- [💡 Activate and Deactivate venv](#-activate-and-deactivate-venv)
- [📁 Manage Dependencies](#-manage-dependencies)
- [🧰 Requirements](#-requirements)
- [🛠️ Best Practices](#️-best-practices)
- [📜 License](#-license)
- [👤 Author](#-author)

---

## 📦 What's Included

- `setup_venv.py`: Python script to:
  - Create a `venv/` virtual environment
  - Generate `.vscode/settings.json` pointing to the venv Python
  - Show activation instructions in the terminal
- Works on Windows, Linux, and macOS
- Auto-configures VS Code

---

## 🚀 How to Use

### 1. Clone this repository or download the files

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Run the script in VS Code's terminal

```bash
python setup_venv.py
# or
python3 setup_venv.py
```

> 💡 VS Code will be set to use the virtual environment's Python automatically.

---

## 💡 Activate and Deactivate venv

### To activate the virtual environment:

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Linux / macOS:
```bash
source venv/bin/activate
```

### To deactivate:
```bash
deactivate
```

---

## 📁 Manage Dependencies

### Install packages:
```bash
pip install package-name
```

### Save installed packages:
```bash
pip freeze > requirements.txt
```

### Install from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🧰 Requirements

- Python 3.6 or higher
- VS Code installed
- Official Python extension for VS Code

---

## 🛠️ Best Practices

- Always use a virtual environment to isolate dependencies.
- Keep your `requirements.txt` up to date.
- Add the `venv/` directory to `.gitignore`:
  ```bash
  echo "venv/" >> .gitignore
  ```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👤 Author

Made with 💻 by **Francis Nascimento**  
🔗 [Meu GitHub](https://github.com/FrancisNascimentoDev)  
📧 francisn.dev@gmail.com  
🌐 [Meu Portefólio](https://francisnascimentodev.github.io/FrancisDev/)

---
