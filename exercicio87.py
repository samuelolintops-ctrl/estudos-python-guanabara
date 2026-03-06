#=========== Desafio 87 ===========

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_3_coluna = 0
print('=' * 40, '\n' f'{"Gerador de matriz 3x3:":^40}', '\n' + '=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Valor na posição [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]
        if j == 2:
            soma_3_coluna += matriz[i][j]
for i in range(0, 3):
    print('|', end='')
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end='')
    print('|')
print(f'\nSoma de todos os pares digitados: {soma_par}')
print(f'Soma dos valores da terceira coluna: {soma_3_coluna}')
maior_2_linha = max(matriz[1])
print(f'O maior valor da segunda linha: {maior_2_linha}')
