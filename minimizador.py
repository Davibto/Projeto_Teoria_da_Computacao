from afd import AFD

class MinimizadorAFD:

    @staticmethod
    def minimizar(afd):
        ### Implementando o metodo de Myhill Nerode
        ## 1. Criando os pares de todos os estados pertencentes ao AFD
        conjunto_estados = set(afd.estados)
        conjunto_estados_finais = set(afd.finais)
        # Estados nao finais e a diferenca entre os conjunto de estados e conjunto de estados finais
        estados_nao_finais = list(conjunto_estados - conjunto_estados_finais)

        pares_marcados = []
        pares_nao_marcados = []

        for i in range(len(estados_nao_finais)): # Cria os pares de estados nao finais
            for j in range(i+1, len(estados_nao_finais)):
                if estados_nao_finais[i] != estados_nao_finais[j]:
                    pares_nao_marcados.append([estados_nao_finais[i], estados_nao_finais[j]])
                
        for i in range(len(afd.finais)): # Cria os pares de estados finais
            for j in range(i+1, len(afd.finais)):
                if afd.finais[i] != afd.finais[j]:
                    pares_nao_marcados.append([afd.finais[i], afd.finais[j]])

        for i in range(len(estados_nao_finais)): #cria os pares de estados marcados
            for j in range(len(afd.finais)):
                if estados_nao_finais[i] != afd.finais[j]:
                    pares_marcados.append([estados_nao_finais[i], afd.finais[j]])
                    
        print("Pares nao marcados (possiveis equivalentes):")
        print(pares_nao_marcados)
        print("Pares marcados (nao equivalentes):")
        print(pares_marcados)

        ### 2.Verificar as transicoe dos pares de estados nao marcados, ate que nao seja possivel marcar mais nenhum par
        alterou = True;
        while (alterou): # Enquanto houverem alteracoes em pares_nao_marcados e em pares_marcados
            for par in pares_nao_marcados:
                qi = par[0]
                qf = par[1]
                print('Par: ' + qi, qf)
                linha = len(afd.estados)
                coluna = len(afd.alfabeto)
                estado_resultado_qi = None
                estado_resultado_qf = None
                
                for s in afd.alfabeto: # Verificando os estados resultantes das transicoes
                    for i in range(linha): # Coluna referente ao qi na tabela de transicoes
                        if afd.transicoes_tabela[i+1][0] == qi:
                            for j in range(coluna):
                                if afd.transicoes_tabela[0][j+1] == s: # Pegando as transicoes s de qi
                                    estado_resultado_qi = afd.transicoes_tabela[i+1][j+1] # Achou o primeiro estado resultante da transicao s
                                    break
                            break
                    
                    for i in range(linha): # Pegando o resultado da transicao s do segundo estado
                        if afd.transicoes_tabela[i+1][0] == qf:
                            for j in range(coluna):
                                if afd.transicoes_tabela[0][j+1] == s: 
                                    estado_resultado_qf = afd.transicoes_tabela[i+1][j+1] # Achou o segundo estado resultante da transicao s
                                    
                                    print('Resultado transicao ' + s + ':' + estado_resultado_qi, estado_resultado_qf)
                                    par_resultante = [] # Array para armazenar o resultado da transicao na tabela de transicao
                                    par_resultante.append(estado_resultado_qi)
                                    par_resultante.append(estado_resultado_qf)
                                    
                                    if (par_resultante in pares_marcados) and (par in pares_nao_marcados):
                                        print('Par resultante: ' + par_resultante[0] + par_resultante[1] + ' esta marcado')
                                        print(par)
                                        pares_nao_marcados.remove(par)
                                        pares_marcados.append(par)
                                        MinimizadorAFD.minimizar(afd)
                                        break
                                    else:
                                        alterou = False
                                        break
                            break

        print("Pares nao marcados (possiveis equivalentes):")
        print(pares_nao_marcados)
        print("Pares marcados (nao equivalentes):")
        print(pares_marcados)

        ### STEP 4 Combine all the unmarked pairs and make them a single state in the minimized DFA.