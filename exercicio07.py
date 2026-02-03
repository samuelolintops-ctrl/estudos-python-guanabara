#=========== Desafio 07 ===========
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Notas lidas -> Primeira nota: {nota1:.2f}; Segunda nota: {nota2:.2f}")
print(f"Média: {media:.2f}")