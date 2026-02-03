#=========== Desafio 59 ===========
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa 
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print("\nDigite dois valores para realizar comparações/operações entre eles:")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
opcao = 0

while opcao != 5:
    print("=-" * 20)
    print("""\nEscolha sua opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opcao = int(input("Digite sua opção: "))
    print("\n")
    if opcao == 1:
        soma = n1 + n2
        print(f"\033[34mA soma entre {n1} e {n2}: é {soma}.\033[m")
    elif opcao == 2:
        prod = n1 * n2
        print(f"\033[34mO produto entre {n1} e {n2} é {prod}.\033[m")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"\033[34mEntre {n1} e {n2} o maior é {maior}.\033[m")
        elif n2 > n1:
            maior = n2
            print(f"\033[34mEntre {n1} e {n2} o maior é {maior}.\033[m")
        else:
            print(f"\033[34mEntre {n1} e {n2} não há um maior, são iguais.\033[m")
    elif opcao == 4:
        print("Redefinindo os valores...")
        sleep(1)
        n1 = int(input("Novo primeiro número: "))
        n2 = int(input("Novo segundo número: "))
        print("\n")
        print("\033[32mValores alterados com sucesso!\033[m")
    elif opcao == 5:
        print("Encerrando programa...")
    else:
        print("\033[31mOpção inválida! Por favor digite alguma opção válida (1 a 5).\033[m")
    sleep(2)
