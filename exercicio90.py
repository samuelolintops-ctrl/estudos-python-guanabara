#=========== Desafio 90 ===========

# Faça um programa que leia nome e média de um aluno, guardando também a 
# situação (Aprovado/Reprovado) em um dicionário. No final, mostre o conteúdo da 
# estrutura na tela.

nome = str(input('Nome: ')).strip().title()
media = float(input(f'Média de {nome}: '))
aluno = {'nome': nome, 'media': media}
if aluno['media'] < 7:
    aluno['situacao'] = '\033[31mReprovado\033[m'
else:
    aluno['situacao'] = '\033[32mAprovado\033[m'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
