#=========== Desafio 36 ===========
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o 
# valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: RS"))
tempo = int(input("Digite em quantos anos ele vai pagar: "))
meses = tempo * 12 # Conversão para meses
prestacao = valor_casa / meses
print(f"Cada prestação custaria RS{prestacao:.2f}, considerando {tempo} anos para pagar. ", end = '')
if prestacao > (salario * 30 / 100):
    print("\033[31mEmpréstimo negado.\033[m")
else:
    print("\033[32mEmpréstimo aprovado.\033[m")