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
