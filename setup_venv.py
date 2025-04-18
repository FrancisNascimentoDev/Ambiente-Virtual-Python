"""
Este script cria um ambiente virtual Python e configura o VS Code para usá-lo.
Ele deve ser executado no diretório do projeto onde você deseja criar o ambiente virtual.
O script também fornece instruções para ativar o ambiente virtual no terminal do VS Code.
Certifique-se de ter o Python instalado e acessível no PATH do sistema.
Para executar o script, você pode usar o seguinte comando no terminal:
 python setup_venv.py

"""

import os
import sys
import subprocess
import platform

# Função para criar o ambiente virtual
def criar_venv():
    print("📦 Criando ambiente virtual...")
    # Chama o comando para criar o ambiente virtual
    subprocess.run([sys.executable, "-m", "venv", "venv"])

# Função para configurar o VS Code para usar o Python da venv
def configurar_vscode():
    print("🛠️ Configurando VS Code para usar a venv...")
    # Cria a pasta .vscode se não existir
    os.makedirs(".vscode", exist_ok=True)
    # Define o caminho do Python dentro do ambiente virtual, considerando o sistema operacional
    path = os.path.abspath("venv/Scripts/python.exe" if platform.system() == "Windows" else "venv/bin/python3")
    # Cria ou sobrescreve o arquivo settings.json do VS Code com o caminho do Python da venv
    with open(".vscode/settings.json", "w") as f:
        f.write(f'''{{
    "python.pythonPath": "{path}"
}}''')

# Função para mostrar a mensagem de sucesso e instruções para ativar o ambiente
def ativar_msg():
    print("\n✅ Ambiente virtual criado com sucesso!")
    print("Abra o terminal do VS Code e ative com:")
    # Dependendo do sistema operacional, fornece o comando correto para ativar a venv
    if platform.system() == "Windows":
        print("venv\\Scripts\\activate")
    else:
        print("source venv/bin/activate")
    print("\nOu apenas feche e reabra o terminal do VS Code, ele deve reconhecer automaticamente.")

# Bloco principal que chama as funções para criar a venv e configurar o VS Code
if __name__ == "__main__":
    criar_venv()        # Cria o ambiente virtual
    configurar_vscode() # Configura o VS Code para usar o ambiente virtual
    ativar_msg()        # Mostra mensagem de sucesso e instruções de ativação
# Fim do código



