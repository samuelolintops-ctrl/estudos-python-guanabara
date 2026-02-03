#=========== Desafio 42 ===========
# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

n1 = float(input("Digite o comprimento da primeira reta: "))
n2 = float(input("Digite o comprimento da segunda reta: "))
n3 = float(input("Digite o comprimento da terceira reta: "))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print("É POSSÍVEL formar um triângulo com as medidas dadas. Se trata de um triângulo: ", end = '')
    if n1 == n2 and n1 == n3:
        print("\033[32mEQUILÁTERO\033[m.")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("\033[36mISÓSCELES\033[m.")
    else:
        print("\033[33mESCALENO\033[m.")
else:
    print("NÃO É POSSÍVEL formar um triângulo com as medidas dadas.")