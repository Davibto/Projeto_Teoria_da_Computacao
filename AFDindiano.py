from afd import AFD
from minimizador import MinimizadorAFD
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

### Criando o AFD a partir de um .txt
## 1.Definino o arquivo que sera lido
# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDindiano.txt"

## 2.Criando o AFD
afd = AFD(arquivo)
## 3.Validando o AFD
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    # afd = afd.afd_para_visual_dfa(afd.estados, afd.estado_inicial, afd.finais, afd.transicoes_tabela);
    # visual_dfa = VisualDFA(afd)
    # visual_dfa.show_diagram(view=True)
    
    ### Minimizando o AFD utilizando o algoritmo de Myhill Nerode
    MinimizadorAFD().minimizar(afd)
    afd = afd.afd_para_visual_dfa(MinimizadorAFD().estados_novos, MinimizadorAFD().inicial_novo,  MinimizadorAFD().finais_novos, MinimizadorAFD().tabela_transicoes_nova)
    visual_dfa = VisualDFA(afd)
    visual_dfa.show_diagram(view=True)