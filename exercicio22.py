#=========== Desafio 22 ===========
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome maiúsculo: {nome.upper()}")
print(f"Seu nome minúsculo: {nome.lower()}")

nome_split = nome.split()
print(f"Quantidade de letras no seu nome: {len(''.join(nome_split))}") # ou: print(f"Quantidade de letras no seu nome: {len(nome) - nome.count(' ')}")
print(f"Quantidade de letras no seu primeiro nome: {len(nome_split[0])}")