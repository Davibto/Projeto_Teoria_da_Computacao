class AFD:

    def __init__(self, arquivo) -> None: # Cria AFD a partir de um arquivo
        # Descricao de um AFD 5-upla = (Σ, Q, σ, q0, F)
        self.alfabeto = [] # Σ
        self.estados = [] # Q
        self.transicoes = [] # σ
        self.estado_inicial = None  # q0
        self.finais = [] # F
        self.transicoes_tabela = [len(self.estados)][len(self.estados)] #σ

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
                pass
            else:
                self.transicoes.append(linha.strip())

        # Criando a matriz/tabela da funcao de transições
        linha = len(self.estados)
        coluna = len(self.alfabeto)
        # Atribuindo None nas transicoes, caso no final do processo a transicao nao exista, o espaco estara none
        self.transicoes_tabela = [[None for _ in range(coluna +1)] for _ in range(linha +1)]
        for i in range(linha):
            self.transicoes_tabela[i+1][0] = self.estados[i]
        for i in range(coluna):
            self.transicoes_tabela[0][i+1] = self.alfabeto[i]

    def valido(self): # Verifica se o AFD e valido
        if self.estado_inicial == '': # Se nao tem estado inicial, nao e AFD
            print('Se nao tem estado inicial, nao e AFD.')
            return False
        else:
            linha = len(self.estados)
            coluna = len(self.alfabeto)

            for transicao in self.transicoes:
                qi = transicao.split(',')[0]
                qf = transicao.split(',')[1]
                s = transicao.split(',')[2]

                if (qi not in self.estados) or (qf not in self.estados) or (s not in self.alfabeto):
                    print('Um ou mais estados na lista de transicao nao pertence ao AFD ou simbolo da transicao nao pertence ao alfabeto compreendido pelo AFD.')
                    return False # Estado nao pertence ao AFD ou simbolo da transicao nao pertence ao alfabeto compreendido pelo AFD
                
                for i in range(linha): # Todo estado tem uma transicao para cada simbolo
                    if self.transicoes_tabela[i+1][0] == qi:
                        for j in range(coluna):
                            if self.transicoes_tabela[0][j+1] == s:
                                if self.transicoes_tabela[i+1][j+1] != None: # Tem mais de uma transicao com o mesmo simbolo saindo do estado
                                    print(self.transicoes_tabela[i+1][j+1]);
                                    print('Tem mais de uma transicao com o mesmo simbolo saindo do estado.')
                                    return False
                                elif self.transicoes_tabela[0][j+1] == s:
                                    self.transicoes_tabela[i+1][j+1] = qf
                                break
                        break

 
        return self.verificar_elementos_matriz(self.transicoes_tabela)
            
    def verificar_elementos_matriz(self, matriz): # Retorna False caso haja mais de um elemento None na tabela de transicoes
        contador = 0
        for linha in matriz:
            for elemento in linha:
                if elemento is None:
                    contador += 1
        if contador == 1:
            return True
        else:
            return False