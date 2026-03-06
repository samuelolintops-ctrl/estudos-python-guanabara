#=========== Desafio 91 ===========

# Crie um programa onde 4 jogadores joguem um dado (randint) e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
qtd_jogadores = 4
for c in range(1, qtd_jogadores + 1):
    nome = str(input(f'Nome do {c}º jogador: ')).strip().lower()
    jogada =  randint(1, 6)
    jogadores[f'{nome}'] = jogada
for k, v in jogadores.items():
    print(f'O jogador {k.title()} tirou {v} no dado.')
    sleep(1)
result_jogo = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=' * 40)
print(f'{"RANKING FINAL":^40}')
print('=' * 40)
for ind, val in enumerate(result_jogo):
    print(f' => {ind + 1}º LUGAR: {val[0].title()} tirando {val[1]}')
    sleep(0.5)
