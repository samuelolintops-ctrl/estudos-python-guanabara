#=========== Desafio 69 ===========

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres_20 =  0
cont = 1

while True:
    idade = int(input(f"\nDigite a idade da {cont}º pessoa: "))
    # Loop para validação do sexo
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo in 'MF':
            break
        print("\033[31mSexo inválido!\033[m Digite M ou F.")
    
    # Atualiza os contadores baseado nas exigências do enunciado
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

    # Loop para confirmar se o usuario quer continuar e validação da escolha
    while True:
        opcao = str(input("\nDeseja continuar? [S/N] ")).strip().upper()[0]
        if opcao in 'SN':
            break
        print("\033[31mOpção inválida!\033[m Digite S ou N.")
    
    # Interrompe o loop se o usuário digitar N
    if opcao == 'N':
        break
    cont += 1
    print("-" * 30)
    
print("\n-------Análise das pessoas cadastradas-------")
print(f"Quantidade de pessoas cadastradas: {cont}")
print(f"Homens cadastrados: {homens}")
print(f"Pessoas com mais de 18 anos: {maiores}")
print(f"Mulheres com menos de 20 anos: {mulheres_20}")
