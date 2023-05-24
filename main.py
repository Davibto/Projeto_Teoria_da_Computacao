from afd import AFD

# Definino o arquivo que sera lido
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDerrado.txt"

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
print("Tabela de transicoes:")
print(afd.valido())
print(afd.transicoes_tabela);

# Preenchendo a tabela de transicoes Verificando as transicoe