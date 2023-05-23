alfabetos = []
estados = []
estado_inicial = None
finais = []
transicoes = [estados][estados]

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
for linha in texto:
    if "transicoes" in linha:
        finais = linha.split(":")[1].split(",")
        finais = [e.strip() for e in finais]

print(alfabetos)
print(estados)
print(estado_inicial)
print(finais)

