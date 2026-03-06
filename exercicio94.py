#=========== Desafio 94 ===========
#-------------------------------------------------------------------------------
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No 
# final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

dados = {}
pessoas = []
soma_idades = 0
mulheres = []
p_acima_media = []
while True:
    dados.clear()
    print(f'\n=== DADOS DA {len(pessoas) + 1}º PESSSOA ===')
    nome = str(input('Nome: ')).strip().title()
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('\033[31mSexo inválido! Digite M ou F.\033[m')
    idade = int(input('Idade: '))
    soma_idades += idade
    dados = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(dados.copy())
    print('\033[32mCadastro realizado com sucesso!\033[m')
    if sexo == 'F':
        mulheres.append(nome)
    while True:
        opcao = str(input('Deseja incluir mais alguém? '
        '[SIM/NÃO] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite SIM ou NÃO.\033[m')
    if opcao == 'N':
        break
qtd_pessoas = len(pessoas)
media = soma_idades / qtd_pessoas
print(f'\nForam cadastradas ao todo {qtd_pessoas} pessoas.')
print(f'A média de idade das pessoas cadastradas é {media:.1f}.')
print(f'As mulheres cadastradas foram: {mulheres}')
for p in pessoas:
    if p['idade'] > media:
        p_acima_media.append(p.copy())
print('As pessoas com idade acima da média do grupo foram:')
for p in p_acima_media:
    for k, v in p.items():
        print(f'{k} -> {v}', end='' if k == 'idade' else '; ')
    print()
print('\nPrograma encerrado. Até a próxima!')