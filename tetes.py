from afd import AFD

# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDcerto.txt"

afd = AFD(arquivo)
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    print("Alfabeto:")
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
    print(afd.transicoes_tabela);

    conjunto_estados = set(afd.estados)
    conjunto_estados_finais = set(afd.finais)
    estados_nao_finais = list(conjunto_estados - conjunto_estados_finais)
    pares_marcados = []
    pares_nao_marcados = []

    for i in range(len(estados_nao_finais)):
        for j in range(i+1, len(estados_nao_finais)):
            if estados_nao_finais[i] != estados_nao_finais[j]:
                pares_nao_marcados.append([estados_nao_finais[i], estados_nao_finais[j]])
            
    for i in range(len(afd.finais)):
        for j in range(i+1, len(afd.finais)):
            if afd.finais[i] != afd.finais[j]:
                pares_nao_marcados.append([afd.finais[i], afd.finais[j]])

    for i in range(len(estados_nao_finais)):
        for j in range(len(afd.finais)):
            if estados_nao_finais[i] != afd.finais[j]:
                pares_marcados.append([estados_nao_finais[i], afd.finais[j]])
                
    print("Pares nao marcados (possiveis equivalentes):")
    print(pares_nao_marcados)
    print("Pares marcados (nao equivalentes):")
    print(pares_marcados)