import utilidades
from cores import colorir

def novo_cadastro(nome):
    with open(nome, 'a') as arquivo:
        print(colorir('Digite os dados da pessoa:', 'amar'))
        nome = str(input('Nome: ')).strip().title()
        idade = utilidades.leiaInt('Idade: ')
        arquivo.write(f'{nome};{idade}\n')
        print(colorir('Cadastro realizado com sucesso!', 'verd'))