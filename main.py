from afd import AFD

# Definino o arquivo que sera lido
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDcerto.txt"

# Criando AFD
afd = AFD(arquivo) 

# Teste da leitura do arquivo
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

# Criando a matriz/tabela da funcao de transições
row = len(afd.alfabeto)
column = len(afd.estados)
transicoes_tabela = [[None for _ in range(row)] for _ in range(column)]
print(transicoes_tabela)

# Preenchendo a tabela de transicoes Verificando as transicoe