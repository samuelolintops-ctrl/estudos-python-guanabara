#=========== Desafio 08 ===========
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros

met = float(input("Digite um valor em metros: "))
cm = met * 100
mm = met * 1000

print(f"Valor lido em metros: {met}")
print(f"Em centímetros: {cm}\nEm milímetros: {mm}")