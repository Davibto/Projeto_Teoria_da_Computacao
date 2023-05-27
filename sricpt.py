import subprocess

def abrir_arquivo_jflap(caminho_arquivo):
    try:
        subprocess.run(['jflap', caminho_arquivo])
    except FileNotFoundError:
        print("O JFLAP não foi encontrado. Certifique-se de que está instalado e configurado corretamente.")

caminho_arquivo_afd = 'caminho/do/arquivo.afd'
abrir_arquivo_jflap(caminho_arquivo_afd)