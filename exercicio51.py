#=========== Desafio 51 ===========
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 
# 10 primeiros termos dessa progressão.

print("\n")
num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da P.A.: "))
print(f"Termo 1: {num}")
for i in range(2, 11):
    num += razao
    print(f"Termo {i}: {num}")

'''
Outra forma de fazer exercício seria usando a fórmula matemática a_n = a_1 + (n-1) . r

print("\n")
num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da P.A.: "))
decimo = num + (10 - 1) * razao
for i in range(num, decimo + razao, razao):
    print(f" {i} ", end = " ")

'''

