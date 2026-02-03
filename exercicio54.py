#=========== Desafio 54 ===========
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não 
# atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
print("\n")
cont_men = 0
cont_mai = 0
for i in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    if (ano_atual - nasc) < 18:
        cont_men += 1
    else:
        cont_mai += 1
print(f"\nQuantidade de pessoas maiores de idade: {cont_mai}\nQuantidade de pessoas menores de idade: {cont_men}")