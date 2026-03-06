#=========== Desafio 102 ===========

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
# primeiro que indique o número a calcular e o outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo
# de cálculo do fatorial.

def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: número o qual será calculado o fatorial
    :param show: mostra ou não o processo de cálculo
    :return: retorna o valor do fatorial calculado
    """
    from time import sleep
    result = 1
    for n in range(num, 0, -1):
        if show:
            print(f'{n}', 'x ' if n > 1 else '= ', end='', flush=True)
            sleep(0.3)
        result *= n
    return result


# Programa principal
print(fatorial(6, show=True))
