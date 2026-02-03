#=========== Desafio 70 ===========

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$ 1000.
# C) qual é o nome do produto mais barato.

# Inicialiçaão das variáveis
total = 0.0
quant_prod_1000 = 0
prod_barato = ""
cont = 1

# Loop de venda
while True:
    nome_prod = str(input(f"Nome do {cont}º produto: ")).strip().title()
    # Laço para armazenar o valor do produto e validação (prevenção contra negativos)
    while True:
        preco = float(input("Valor do produto: "))
        if preco > 0.0:
            break
        print("\n" + "\033[31mERRO!\033[m Você digitou um número negativo, confira e reescreva o valor inserido.")
    
    total += preco

    if cont == 1 or preco < valor_barato:
        valor_barato = preco
        prod_barato = nome_prod

    if preco > 1000.0:
        quant_prod_1000 += 1
    
    # Laço para armazenar a opcao do usuario se quer continuar ou nao e validação da opção
    while True:
        opcao = str(input("\nDeseja continuar? [S/N] ")).strip().upper()[0]
        if opcao in 'SN':
            break
        print("\n" + "\033[31mERRO!\033[m Você digitou uma opção inválida, confira e reescreva uma opção válida (S ou N).")
    
    # Encerra a venda se o usuario digitar N
    if opcao == 'N':
        break

    cont += 1

print("-" * 17 + "\nANÁLISE DA COMPRA\n" + "-" * 17)
print(f"Total gasto: RS{total:.2f}")
print(f"Quantidade de produtos que custam acima de RS1000.00: {quant_prod_1000}")
print(f"Produto mais barato: {prod_barato}, custando RS{valor_barato:.2f}")
