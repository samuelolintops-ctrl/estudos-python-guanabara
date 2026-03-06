#=========== Desafio 103 ===========

# Faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O 
# programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente (ou tenha ficado vazio).

def ficha(nome='<desconhecido>', gols=0):
    """
    Imprime uma ficha com nome do jogador e quantidade de gols que ele marcou.
    :param nome: (opcional) nome do jogador
    :param gols: (opcional) quantidade de gols do jogador
    :return: sem retorno
    """
    titulo = 'FICHA DO JOGADOR'
    prim_nome = nome.split()[0]
    print('=' * (len(titulo + prim_nome) + 5))
    print(f'  {titulo} {prim_nome.upper()}')
    print(f'Nome: {nome}.')
    print(f'Gols marcados: {gols}.')


# Programa principal
nome_jog = str(input('Digite o nome do jogador: ')).strip().title()
qtd_gols = str(input('Quantidade de gols marcados: ')).strip()
if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0
if nome_jog == '':
    ficha(gols=qtd_gols)
else:
    ficha(nome_jog, qtd_gols)
