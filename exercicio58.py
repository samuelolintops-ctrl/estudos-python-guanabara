#=========== Desafio 58 ===========
# Melhore o jogo do DESAFIO 028 onde o computador "pensa" em um número entre 0 e 10. Só que agora o jogador vai 
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# (Desafio 028): Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o 
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
comp = randint(0, 10)
palpite = 0
escolha = -1
print("\nTente adivinhar o número entre 0 a 10 que o computador pensou!")

while escolha != comp:
    escolha = int(input("Qual o seu palpite? "))
    palpite += 1
    if escolha < comp:
        print("Você digitou um número menor! Tente novamente.")
    elif escolha > comp: 
        print("Você digitou um número maior! Tente novamente.")

print(f"Parabéns, você acertou!! Para acertar foram necessários {palpite} palpites.")
