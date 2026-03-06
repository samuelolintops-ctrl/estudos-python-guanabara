#=========== Desafio 89 ===========

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo 
# em uma lista composta. No final, mostre um boletim contendo a média de cada
# um e permita que o usuário possa mostrar as notas de cada aluno 
# individualmente.

print('=' * 40)
print(f'{"CADASTRO DE ALUNOS E NOTAS":^40}')
print('=' * 40)
alunos = []
qtd_notas = 2
cont = 0
while True:
    temporario = [str(input(f'Nome do aluno {cont}: ')).strip().title()]
    soma_notas = 0
    for i in range(1, qtd_notas + 1):
        nota = float(input(f'{i}º nota: '))
        temporario.append(nota)
        soma_notas += nota
    media = soma_notas / 2
    temporario.append(media)
    alunos.append(temporario[:])
    temporario.clear()
    while True:
        opcao = str(input('Quer incluir mais um aluno? '
        '[SIM/NÃO] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite SIM ou NÃO.\033[m')
    if opcao == 'N':
        break
    cont += 1
qtd_alunos = len(alunos)
print('=' * 40)
print(f'{"BOLETIM DA TURMA":^40}')
print('=' * 40)
print(f'{"No.":<4}', end='')
print(f'{"Nome":<20}', end='')
print(f'{"Média":<5}')
print('-' * 40)
for i in range(0, qtd_alunos):
    print(f'{i:<4}', end='')
    print(f'{alunos[i][0]:<20}', end='')
    print(f'{alunos[i][-1]:<5.2f}')
print('-' * 40)
while True:
    while True:
        n_aluno = int(input('Deseja ver as notas de qual aluno? '
        '(Digite o No do aluno ou 999 para interromper) '))
        if 0 <= n_aluno < qtd_alunos or n_aluno == 999:
            break
        print('\033[31mÍndice inválido! Digite novamente.\033[m')
    if n_aluno == 999:
        break
    print(f'Notas do(a) aluno(a) {alunos[n_aluno][0]}: ', end='')
    for i in range(1, qtd_notas + 1):
        print(f'{i}º nota: {alunos[n_aluno][i]:.2f}', end='... ')
    print()
    print('-' * 40)
