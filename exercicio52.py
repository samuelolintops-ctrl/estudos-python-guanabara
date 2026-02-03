#=========== Desafio 52 ===========
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("\n")
cont = 0
num = int(input("Digite um número inteiro para descobrir se ele é primo ou não: "))
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
if cont == 2:
    print(f"{num} é PRIMO.")
else:
    print(f"{num} NÃO é PRIMO.")