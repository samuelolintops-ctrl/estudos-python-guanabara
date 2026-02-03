#=========== Desafio 14 ===========
# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temp = float(input("Digite a temperatura em graus Celsius: "))
temp_far = (temp * 1.8) + 32

print(f"{temp:.1f} graus Celsius equivale a {temp_far:.1f} graus Fahrenheit.")