#=========== Desafio 05 ===========
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
num = int(input("Digite um número inteiro: "))
ant = num - 1
suc = num + 1
print(f"O valor lido foi: {num}")
print(f"Antecessor: {ant}; Sucessor: {suc}")