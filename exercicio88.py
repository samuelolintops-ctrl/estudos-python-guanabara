#=========== Desafio 88 ===========

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
print('=' * 30)
print(f'{"JOGANDO NA MEGA SENA":^30}')
print('=' * 30)
qtd_jogos = int(input('Quantos jogos você fará? '))
cartelas = []
for i in range(0, qtd_jogos):
    temporario = []
    while len(temporario) < 6:
        num = randint(1, 60)
        if num not in temporario:
            temporario.append(num)
    cartelas.append(temporario[:])
print('=' * 30)
print(f'{"SEUS JOGOS":^30}')
print('=' * 30)
for ind, val in enumerate(cartelas):
    cartelas[ind].sort()
    print(f'{ind + 1}º Cartela: ', end='')
    for n in val:
        print(f'{n:^4}', end='')
    print()
