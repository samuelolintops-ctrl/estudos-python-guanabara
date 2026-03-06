#=========== Desafio 80 ===========

# Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o 
# sort()). No final, mostre a lista ordenada na tela.

limite = 5
posicao = 0
lista = []

for rodada in range(0, limite):
    num = int(input(f'\n{rodada + 1}º valor: '))
    
    if rodada == 0:
        lista.append(num)
    
    else:
        posicao = 0
        for i in lista:
            if num > i:
                posicao += 1
        lista.insert(posicao, num)
    
    print(f'{num} adicionado na posição {posicao}.')

print(f'\nA lista criada: {lista}')
