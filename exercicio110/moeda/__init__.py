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
    """
    Mostra na tela um resumo do valor digitado pelo usuário com todas as
    funções do módulo.
    :param valor: valor digitado pelo usuário
    :param p_aumento: taxa de aumento aplicado no valor
    :param p_diminui: taxa de diminuição aplicado no valor
    :return: sem retorno
    """
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<20}' f'{moeda(valor):>20}')
    print(f'{"Dobro do preço:":<20}' f'{dobro(valor, True):>20}')
    print(f'{"Metade do preço:":<20}' f'{metade(valor, True):>20}')
    print(f'{f"{p_aumento}% de aumento:":<20}' 
          f'{aumentar(valor, p_aumento, True):>20}')
    print(f'{f"{p_diminui}% de redução:":<20}' 
          f'{diminuir(valor, p_diminui, True):>20}')
    print('-' * 40)
