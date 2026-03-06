def aumentar(num, taxa=0):
    """
    Calcula o aumento de um valor baseado numa taxa percentual
    """
    resultado = num
    resultado += (num * taxa) / 100
    return resultado

def diminuir(num, taxa=0):
    """
    Calcula a redução de um valor baseado numa taxa percentual
    """
    resultado = num
    resultado -= (num * taxa) / 100
    return resultado

def dobro(num):
    resultado = num * 2
    return resultado

def metade(num):
    resultado = num / 2
    return resultado

def moeda(val):
    """
    Formata o valor enviado no argumento para o padrão monetário 
    brasileiro
    """
    val = str(f'{val:.2f}')
    val = val.replace('.', ',')
    return f'R$ {val}'