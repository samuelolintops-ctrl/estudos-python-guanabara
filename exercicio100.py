#=========== Desafio 100 ===========

# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar().
# A primeira função vai sortear 5 números e colocá-los dentro da lista.
# A segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.

from random import randint
from time import sleep

def exibir_titulo(mensagem):
    """
    Exibe uma mensagem em destaque formatada de acordo com o 
    tamanho da frase.
    """
    tam_mensagem = len(mensagem) + 4
    print('=' * tam_mensagem)
    print(f'  {mensagem.upper()}')
    print('=' * tam_mensagem)


def sorteia(lista):
    """
    Sorteia 5 números e os coloca em uma lista.
    """
    limite = 5
    i = 1
    f = 50
    for _ in range(0, limite):
        lista.append(randint(i, f))
    print(f'(Gerando números entre {i} e {f})')
    sleep(1)
    print('\033[32mNúmeros aleatórios adicionados na lista com sucesso!\033[m')

def somaPar(lista):
    """
    Soma os pares de uma lista e mostra o resultado na tela.
    Também notifica se não há pares na lista.
    """
    print('Analisando lista', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.', flush=True)
    sleep(0.5)
    soma_pares = 0
    contador = 0
    for n in lista:
        if n % 2 == 0:
            soma_pares += n
            contador += 1
    if contador == 0:
        print('Não há pares na lista.')
    else:
        print(f'A soma dos {contador} pares da lista resultou em {soma_pares}.')


# Programa principal
exibir_titulo('sorteio e soma de pares entre números aleatórios')
numeros = []
sorteia(numeros)
print(f'\nLista gerada: {numeros}.')
somaPar(numeros)
