#=========== Desafio 09 ===========
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input("Digite um número inteiro para descobrir sua tabuada: "))

print(f"{num} x 1 = {num}\n{num} x 2 = {num * 2}\n{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}\n{num} x 5 = {num * 5}\n{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}\n{num} x 8 = {num * 8}\n{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

# Outra forma de fazer esses prints:
'''
print(f"""{num} x 1 = {num}\n{num} x 2 = {num * 2}\n{num} x 3 = {num * 3}
{num} x 4 = {num * 4}\n{num} x 5 = {num * 5}\n{num} x 6 = {num * 6}
{num} x 7 = {num * 7}\n{num} x 8 = {num * 8}\n{num} x 9 = {num * 9}
{num} x 10 = {num * 10}""")
'''