#=========== Desafio 55 ===========
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print("\n")
peso = float(input("Digite o peso da pessoa 1 em kg: "))
mai = peso
men = peso
for i in range(2, 6):
    peso = float(input(f"Digite o peso da pessoa {i} em kg: "))
    if peso > mai:
        mai = peso
    if peso < men:
        men = peso
print(f"Maior peso: {mai}\nMenor peso: {men}")