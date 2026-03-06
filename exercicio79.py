#=========== Desafio 79 ===========

# Crie um programa onde o usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

cont = 1
lista = []

print('\nDigite valores quaisquer.')
while True:
    num = int(input(f'{cont}º valor: '))
    if num not in lista:
        lista.append(num)
        print('\033[32mValor adicionado com sucesso!\033[m')
        
        while True:
            opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if opcao in 'SN':
                break
            print('\033[31mOpção inválida! Digite S ou N.\033[m')
        if opcao == 'N':
            break
        cont += 1
    
    else:
        print('\033[31mValor duplicado! Este número não será adicionado' 
              'na lista.\033[m')

lista.sort()
print('\nValores únicos digitados em ordem crescente: ', end = '')
for ind, val in enumerate(lista, start=1):
    print(f'{val}', end =  ', ' if ind < len(lista) else '')
