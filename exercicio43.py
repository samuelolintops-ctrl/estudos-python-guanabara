#=========== Desafio 43 ===========
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo 
# com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

# A fórmula é IMC = peso / (altura x altura)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / altura ** 2

print(f"Com o IMC de {imc:.1f}, sua classificação é: ", end = '')
if imc < 18.5:
    print("\033[31mAbaixo do peso\033[m.")
elif imc < 25:
    print("\033[32mPeso ideal\033[m.")
elif imc < 30:
    print("\033[31mSobrepeso\033[m.")
elif imc < 40:
    print("\033[31mObesidade\033[m.")
else:
    print("\033[31mObesidade mórbida\033[m.")