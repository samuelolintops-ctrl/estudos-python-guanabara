#=========== Desafio 39 ===========
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Digite o seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda vai se alistar. Falta(m) {tempo} ano(s).")
elif idade == 18:
    print("Você está em tempo de se alistar!")
else:
    excedente = idade - 18
    print(f"O tempo de alistamento passou {excedente} ano(s). Quando realizado fora do tempo uma multa é aplicada.")
print(f"Ano de alistamento: {ano + 18}")