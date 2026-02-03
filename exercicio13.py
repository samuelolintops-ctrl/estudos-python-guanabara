#=========== Desafio 13 ===========
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input("Digite seu salário: "))
novo_sal = sal + ((sal / 100) * 15)

print(f"Seu salário de RS{sal:.2f} com aumento de 15% fica em RS{novo_sal:.2f}.")