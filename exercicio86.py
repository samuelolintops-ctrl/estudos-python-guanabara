#=========== Desafio 86 ===========

# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final, mostre a matriz na tela, com a formatação 
# correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('=' * 40, '\n' f'{"Gerador de matriz 3x3:":^40}', '\n' + '=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Valor na posição [{i}][{j}]: '))
print('\nMatriz gerada:')
for i in range(0, 3):
    print('| ', end='')
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end=' ')
    print('|')
