#=========== Desafio 44 ===========
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros3

valor = float(input("Digite o valor do produto: RS"))
print("""Escolha uma opção:
1. à vista dinheiro/cheque
2. à vista no cartão
3. em até 2x no cartão
4. 3x ou mais no cartão""")
opcao = int(input("Digite sua opção (1, 2, 3 ou 4): "))

if opcao == 1:
    valor = valor - (valor * 10 / 100)
elif opcao == 2:
    valor = valor - (valor * 5 / 100)
elif opcao == 3:
    parcela = valor / 2
    print(f"Valor da parcela (2x): \033[32mRS{parcela:.2f}\033[m.")
elif opcao == 4:
    valor = valor + (valor * 20 / 100)
    totparcelas = int(input("Deseja dividir em quantas parcelas? "))
    parcela = valor / totparcelas
    print(f"Valor da parcela ({totparcelas}): \033[32mRS{parcela:.2f}\033[m (juros aplicado).")
else:
    print("\033[31mOpção inválida. Encerrando programa.\033[m")
    exit()
print(f"Valor final: \033[32mRS{valor:.2f}\033[m.")
