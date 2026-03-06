#=========== Desafio 96 ===========

# Faça um programa que tenha uma função chamada area(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def exibir_titulo(mensagem):
    """
    Exibe uma mensagem em destaque formatada de acordo com o 
    tamanho da frase.
    """
    tam_frase = len(mensagem) + 4
    print('=' * tam_frase)
    print(f'  {mensagem.upper()}')
    print('=' * tam_frase)

def area(largura, comprimento, metrica):
    """
    Calcula a área de um terreno retangular.
    largura: dimensão da largura do terreno;
    comprimento: dimensão do comprimento do terreno;
    metrica: unidade de medida (str).
    """
    a = largura * comprimento
    print(f'\nLargura: {largura}{metrica}\nComprimento: {comprimento}{metrica}')
    print(f'Área: {a}{metrica}²')


# Programa principal
exibir_titulo('calculando área de um terreno')
met = str(input('Deseja usar qual métrica? (km, m, cm...) ')).strip().lower()
larg = float(input(f'Largura (em {met}): '))
comp = float(input(f'Comprimento (em {met}): '))
area(larg, comp, met)
