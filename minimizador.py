from afd import AFD

class MinimizadorAFD:

    @staticmethod
    def minimizar(afd):
        ### Implementando o metodo de Myhill Nerode
        ## 1. Recuperando os pares de todos os estados pertencentes ao AFD
        conjunto_estados = afd.estados
        print('conjuto estados: ', conjunto_estados)
        conjunto_estados_finais = afd.finais
        print('conjunto_estados_finais: ', conjunto_estados_finais)
        estados_nao_finais = [estado for estado in conjunto_estados if estado not in conjunto_estados_finais] # Estados nao finais eh a diferenca entre os estados e os estados finais
        print('estados_nao_finais: ', estados_nao_finais)
        pares_marcados = []
        pares_nao_marcados = []

        for i in range(len(estados_nao_finais)): ## 2.Cria os pares de estados nao finais
            for j in range(i+1, len(estados_nao_finais)):
                if estados_nao_finais[i] != estados_nao_finais[j]:
                    pares_nao_marcados.append([estados_nao_finais[i], estados_nao_finais[j]])
                
        for i in range(len(afd.finais)): ## 3.Cria os pares de estados finais
            for j in range(i+1, len(afd.finais)):
                if afd.finais[i] != afd.finais[j]:
                    pares_nao_marcados.append([afd.finais[i], afd.finais[j]])

        for i in range(len(estados_nao_finais)): # 4.Cria os pares de estados marcados
            for j in range(len(afd.finais)):
                if estados_nao_finais[i] != afd.finais[j]:
                    pares_marcados.append([estados_nao_finais[i], afd.finais[j]])
                    
        print("Pares nao marcados (possiveis equivalentes):")
        print(pares_nao_marcados)
        print("Pares marcados (nao equivalentes):")
        print(pares_marcados)

        ## 5.Verificar as transicoe dos pares de estados nao marcados, ate que nao seja possivel marcar mais nenhum par
        alterou = True
        while alterou: # Enquanto houver alteracoes em pares_nao_marcados e pares_marcados, verifica os estados de pares_nao_marcados
            count = 0
            while (count < len(pares_nao_marcados)): # Percorrer o array a cada alteracao
                par = pares_nao_marcados[count]
                qi = par[0]
                qf = par[1]
                linha = len(afd.estados)
                coluna = len(afd.alfabeto)
                estado_resultado_qi = None
                estado_resultado_qf = None
                #print(qi, qf) ta pegando todos os estados

                for s in afd.alfabeto: # Verificando os estados resultantes das transicoes
                    for i in range(linha): # Linha referente ao qi na tabela de transicoes
                        if afd.transicoes_tabela[i+1][0] == qi:
                            for j in range(coluna): # Coluna referente ao simbolo s na tabela de transicoes
                                if afd.transicoes_tabela[0][j+1] == s: # Pegando as transicoes s de qi
                                    estado_resultado_qi = afd.transicoes_tabela[i+1][j+1] # Achou o primeiro estado resultante da transicao s
                                    break
                            break
                    for i in range(linha): # Linha referente ao qf na tabela de transicoes
                        if afd.transicoes_tabela[i+1][0] == qf:
                            for j in range(coluna): # Coluna referente ao simbolo s na tabela de transicoes
                                if afd.transicoes_tabela[0][j+1] == s:  # Pegando as transicoes s de qi
                                    estado_resultado_qf = afd.transicoes_tabela[i+1][j+1] # Achou o segundo estado resultante da transicao s
                                    break
                            break
                
                par_resultante = [] # Array para armazenar o resultado da transicao na tabela de transicao
                par_resultante_inverso = [] 
                par_resultante.append(estado_resultado_qi)
                par_resultante.append(estado_resultado_qf)
                par_resultante_inverso.append(estado_resultado_qf)
                par_resultante_inverso.append(estado_resultado_qi)

                if par_resultante in pares_marcados: ## 6.Caso o resultado do par esteja marcado, mudadmos o par para pares_marcados
                    print('Par resultante: ' + par_resultante[0] + par_resultante[1] + ' esta marcado')
                    print(par)
                    pares_nao_marcados.remove(par)
                    pares_marcados.append(par)
                    count = 0
                elif par_resultante_inverso in pares_marcados:
                    print('Par resultante: ' + par_resultante_inverso[0] + par_resultante_inverso[1] + ' esta marcado')
                    print(par)
                    pares_nao_marcados.remove(par)
                    pares_marcados.append(par)
                    count = 0
                else:
                    count +=1
                    if count == len(pares_nao_marcados)-1: 
                        alterou = False
            #while(i < len(pares_nao_marcados))                     

            break

        print("Pares nao marcados (possiveis equivalentes):")
        print(pares_nao_marcados)
        print("Pares marcados (nao equivalentes):")
        print(pares_marcados)

        ### STEP 4 Combine all the unmarked pairs and make them a single state in the minimized DFA.