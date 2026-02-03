#=========== Desafio 57 ===========
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a 
# digitação novamente até ter um valor correto.

print("\n")
sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0] # Adição de um fatiamento de string para armazenar apenas a primeira letra
while sexo not in "MF":
    sexo = str(input("Opção inválida, verifique e digite novamente [M/F]: ")).strip().upper()
if sexo == "F":
    print("\nSexo registrado: Feminino.")
else:
    print("\nSexo registrado: Masculino.")