from afd import AFD
from minimizador import MinimizadorAFD
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA


# Arquivo = "cd.. /AFDs/AFDteste.txt"
arquivo = "C:/Users/arthu/Vscode/Python/MinimizadorAFD/Projeto_Teoria_da_Computacao/AFDs/AFDcerto.txt"

afd = AFD(arquivo)
afd_valido = afd.valido()

if afd_valido == False:
    print('Nao foi possivel gerar um AFD a partir do arquivo dado.')

else:
    MinimizadorAFD().minimizar(afd)
    afd = afd.afd_para_visual_dfa(MinimizadorAFD().estados_novos, MinimizadorAFD().inicial_novo,  MinimizadorAFD().finais_novos, MinimizadorAFD().tabela_transicoes_nova)
    visual_dfa = VisualDFA(afd)
    visual_dfa.show_diagram(view=True)