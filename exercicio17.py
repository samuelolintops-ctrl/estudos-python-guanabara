#=========== Desafio 17 ===========
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, pow, hypot

print("Digite os valores dos catetos do triângulo:")
cat_op = float(input("Cateto oposto: "))
cat_ad = float(input("Cateto adjacente: "))
metrica = input("Digite a unidade de medida (m, cm...): ")

hip = sqrt((pow(cat_op, 2) + pow(cat_ad, 2)))

print(f"\n\nMedidas do seu triângulo:\nCateto oposto: {cat_op}{metrica}\nCateto adjacente: {cat_ad}{metrica}\nHipotenusa: {hip:.2f}{metrica}")

# a biblioteca math já tem uma função de calculo para a hipotenusa, é o math.hypot(), ou seja o programa rodaria se eu fizesse assim:

hip = hypot(cat_op, cat_ad)
print(f"Hipotenusa: {hip:.2f}{metrica}")