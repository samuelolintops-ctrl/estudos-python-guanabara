#=========== Desafio 101 ===========

# Crie um programa que tenha uma função chamada voto() que receba como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se
# uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        situacao = 'NEGADO'
    elif idade <= 17 or idade > 65:
        situacao = 'OPCIONAL'
    else:
        situacao = 'OBRIGATÓRIO'
    return situacao


# Programa principal
nasc = int(input('Qual o seu ano de nascimento: '))
situacao = voto(nasc)
print(f'Situação de voto: {situacao}.')