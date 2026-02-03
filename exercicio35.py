#=========== Desafio 35 ===========
# Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.

n1 = float(input("Digite o comprimento da primeira reta: "))
n2 = float(input("Digite o comprimento da segunda reta: "))
n3 = float(input("Digite o comprimento da terceira reta: "))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print("É POSSÍVEL formar um triângulo com as medidas dadas.")
else:
    print("NÃO É POSSÍVEL formar um triângulo com as medidas dadas.")