#=========== Desafio 49 ===========
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço 
# for.

# (Desafio 009): Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input("Digite um número inteiro para descobrir sua tabuada: "))
print(f"Tabuada do {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")