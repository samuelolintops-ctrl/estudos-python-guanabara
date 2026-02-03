#=========== Desafio 12 ===========
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

val = float(input("Digite o preço original: RS"))
novo_val = val - ((val / 100) * 5)

print(f"O valor lido de RS{val:.2f}, com 5% de desconto fica RS{novo_val:.2f}.")