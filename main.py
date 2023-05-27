from afd import AFD
from minimizador import MinimizadorAFD
import pygame

### Criando o AFD a partir de um .txt
## 1.Definino o arquivo que sera lido
# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDcerto.txt"

## 2.Criando o AFD
afd = AFD(arquivo)
## 3.Validando o AFD
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    ### Minimizando o AFD utilizando o algoritmo de Myhill Nerode
    MinimizadorAFD().minimizar(afd)

    ### Desenhando o AFD minimizado utilizando pygame
    pygame.init() ## 1.Iniciando o pyagme
    tela = pygame.display.set_mode((1080, 720)) ## 2.Criando a tela

    # 3. Mudando o titulo e logo da tela
    pygame.display.set_caption('Minimizador de AFD')
    # icone = pygame.image.load('') # 32x32 pixels
    # pygame.display.set_icon(icone) 

    executando = True

    while executando: ## 3.Toda a parte grafica sera executada dentro deste loop do programa, isso inclui desenhos do AFD e captura de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: ## 4.Evento para fechar a tela
                executando = False
        tela.fill((255, 255, 255)) # Mudando a cor da tela (RGB) -> tela branca
        pygame.display.update() # Atualizando a tela