#=========== Desafio 56 ===========
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos. 

soma_idade = 0
mul_menor = 0
maior_idade = 0
nome_velho = ""
print("\n")
for i in range(1, 5):
    print(f"------ PESSOA {i}: ------")
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if sexo in "Ff" and idade < 20:
        mul_menor += 1
    if sexo in "Mm" and idade > maior_idade:
        nome_velho = nome
        maior_idade = idade
media_idade = soma_idade / 4
print(f"\n- Média de idade do grupo: {media_idade}.")
print(f"- Quantidade de mulheres com menos de 20 anos: {mul_menor}.")
if nome_velho == "":
    print(f"- Nenhum homem digitado.")
else:
    print(f"- Homem mais velho: {nome_velho}")
