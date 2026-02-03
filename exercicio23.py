#=========== Desafio 23 ===========
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input("Digite um número de 0 a 9999: "))
num = num.strip()
num = ["000", num]
num = ''.join(num)

print(f"""Unidade:{num[-1]}
Dezena:{num[-2]}
Centena:{num[-3]}
Milhar:{num[-4]}""") # Quando coloco um número negativo no índice, é lido o caracter de trás pra frente contando de acordo o número informado

# Solução usando lógica matemática:
num = int(input("Digite um número de 0 a 9999: "))
print(f"""Unidade:{((num % 1000) % 100) % 10}
Dezena:{(num % 100) // 10}
Centena:{(num % 1000) // 100}
Milhar:{num // 1000}""")