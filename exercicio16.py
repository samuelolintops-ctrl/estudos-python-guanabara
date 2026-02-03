#=========== Desafio 16 ===========
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

# trunc é o ideal, porque o floor não funcionaria com números negativos e retornaria um valor indesejado
# o trunc preserva a parte inteira mesmo em negativos

num = float(input("Digite um número real: "))
pt_int = trunc(num)
print(f"O número digitado ({num}), tem como parte inteira: {pt_int}.")
