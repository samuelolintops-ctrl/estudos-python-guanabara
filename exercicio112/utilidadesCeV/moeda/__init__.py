def moeda(val):
    val = str(f'{val:.2f}')
    val = val.replace('.', ',')
    return f'R$ {val}'

def aumentar(num, taxa=0, form=False):
    """
    Calcula o aumento de um valor baseado numa taxa percentual
    """
    resultado = num
    resultado += (num * taxa) / 100
    if form:
        return moeda(resultado)
    return resultado

def diminuir(num, taxa=0, form=False):
    """
    Calcula a redução de um valor baseado numa taxa percentual
    """
    resultado = num
    resultado -= (num * taxa) / 100
    if form:
        return moeda(resultado)
    return resultado

def dobro(num, form=False):
    resultado = num * 2
    if form:
        return moeda(resultado)
    return resultado

def metade(num, form=False):
    resultado = num / 2
    if form:
        return moeda(resultado)
    return resultado

def resumo(valor, p_aumento, p_diminui):
    print('-' * 50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-' * 50)
    print(f'{"Preço analisado:":<25}', end='')
    print(f'{moeda(valor):>25}')
    print(f'{"Dobro do preço:":<25}', end='')
    print(f'{dobro(valor, True):>25}')
    print(f'{"Metade do preço:":<25}', end='')
    print(f'{metade(valor, True):>25}')
    print(f'{f"{p_aumento}% de aumento:":<25}', end='')
    print(f'{aumentar(valor, p_aumento, True):>25}')
    print(f'{f"{p_diminui}% de redução:":<25}', end='')
    print(f'{diminuir(valor, p_diminui, True):>25}')
    print('-' * 50)
