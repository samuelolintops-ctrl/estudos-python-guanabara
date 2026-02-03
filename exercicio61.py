#=========== Desafio 61 ===========
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
# usando a estrutura while.

# (Desafio 51) Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No 
# final, mostre os 10 primeiros termos dessa progressão.

print("\nDescobrindo os 10 primeiros termos de uma P.A.:")
prim_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = 0
num = 0
while num < 10:
    pa = prim_termo + razao * num
    print(f"{pa} ", end = '')
    print('-> ' if num < 9 else '', end = '')
    num += 1

'''
# Alternativa para deixar o código mais limpo:
termo = prim_termo
cont = 1
while cont <= 10:
    print(f"{termo} ", end="")
    termo += razao  # O próximo termo é o atual + razão
    cont += 1
'''
