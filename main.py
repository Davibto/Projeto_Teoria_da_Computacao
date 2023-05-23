alfabetos = []
estados = []
estado_inicial = None
finais = []

#Abertura dos arquivos e leitura do alfabeto, estado, estado inicial e estados finais
def LerArquivo():
    with open("AFDcerto.txt", "r") as arquivo:
        texto = arquivo.readlines()    
    for linha in texto:
        if "alfabeto" in linha:
            alfabetos = linha.split(":")[1].split(",")
            alfabetos = [a.strip() for a in alfabetos]
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
    return alfabetos, estados, estado_inicial, finais

alfabetos, estados, estado_inicial, finais = LerArquivo() 

#Fazendo testes da matriz das transições
Raw = len(alfabetos)
Column = len(estados)
matriz_transicao = [['*' for _ in range(Raw)] for _ in range(Column)]
print(matriz_transicao)



print(alfabetos)
print(estados)
print(estado_inicial)
print(finais)

