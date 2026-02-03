#=========== Desafio 28 ===========
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça 
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

num = int(input("\nDigite um número e decubra se você acertou: "))
sorteado = randint(1, 5) # randint leva como parametro o inicio e fim da sequencia numérica que irá sortear incluidndo eles mesmos

if num == sorteado:
    print("\nParabéns você acertou!!")
else:
    print("Burro KKKKKKKKKKK, errou otário")
    print(f"O número sorteado: {sorteado}")