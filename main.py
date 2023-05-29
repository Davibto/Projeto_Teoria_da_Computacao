from afd import AFD
from minimizador import MinimizadorAFD
import pygame

### Criando o AFD a partir de um .txt
## 1.Definino o arquivo que sera lido
# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDteste.txt"

## 2.Criando o AFD
afd = AFD(arquivo)
## 3.Validando o AFD
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    ### Minimizando o AFD utilizando o algoritmo de Myhill Nerode
    MinimizadorAFD().minimizar(afd)