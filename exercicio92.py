#=========== Desafio 92 ===========

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# (CTPS) e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for 
# diferente de ZERO, o dicionário receberá também o ano de contratação e o 
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.

from datetime import date

nome = str(input('Nome: ')).strip().title()
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
while True:
    cart_trabalho = str(input('Carteira de Trabalho (CTPS): '
    '[0 se não tiver] ')).strip()
    if cart_trabalho.isnumeric():
        break
    print('\033[31mAlgum caracter inválido foi digitado. '
          'Digite apenas números!\033[m')
dados = {
    'nome': nome,
    'ano_nascimento': ano_nasc,
    'idade': idade,
    'carteira_de_trabalho': cart_trabalho
}
if cart_trabalho != '0':
    ano_contrat = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    tempo_trabalho = ano_atual - ano_contrat
    ano_aposent = dados['idade'] + (35 - tempo_trabalho)
    dados['ano_de_contratacao'] = ano_contrat
    dados['salario'] = salario
    dados['ano_de_aposentadoria'] = ano_aposent
print('-' * 40)
print(f'{"DADOS CADASTRADOS":^40}')
print('-' * 40)
for k, v in dados.items():
    print(f' - {k} tem valor: {v}')
