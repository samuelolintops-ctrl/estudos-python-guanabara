#=========== Desafio 15 ===========
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa RS 60,00 por dia e RS0,15 por
# Km rodado.

km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

val_dia = 60.0
val_km = 0.15
val_total = (km * val_km) + (dias * val_dia)

print(f"Percorrendo {km}km usando o carro por {dias} dia (s), você deverá pagar RS{val_total:.2f}.")