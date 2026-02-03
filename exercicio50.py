#=========== Desafio 50 ===========
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o 
# valor digitado for ímpar, desconsidere-o.

soma_par = 0
cont_par = 0
print("\n")
for i in range(0, 6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma_par += num
        cont_par += 1
print(f"\nQuantidade de pares digitados: {cont_par}\nSoma dos pares digitados: {soma_par}")