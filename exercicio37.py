#=========== Desafio 37 ===========
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
# conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print("""Conversão de base decimal para outras bases
- 1 para binário
- 2 para octal
- 3 para hexadecimal""")
opcao = int(input("Digite sua opção (1, 2 ou 3): "))

num = int(input("Digite um número para conversão: "))

if opcao == 1:
    print("\nConvertendo para binário...")
    binario = bin(num)
    print(f"{num} em BINÁRIO é {binario[2:]}")
elif opcao == 2:
    print("\nConvertendo para octal...")
    octal = oct(num)
    print(f"{num} na base OCTAL é {octal[2:]}")
elif opcao == 3:
    print("\nConvertendo para hexadecimal...")
    hexa = hex(num)
    print(f"{num} na base HEXADECIMAL é {hexa[2:]}")
else:
    print("\n\033[31mOpção inválida, escolha entre 1, 2 e 3.\033[m")
print("\nPrograma encerrando. Até mais!")
