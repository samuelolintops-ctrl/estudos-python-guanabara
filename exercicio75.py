#=========== Desafio 75 ===========

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma 
# tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('\nDigite 4 valores:')
'''
# Como eu fiz:
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))
tupla = (n1, n2, n3, n4)
'''

# Como o Guanabara fez:
tupla = (int(input('\nPrimeiro valor: ')),
        int(input('Segundo valor: ')),
        int(input('Terceiro valor: ')),
        int(input('Quarto valor: ')))

contagem_9 = tupla.count(9)
print(f'\nO 9 apareceu {contagem_9} vez(es).')

if tupla.count(3) > 0:
    posicao_3 = tupla.index(3)
    print(f'Posição em que foi digitado o primeiro valor 3: {posicao_3}.')
else:
    print('Nenhum 3 digitado.')

pares = [i for i in tupla if i % 2 ==0]
if len(pares) < 0:
    print('Nenhum número par digitado.')
else:
    print('Pares digitados: ', end = '')
    for p in pares:
        print(p, end = ' ')
