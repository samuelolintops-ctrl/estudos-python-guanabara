#=========== Desafio 74 ===========

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e 
# o maior valor que estão na tupla.

from random import randint

# Como eu fiz: 
'''
lista = []
for i in range(0, 5):
    lista.append(randint(0, 50))

tupla = (lista[0], lista[1], lista[2], lista[3], lista[4])
'''

# Como o Guanabara fez:
tupla = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), 
         randint(0, 50))

print(f'Números gerados: {tupla}')

tupla_ordenada = sorted(tupla)
print(f'Menor valor: {tupla_ordenada[0]}')
print(f'Maior valor: {tupla_ordenada[-1]}')
