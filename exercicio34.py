#=========== Desafio 34 ===========
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a RS1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Digite seu salário: "))
if sal > 1250:
    novo_sal = sal + (sal * 10 / 100)
else:
    novo_sal = sal + (sal * 15 / 100)
print(f"Salário antigo: RS{sal:.2f}\nSalário novo: RS{novo_sal:.2f}.")