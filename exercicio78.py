#=========== Desafio 78 ===========

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas 
# respectivas posições na lista.

print('\nDigite 5 valores')
limite = 5
lista = []
for i in range(0, limite):
    lista.append(int(input(f'Valor na posição {i}: ')))

maior = max(lista)
menor = min(lista)
pos_mai = []
pos_men = []

for ind, val in enumerate(lista):
    if val == maior:
        pos_mai.append(ind)
    if val == menor:
        pos_men.append(ind)

print(f'\nO maior valor digitado foi {maior}, na(s) posição(ões) ', end = '')
for i in pos_mai:
    print(f'{i}...', end = '')
print(f'\nO menor valor digitado foi {menor}, na(s) posição(ões) ', end = '')
for i in pos_men:
    print(f'{i}...', end = '')
