#=========== Desafio 67 ===========

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    num = int(input("Você deseja visualisar a tabuada de qual número (digite um negativo para parar): "))
    print("-" * 80)
    if num < 0:
        break
    for i in range(1, 11):
        prod = num * i
        print(f"{num} x {i} = {prod}")
    print("-" * 80)
'''

# Outra forma de fazer, porém usando apenas o laço while
while True:
    num = int(input("Você deseja visualisar a tabuada de qual número (digite um negativo para parar): "))
    print("-" * 80)
    if num < 0:
        break
    i = 0
    while True:
        i += 1
        if i > 10:
            break
        prod = num * i
        print(f"{num} x {i} = {prod}")
    print("-" * 80)