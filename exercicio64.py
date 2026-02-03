#=========== Desafio 64 ===========
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 
# o valor 999 (que é a condição de parada/flag). No final, mostre quantos números foram digitados e qual foi a soma 
# entre eles (desconsiderando o flag).

print("\nDigite uma sequência de valores e obtenha a soma entre eles (digite 999 para encerrar):")
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Valor: "))
    if n != 999:
        soma += n
        cont += 1

print(f"Soma dos {cont} valores digitados: {soma}.")