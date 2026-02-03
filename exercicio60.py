#=========== Desafio 60 ===========
# Faça um programa que leia um número qualquer e mostre o seu fatorial. (Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120).


orig = int(input("\nDigite um valor para calcular seu fatorial: "))
num = orig
fat = 1

while num > 0:
    print(num, end = "")
    print(" x " if num > 1 else " = ", end = "")
    fat *= num
    num -= 1

print(fat)

# No python, na biblioteca math, tem uma função chamada factorial que já calcula o fatorial de um número
# Para o fatorial de 5, por exemplo:
# fat = factorial(5)

# Nesse exercício, como conhecemos o limite, é possível resolvê-lo usando o laço for:

orig = int(input("\nDigite um valor para calcular seu fatorial: "))
num = orig
fat = 1

for i in range(num, 0, -1):
    print(i, end = '')
    print(' x ' if i > 1 else ' = ', end = '')
    fat *= i

print(fat)
