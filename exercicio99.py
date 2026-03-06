#=========== Desafio 99 ===========

# Faça um programa que tenha uma função chamada maior(), que receba vários 
# parâmetros com valores inteiros. Seu programa tem que analisar todos os 
# valores e dizer qual deles é o maior.

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

def imprime_linha(separador, tamanho):
    print(separador * tamanho)

def maior(* numeros):
    print(f'Analisando valores {numeros}', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.', end='', flush=True)
    sleep(0.5)
    print('.')
    sleep(0.5)
    if len(numeros) == 0:
        print('Nenhum número foi passado.')
    else:
        print(f'O maior valor é {max(numeros)}.')


# Programa principal
exibir_titulo('analisando o maior número')
maior(1, 2, 3, 3, 9)
imprime_linha('-', 30)
maior()
imprime_linha('-', 30)
maior(98)
imprime_linha('-', 30)
print('Fim do programa. Até mais.')
