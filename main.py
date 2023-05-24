# Descricao de um AFD (Σ, Q, σ, q0, F)

alfabeto = [] # Σ
estados = [] # Q
transicoes = [len(estados)][len(estados)] # σ
estado_inicial = None  # q0
finais = [] # F

# Definino o arquivo que sera lido
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDcerto.txt"

# Funcao para ler e mapear o arquivo .txt 
def LerArquivo(arquivo):
    with open(arquivo, "r") as arquivo:
        texto = arquivo.readlines()
                
    for linha in texto:
        if "alfabeto" in linha:
            alfabeto = linha.split(":")[1].split(",")
            alfabeto = [a.strip() for a in alfabeto] # Tratamento da string para remover espacos em branco

    for linha in texto:
        if "estados" in linha:
            estados = linha.split(":")[1].split(",")
            estados = [e.strip() for e in estados]

    for linha in texto:
        if "inicial" in linha:
            estado_inicial = linha.split(":")[1].strip()

    for linha in texto:
        if "finais" in linha:
            finais = linha.split(":")[1].split(",")
            finais = [e.strip() for e in finais]

    return alfabeto, estados, estado_inicial, finais

alfabeto, estados, estado_inicial, finais = LerArquivo(arquivo) 

print("Alfabeto:")
print(alfabeto)
print("Estados:")
print(estados)
print("Estado inicial:")
print("['" + estado_inicial + "']")
print("Estados finais:")
print(finais)

#Fazendo testes da matriz das transições
Raw = len(alfabeto)
Column = len(estados)
matriz_transicao = [['*' for _ in range(Raw)] for _ in range(Column)]
print(matriz_transicao)