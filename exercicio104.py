#=========== Desafio 104 ===========

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante à função input() do Python, mas que faça a validação para aceitar
# apenas um valor numérico.

def leiaInt(mensagem):
    """
    Lê um número inteiro válido.
    :param mensagem: string de comando para o usuário
    """
    while True:
        valor = input(f'{mensagem}').strip()
        if valor.isnumeric():
            valor = int(valor)
            break
        print('\033[31mERRO! Digite um número válido.\033[m')
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
