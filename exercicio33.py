#=========== Desafio 33 ===========
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Digite 3 números:")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
maior = n1
menor = n1

if n2 > maior and n2 > n3:
    maior = n2
if n3 > maior and n3 > n2:
    maior = n3
if n2 < menor and n2 < n3:
    menor = n2
if n3 < menor and n3 < n2:
    menor = n3

print(f"O maior número digitado foi: {maior}\nO menor número digitado foi: {menor}.")