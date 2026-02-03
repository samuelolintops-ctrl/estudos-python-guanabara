#=========== Desafio 29 ===========
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar RS7,00 por cada Km acima do limite.

velocidade = int(input("Digite a velocidade do carro (em km/h): "))
if velocidade > 80:
    v_acima = velocidade - 80
    multa = v_acima * 7
    print(f"Você foi multado!!\nValor da multa: RS{multa:.2f}")
else:
    print("Você não será multado.")