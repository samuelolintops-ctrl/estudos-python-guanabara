#=========== Desafio 31 ===========
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando RS 0,50
# por Km para viagens de até 200Km e RS0,45 para viagens mais longas.

dist = float(input("Digite a distância da sua viagem em Km: "))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print(f"O valor da sua passagem: RS{preco:.2f}")