class AFD:

    # Cria AFD a partir de um arquivo
    def __init__(self, arquivo) -> None:
        # Descricao de um AFD 5-upla = (Σ, Q, σ, q0, F)
        self.alfabeto = [] # Σ
        self.estados = [] # Q
        self.transicoes = [] # σ
        self.estado_inicial = None  # q0
        self.finais = [] # F
        self.transicoes_tabela = [len(self.estados)][len(self.estados)] # σ

        # Convertendo o arquivo .txt em afd 
        with open(arquivo, 'r') as arquivo:
            texto = arquivo.readlines()         
        for linha in texto:
            if 'alfabeto' in linha:
                alfabeto = linha.split(':')[1].split(',')
                self.alfabeto = [a.strip() for a in alfabeto] # Tratamento da string para remover espacos em branco
            elif 'estados' in linha:
                estados = linha.split(':')[1].split(',')
                self.estados = [e.strip() for e in estados]
            elif 'inicial' in linha:
                self.estado_inicial = linha.split(':')[1].strip()
            elif 'finais' in linha:
                finais = linha.split(':')[1].split(',')
                self.finais = [e.strip() for e in finais]
            elif 'transicoes' in linha:
                continue
            else:
                self.transicoes.append(linha.strip())

    def valida_afd(self):    
        # Criando a matriz/tabela da funcao de transições
        linha = len(self.alfabeto)
        coluna = len(self.estados)
        # Atribuindo None nas transicoes, caso no final do processo a transicao nao exista, o espaco estara none
        self.transicoes_tabela = [[None for _ in range(linha)] for _ in range(coluna)]

        for transicao in self.transicoes:
            qi = transicao.split(',')[0]
            qf = transicao.split(',')[1]
            s = transicao.split(',')[2]
            print(qi + ' -' + s +'-> ' + qf)
