#=========== Desafio 82 ===========

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite S ou N.\033[m')

    if opcao == 'N':
        break

for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'\nLista original: {lista}')
print(f'Lista com os números pares: {lista_par}')
print(f'Lista com os números ímpares: {lista_impar}')
