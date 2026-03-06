#=========== Desafio 106 ===========

# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
# 'FIM', o programa se encerrará.
# Obs: Use cores para destacar cada parte do sistema.

def imprime_titulo(mensagem, c='\033[42m'):
    tamanho_mensagem = len(mensagem) + 4
    print(c, end='')
    print('~' * tamanho_mensagem)
    print(f'  {mensagem}  ')
    print('~' * tamanho_mensagem, end='')
    print(cor["limpa"])

def ajuda(func_bib):
    from pydoc import render_doc
    from time import sleep
    manual = render_doc(func_bib)
    imprime_titulo(f'Manual da Função/Biblioteca {func_bib}', cor["azul"])
    sleep(2)
    print(f'{cor["bran"]}{manual}{cor["limpa"]}')
    sleep(2)


# Programa principal
cor = {
    'limpa': '\033[m',
    'verm': '\033[41m',
    'bran': '\033[7m',
    'verd': '\033[42m',
    'azul': '\033[44m',
    'amar': '\033[33m'
}
while True:
    imprime_titulo('AJUDA COM O COMANDOS DO PYTHON')
    comando = str(input(f'\n{cor["amar"]}>>> Função ou Biblioteca: [FIM '
                        f'para encerrar] {cor["limpa"]}')).strip().lower()
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
imprime_titulo('Fim do programa! Até mais.', cor['verm'])
