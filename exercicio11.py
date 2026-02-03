#=========== Desafio 11 ===========
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

alt = float(input("Digite a a altura da parede (em metros): "))
larg = float(input("Digite a largura da parede (em metros): "))
area = alt * larg
tinta = area / 2

print(f"Dado a área de {area }metros quadrados, você precisará de {tinta} litros de tinta.")