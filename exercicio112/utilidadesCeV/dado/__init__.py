def leiaDinheiro(mensagem):
    """
    Função que aceita apenas números reais. Aceita vírgula e ponto.
    :param mensagem: prompt para o usuário
    :return: retorna um número do tipo float
    """
    while True:
        num = str(input(mensagem)).strip()
        num = num.replace(',', '.')
        temp = num.replace('.', '')
        if temp.isnumeric() and num.count('.') <= 1:
            break
        print('\033[31mERRO! Digite um preço válido.\033[m')
    return float(num)
