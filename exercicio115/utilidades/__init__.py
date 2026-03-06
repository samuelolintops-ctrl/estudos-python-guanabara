from cores import colorir

def imp_linha(tam=40):
    print('-' * tam)

def mostra_menu(opcoes_menu, cor='azul'):
    """
    -> Mostra um menu com opções listadas padronizado em azul.
    :param opcoes_menu: iterável com as opções
    :param cor: cor das opções
    :return: sem retorno
    """
    for ind, val in enumerate(opcoes_menu):
        print(colorir(f'{ind + 1}. {val}', cor))

def cabecalho(mensagem, form=False):
    """
    -> Mostra na tela uma mensagem em destaque, podendo ser formatada
    de acordo com o tamanho da mensagem.
    :param mensagem: mensagem-título
    :param form: (opcional) padronizado para uma mensagem centralizada
    em 40 espaços. Caso tenha valor True formata de acordo com o tamanho
    da mensagem
    :return: sem retorno
    """
    if form:
        tam_msg = len(mensagem) + 4
        imp_linha(tam_msg)
        print(f'  {mensagem}')
        imp_linha(tam_msg)
    else:
        imp_linha()
        print(f'{mensagem:^40}')
        imp_linha()

def leiaInt(mensagem):
    """
    -> Lê um número inteiro válido.
    :param mensagem: prompt para o usuário.
    :return: retorna um número inteiro. Retorna 0 em caso de interrupção
    do programa.
    """
    while True:
        try:
            n = int(input(mensagem))
        except ValueError:
            print(colorir('ERRO: digite um número inteiro válido.', 'verm'))
        except KeyboardInterrupt:
            print(colorir('O usuário preferiu não digitar.', 'verm'))
            return 0
        except Exception as erro:
            print(colorir(f'ERRO do tipo {erro.__class__}.', 'verm'))
        else:
            return n
