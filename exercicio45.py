#=========== Desafio 45 ===========
# Crie um programa que faça o computador jogar Jokenpô com você.
# O programa deve ler a escolha do jogador (Pedra, Papel ou Tesoura) 
# e gerar uma escolha aleatória para o computador. 
# No final, mostre quem venceu ou se houve empate.

from random import randint
print("\033[36m-=\033[m" * 20)
print(f'\033[1;34m{"JOKENPÔ":^40}\033[m')
print("\033[36m-=\033[m" * 20)
print("""\nFaça sua escolha!
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
opcao = int(input("Digite sua opção (0, 1 ou 2): "))

sort = randint(0, 2)
escolhas = ["Pedra", "Papel", "Tesoura"]
vit_jogador = [(0, 2), (1, 0), (2, 1)]

if opcao == sort:
    print("\033[33m\nEMPATE!\033[m")
elif (opcao, sort) in vit_jogador:
    print("\033[32m\nPARABÉNS! Você venceu!\033[m")
elif opcao not in (0, 1, 2):
    print("\033[31m\nERRO: Opção inválida!\033[m")
    exit()
else:
    print("\033[31m\nDERROTA! Não foi dessa vez.\033[m")

print(f"\nESCOLHAS\nUsuário: {escolhas[opcao]}\nComputador: {escolhas[sort]}")
