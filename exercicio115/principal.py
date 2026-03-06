#=========== Desafio 115 ===========

# Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar
# todas as pessoas cadastradas.

from time import sleep
import utilidades
import listagem
import cadastro
from cores import colorir

# Verifica se existe um arquivo txt, se não houver cria um
nome_arq = 'lista_cad.txt'
try:
    arq = open(nome_arq, 'a')
except FileNotFoundError:
    arq = open(nome_arq, 'w')
    arq.close()
except Exception as erro:
    print(f'ERRO do tipo: {erro.__class__}')
else:
    arq.close()

# Declaração das opções ao usuário em lista
menu = [
    'Cadastrar uma nova pessoa',
    'Listar cadastrados',
    'Sair do programa'
]
qtd_opc = len(menu)
while True:
    utilidades.cabecalho('CADASTRANDO PESSOAS')
    utilidades.mostra_menu(menu)
    utilidades.imp_linha()
    while True:
        opcao = utilidades.leiaInt(colorir('Digite sua opção: ', 'cian'))
        if opcao > 0 and opcao <= qtd_opc:
            break
        print(colorir(f'Opção "{opcao}" inválida! Digite novamente.', 'verm'))
    # Início dos módulos
    if opcao == 1:
        print('Iniciando módulo de Cadastro.')
        sleep(2)
        cadastro.novo_cadastro(nome_arq)
        sleep(2)
    elif opcao == 2:
        print('Iniciando módulo de listagem.')
        sleep(2)
        listagem.listar_cadastros(nome_arq)
        sleep(2)
    else:
        print('Encerrando sistema.')
        sleep(2)
        break
print('\nFim do programa! Volte sempre!')
