from afd import AFD

## Criando o AFD a partir de um .txt
## 1.Definino o arquivo que sera lido
# Arquivo = "AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDcerto.txt"

## 2.Criando o AFD
afd = AFD(arquivo)
## 3.Validando o AFD
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')
else:
    # Teste da leitura do arquivo
    """print("Alfabeto:")
    print(afd.alfabeto)
    print("Estados:")
    print(afd.estados)
    print("Estado inicial:")
    print("['" + afd.estado_inicial + "']")
    print("Estados finais:")
    print(afd.finais)
    print("Transicoes:")
    print(afd.transicoes)
    print("Tabela de transicoes:")
    print(afd.valido())
    print(afd.transicoes_tabela);"""

    ### Implementando o metodo de Myhill Nerode
    ## 1. Criando os pares de todos os estados pertencentes ao AFD
    conjunto_estados = set(afd.estados)
    conjunto_estados_finais = set(afd.finais)
    # Estados nao finais e a diferenca entre os conjunto de estados e conjunto de estados finais
    estados_nao_finais = list(conjunto_estados - conjunto_estados_finais)

    pares_marcados = []
    pares_nao_marcados = []

    for i in range(len(estados_nao_finais)): # Cria os pares de estados nao finais
        for j in range(i+1, len(estados_nao_finais)):
            if estados_nao_finais[i] != estados_nao_finais[j]:
                pares_nao_marcados.append([estados_nao_finais[i], estados_nao_finais[j]])
            
    for i in range(len(afd.finais)): # Cria os pares de estados finais
        for j in range(i+1, len(afd.finais)):
            if afd.finais[i] != afd.finais[j]:
                pares_nao_marcados.append([afd.finais[i], afd.finais[j]])

for i in range(len(estados_nao_finais)): #cria os pares de estados marcados
    for j in range(len(afd.finais)):
        if estados_nao_finais[i] != afd.finais[j]:
            pares_marcados.append([estados_nao_finais[i], afd.finais[j]])
            
print("Pares nao marcados (possiveis equivalentes):")
print(pares_nao_marcados)
print("Pares marcados (nao equivalentes):")
print(pares_marcados)

    ### STEP 3 if !alterou: end
    # while (!alterou) inicialmente False
    # for percorrer pares_nao_marcados, pega string[0] e string[1], buscar o resultado da transicao na tabela de transicao
    # if resultado da transicao in pares_marcados: pares_marcados.append(string) -> i = 0
    # else:
    #  alterou = True

    ### STEP 4 Combine all the unmarked pairs and make them a single state in the minimized DFA.