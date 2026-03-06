#=========== Desafio 81 ===========

# Crie um programa que vai ler vários números e colocar em uma lista. Depois 
# disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite S ou N.\033[m')
    if opcao == 'N':
        break

# A
tam_lista = len(lista)
print(f'\nForam digitados {tam_lista} valores.')

# B
lista.sort(reverse=True)
print(f'A lista organizada de forma decrescente: {lista}')

# C
if 5 in lista:
    print('O valor 5 foi digitado e por isso está na lista.')
else:
    print('O valor 5 não foi digitado, logo não está na lista.')
