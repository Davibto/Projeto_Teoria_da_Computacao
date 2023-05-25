from afd import AFD

# Definino o arquivo que sera lido
#arquivo = "AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDcerto.txt"

# Criando AFD
afd = AFD(arquivo) 

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

# Preenchendo a tabela de transicoes Verificando as transicoe

#Criando os pares de estados
pares_marcados = []
pares_nao_marcados = []
conjunto1 = set(afd.estados)
conjunto2 = set(afd.finais)

estados_nao_finais = list(conjunto1 - conjunto2) #cria os estados nao finais a partir da diferenca entre os estados e os estados finais

for i in range(len(estados_nao_finais)): #cria os pares de estados nao finais
    for j in range(i+1, len(estados_nao_finais)):
        if estados_nao_finais[i] != estados_nao_finais[j]:
            pares_nao_marcados.append([estados_nao_finais[i], estados_nao_finais[j]])
        
for i in range(len(afd.finais)): #cria os pares de estados finais
    for j in range(i+1, len(afd.finais)):
        if afd.finais[i] != afd.finais[j]:
            pares_nao_marcados.append([afd.finais[i], afd.finais[j]])

for i in range(len(estados_nao_finais)): #cria os pares de estados marcados
    for j in range(i, len(afd.finais)):
        if estados_nao_finais[i] != afd.finais[j]:
            pares_marcados.append([estados_nao_finais[i], afd.finais[j]])
            
print("Pares nao marcados (possiveis equivalentes):")
print(pares_nao_marcados)
print("Pares marcados (nao equivalentes):")
print(pares_marcados)

#STEP 3

