class AFD:
    
    # Cria AFD a partir de um arquivo
    def __init__(self, arquivo) -> None:
        # Descricao de um AFD 5-upla = (Σ, Q, σ, q0, F)
        self.alfabeto = [] # Σ
        self.estados = [] # Q
        self.transicoes = [] # σ
        self.estado_inicial = None  # q0
        self.finais = [] # F

        # Convertendo o arquivo .txt em afd 
        with open(arquivo, "r") as arquivo:
            texto = arquivo.readlines()         
        for linha in texto:
            if "alfabeto" in linha:
                alfabeto = linha.split(":")[1].split(",")
                self.alfabeto = [a.strip() for a in alfabeto] # Tratamento da string para remover espacos em branco
            elif "estados" in linha:
                estados = linha.split(":")[1].split(",")
                self.estados = [e.strip() for e in estados]
            elif "inicial" in linha:
                self.estado_inicial = linha.split(":")[1].strip()
            elif "finais" in linha:
                finais = linha.split(":")[1].split(",")
                self.finais = [e.strip() for e in finais]
            elif "transicoes" in linha:
                continue
            else:
                self.transicoes.append(linha.strip())
