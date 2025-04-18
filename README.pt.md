
# 🐍 Ambiente Virtual Python para VS Code

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

> 🇺🇸 **Prefer English? [Click here for the English version](README.en.md)**

Automatize a criação de ambiente virtual em Python e configure o VS Code para usar a `venv` corretamente. Este setup é ideal para projetos pessoais, scripts, APIs e microserviços em Python.

---

## 🧭 Sumário

- [📦 O que está incluído?](#-o-que-está-incluído)
- [🚀 Como usar](#-como-usar)
- [💡 Ativar e desativar a venv](#-ativar-e-desativar-a-venv)
- [📁 Gerenciar dependências](#-gerenciar-dependências)
- [🧰 Requisitos](#-requisitos)
- [🛠️ Boas práticas](#️-boas-práticas)
- [📜 Licença](#-licença)
- [👤 Autor](#-autor)

---

## 📦 O que está incluído?

- `setup_venv.py`: Script Python para:
  - Criar o ambiente virtual `venv/`
  - Criar `.vscode/settings.json` apontando para a `venv`
  - Mostrar instruções de ativação no terminal
- Suporte a Windows, Linux e macOS
- Integração automática com VS Code

---

## 🚀 Como usar

### 1. Clone este repositório ou baixe os arquivos

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Execute o script no terminal do VS Code

```bash
python setup_venv.py
# ou
python3 setup_venv.py
```

> 💡 O VS Code será configurado para usar o Python da `venv` automaticamente.

---

## 💡 Ativar e desativar a venv

Após a criação, ative o ambiente com:

### Windows:
```bash
venv\Scripts\activate
```

### Linux / macOS:
```bash
source venv/bin/activate
```

Para desativar:
```bash
deactivate
```

---

## 📁 Gerenciar dependências

### Para instalar pacotes:
```bash
pip install nome-do-pacote
```

### Para salvar os pacotes em `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### Para instalar pacotes a partir de um `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🧰 Requisitos

- Python 3.6 ou superior
- VS Code
- Extensão oficial do Python instalada no VS Code

---

## 🛠️ Boas práticas

- Sempre use ambientes virtuais para isolar dependências.
- Mantenha seu `requirements.txt` atualizado.
- Adicione o diretório `venv/` ao `.gitignore`:
  ```bash
  echo "venv/" >> .gitignore
  ```

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

Feito com 💻 por **Francis Nascimento**  
🔗 [Meu GitHub](https://github.com/FrancisNascimentoDev)  
📧 francisn.dev@gmail.com  
🌐 [Meu Portefólio](https://francisnascimentodev.github.io/FrancisDev/)

---
