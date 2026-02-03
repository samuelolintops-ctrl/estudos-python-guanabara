#=========== Desafio 71 ===========

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print("\n" + "=-" * 20)
titulo = 'CAIXA ELETRÔNICO'
print(f"{titulo:^40}")
print("=-" * 20)

valor = int(input("Digite o valor que deseja sacar (apenas os reais, não é possível sacar moedas): RS"))
total = valor
cedula_atual = 200
total_cedulas = 0

while True:
    # Verifica se o total ainda é maior ou igual ao valor da cedula_atual. Se for, significa que uma cédula daquele valor pode ser entregue.
    # Então, o total é diminuído pelo valor da cedula_atual, e a contagem de total_cedula para aquela cédula é incrementada em um. Este processo
    # se repete até que o total seja menor que a cedula_atual.
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    
    # Caso minha cédula atual não sevir mais, ou seja, ser maior que o valor atual, faço a impressão da qtd de cédulas a ser entregue e 
    # atualizo o valor dela
    else:
        # Só imprime se a quantidade de cédulas for maior que 0, para evitar prints desnecessários
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de RS{cedula_atual}.00.")
        
        # Atualizo minha cédula atual para uma menor quando ela ultrapassar o valor atual
        if cedula_atual == 200:
            cedula_atual = 100
        elif cedula_atual == 100:
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 2
        elif cedula_atual == 2:
            cedula_atual = 1

        total_cedulas = 0 # Zero meu contador de cédulas para a próxima quantidade do próximo valor de cédula

        # Interrompo o loop quando o total chegar em zero, ou seja, depois de todas as cédulas serem entregues, encerrando o programa
        if total == 0:
            break
