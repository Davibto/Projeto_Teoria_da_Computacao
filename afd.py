class AFD:

    def __init__(self, arquivo) -> None: #Cria AFD a partir de um arquivo
        #Descricao de um AFD 5-upla = (Σ, Q, σ, q0, F)
        self.alfabeto = [] #Σ
        self.estados = [] #Q
        self.transicoes = [] #σ
        self.estado_inicial = None  #q0
        self.finais = [] #F
        self.transicoes_tabela = [len(self.estados)][len(self.estados)] #σ

        #Convertendo o arquivo .txt em afd 
        with open(arquivo, 'r') as arquivo:
            texto = arquivo.readlines()         
        for linha in texto:
            if 'alfabeto' in linha:
                alfabeto = linha.split(':')[1].split(',')
                self.alfabeto = [a.strip() for a in alfabeto] #Tratamento da string para remover espacos em branco
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

    def valido(self): #Verifica se o AFD e valido
        if (self.estado_inicial == '') or (self.finais == ''): #Se nao tem estado inicial ou final, nao e AFD
            return False
        
        #Criando a matriz/tabela da funcao de transições
        coluna = len(self.estados)
        linha = len(self.alfabeto)
        #Atribuindo None nas transicoes, caso no final do processo a transicao nao exista, o espaco estara none
        self.transicoes_tabela = [[None for _ in range(linha +1)] for _ in range(coluna +1)]
        for i in range(coluna):
            self.transicoes_tabela[i+1][0] = self.estados[i]
        for i in range(linha):
            self.transicoes_tabela[0][i+1] = self.alfabeto[i]

        for transicao in self.transicoes:
            qi = transicao.split(',')[0]
            qf = transicao.split(',')[1]
            s = transicao.split(',')[2]

            if (qi not in self.estados) or (qf not in self.estados): #Transicao de um estado que nao pertence ao AFD
                return False
            elif s not in self.alfabeto: #Simbolo da transicao nao pertence ao alfabeto compreendido pelo AFD
                return False
            
            #Todo estado tem uma transicao para cada simbolo
            if self.transicoes_tabela[1][0] == qi:
                pass
            print(qi + ' -' + s +'-> ' + qf)
            
