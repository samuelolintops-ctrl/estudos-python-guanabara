#=========== Desafio 41 ===========
# A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
# categoria, de acordo com a idade:
# - Até 9 anos: mirim
# - Até 14 anos: infantil
# - Até 19 anos: junior
# - Até 24 anos: sênior
# - Acima: master

from datetime import date

ano = int(input("Digite o ano de nascimento do atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 0:
    print("\033[31mERRO: Você digitou um ano maior que o atual, verifique e tente novamente.\033[m")
elif idade <= 9:
    print("Categoria: \033[31mMIRIM\033[m")
elif idade <= 14:
    print("Categoria: \033[32mINFANTIL\033[m")
elif idade <= 19:
    print("Categoria: \033[34mJUNIOR\033[m")
elif idade <= 24:
    print("Categoria: \033[35mSÊNIOR\033[m")
elif idade > 24:
    print("Categoria: \033[33mMASTER\033[m")