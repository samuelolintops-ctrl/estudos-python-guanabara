#=========== Desafio 113 ===========

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um tipo numérico inválido (como
# uma letra ou deixar vazio). Aproveite e crie também uma função 
# leiaFloat() com a mesma funcionalidade, tratando as exceções de valor
# e a interrupção do usuário.

def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except ValueError:
            print('\033[31mERRO: digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar. Retorno de valor: 0')
            return 0
        except Exception as erro:
            print(f'\033[31mERRO do tipo: {erro.__class__}.\033[m')      
        else:
            return n

def leiaFloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except ValueError:
            print('\033[31mERRO: digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar. Retorno de valor: 0')
            return 0.0
        except Exception as erro:
            print(f'\033[31mERRO do tipo: {erro.__class__}.\033[m')
        else:
            return n
        

# Programa principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'\nVocê digitou o número inteiro {inteiro} e o número real {real}.')
