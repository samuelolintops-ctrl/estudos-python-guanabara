#=========== Desafio 27 ===========
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: ")).strip().title()
nome_split = nome.split()
nome1 = nome_split[0]
nome2 = nome_split[-1]

print(f"Primeiro nome: {nome1}\nÚltimo nome: {nome2}")
# Ou, para verificar o último nome:
# print(f"Último nome: {nome_split[len(nome_split) - 1]}")