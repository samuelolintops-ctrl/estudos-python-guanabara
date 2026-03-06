#=========== Desafio 84 ===========

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em 
# uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
cont = 1
while True:
    print(f'==== {cont}º pessoa ====')
    dados = [str(input('Nome: ')).strip().title()]
    while True:
        peso = float(input('Peso (em kg): '))
        if peso > 0:
            break
        print('\033[31mVocê digitou um peso nulo ou negativo! ' 
              'Digite os dados novamente.\033[m')
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    if cont == 1:
        maior_peso = menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso
    print('\033[32mCadastro realizado com sucesso!\033[m')
    while True:
        opcao = str(input('Deseja continuar? [SIM/NÃO] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite SIM ou NÃO.\033[m')
    if opcao == 'N':
        break
    cont += 1
# A
qtd_cadastros = len(pessoas)
print(f'\nQuantidade de cadastros realizados: {qtd_cadastros}.')
# B & C
print(f'Pessoas cadastradas com o menor peso ({menor_peso:.2f}kg): ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'{p[0]}...', end='')
print(f'\nPessoas cadastradas com o maior peso ({maior_peso:.2f}kg): ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'{p[0]}...', end='')
