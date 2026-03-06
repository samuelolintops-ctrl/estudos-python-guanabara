#=========== Desafio 97 ===========

# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(mensagem):
    """
    Exibe uma mensagem em destaque formatada de acordo com o 
    tamanho da frase.
    """
    tam_mensagem = len(mensagem) + 4
    print('~' * tam_mensagem)
    print(f'  {mensagem}')
    print('~' * tam_mensagem)


# Programa principal
texto = str(input('Digite uma mensagem para ser formatada: ')).strip()
escreva(texto)
