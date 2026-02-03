#=========== Desafio 63 ===========
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma 
# Sequência de Fibonacci. (Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8). F(n) = F(n-1) + F(n-2)

# Minha resolução:
# Usei a lista a meu favor e a sequência de Fibonacci preenche a lista de acordo com a quantidade de termos 
# informada pelo usuário

print("\nDigite um valor para n para os primeiros n elementos da Sequência de Fibonacci.")
n = int(input("Valor de n: "))
lista = [0, 1]
cont = 2
while cont < n:
    lista.append(lista[cont - 1] + lista[cont - 2])
    cont += 1
print(lista)

# Outra forma de se fazer sem usar lista:
print("\nDigite um valor para n para os primeiros n elementos da Sequência de Fibonacci.")
n = int(input("Valor de n: "))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end = '')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}' if cont <= n else f' {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
