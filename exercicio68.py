#=========== Desafio 68 ===========

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

cont_vitorias = 0
print("=-" * 13 + "\n" + "Vamos jogar par ou ímpar!" + "\n" + "=-" * 13)

while True:
    comp = randint(0, 5)

    # Validação de P ou I
    while True:
        par_impar = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0] # Armazena escolha do usuario entre par e impar
        if par_impar in 'PI':
            break
        print("\033[31mEscolha inválida. Digite P ou I, para par ou ímpar, respectivamente.\033[m" + "\n")
    
    # Validação do numero que o usuario vai jogar
    while True:
        escolha = int(input("Escolha seu número (entre 0 e 5): ")) # Armazena o valor da jogada do usuario
        if escolha <= 5 and escolha >= 0:
            break
        print("\033[31mEscolha inválida. Digite um número no intervalo de 0 a 5.\033[m" + "\n")
    
    # Transforma P e I para 0 e 1 para facilitar condiçãO DE vitória
    if par_impar == 'P':
        valor_par_impar = 0
    if par_impar == 'I':
        valor_par_impar = 1

    soma = comp + escolha
    resultado = soma % 2
    result_jogo = 'PAR' if resultado == 0 else 'ÍMPAR'

    if resultado == valor_par_impar:
        cont_vitorias += 1
        print("\n" + "\033[32mVocê ganhou!\033[m" + f"\nVocê jogou {escolha} e o computador {comp}. Total {soma} é {result_jogo}.")
        print("Vamos jogar novamente...\n" + "-" * 25)
    else:
        print("\n" + "\033[31mVocê perdeu!\033[m" + f"\nVocê jogou {escolha} e o computador {comp}. Total {soma} é {result_jogo}.")
        break

print(f"\nVocê ganhou {cont_vitorias} vez(es) consecutiva(s)!")
