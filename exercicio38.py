#=========== Desafio 38 ===========
# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print("\033[1mDigite dois números inteiros:\033[m")
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

if num1 > num2:
    print("\nO \033[1mprimeiro\033[m valor é maior que o segundo.")
elif num2 > num1:
    print("\nO \033[1msegundo\033[m valor é maior que o primeiro.")
else:
    print("\nNão existe valor maior, os dois são iguais.")