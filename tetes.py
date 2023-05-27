from afd import AFD
import pyautogui
import time
from minimizador import MinimizadorAFD

# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDindiano.txt"

afd = AFD(arquivo)
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    # print("Alfabeto:")
    # print(afd.alfabeto)
    # print("Estados:")
    # print(afd.estados)
    # print("Estado inicial:")
    # print("['" + afd.estado_inicial + "']")
    # print("Estados finais:")
    # print(afd.finais)
    # print("Transicoes:")
    # print(afd.transicoes)
    # print("Tabela de transicoes:")
    # print(afd.valido())
    # print(afd.transicoes_tabela);

    MinimizadorAFD().minimizar(afd)

def abrir_arquivo_jflap(caminho_arquivo):
    pyautogui.press('win')
    pyautogui.write('jflap7.1')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(10)

    # Abre o arquivo no JFLAP
    pyautogui.hotkey('ctrl', 'o')
    pyautogui.write(caminho_arquivo)
    pyautogui.press('enter')

caminho_arquivo_afd = 'C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/teste.jff'
abrir_arquivo_jflap(caminho_arquivo_afd)