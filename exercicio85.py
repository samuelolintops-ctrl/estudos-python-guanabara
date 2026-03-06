#=========== Desafio 85 ===========

# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e 
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

limite = 7
lista_principal = [[], []]
for i in range(1, limite + 1):
    num = int(input(f'{i}º valor: '))
    if num % 2 == 0:
        lista_principal[0].append(num)
    else:
        lista_principal[1].append(num)
lista_principal[0].sort()
lista_principal[1].sort()
print(f'Valores pares da lista: {lista_principal[0]}')
print(f'Valores ímpares da lista: {lista_principal[1]}')
