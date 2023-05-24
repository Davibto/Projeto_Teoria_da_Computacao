# Descricao de um AFD (Σ, Q, σ, q0, F)
alfabeto = [] # Σ
estados = [] # Q
transicoes_tabela = [len(estados)][len(estados)] # σ
transicoes = [] # σ
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

        elif "estados" in linha:
            estados = linha.split(":")[1].split(",")
            estados = [e.strip() for e in estados]

        elif "inicial" in linha:
            estado_inicial = linha.split(":")[1].strip()

        elif "finais" in linha:
            finais = linha.split(":")[1].split(",")
            finais = [e.strip() for e in finais]

        elif "transicoes" in linha:
            print("chegou nas transicoes")

        else:
            transicoes.append(linha.strip())
            

    return alfabeto, estados, estado_inicial, finais, transicoes

alfabeto, estados, estado_inicial, finais, transicoes = LerArquivo(arquivo) 

# Teste da leitura do arquivo
print("Alfabeto:")
print(alfabeto)
print("Estados:")
print(estados)
print("Estado inicial:")
print("['" + estado_inicial + "']")
print("Estados finais:")
print(finais)
print("Transicoes:")
print(transicoes)

# Teste da matriz que contem o resultado das funcoes de transições
row = len(alfabeto)
column = len(estados)
matriz_transicao = [['*' for _ in range(row)] for _ in range(column)]
print(matriz_transicao)