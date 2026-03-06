#=========== Desafio 95 ===========

# Aprimore o Desafio 93 para que ele funcione com vários jogadores, incluindo um
# sistema de visualização de detalhes do aproveitamento de cada jogador (como 
# você fez no boletim dos alunos).

print('=' * 40)
print(f'{"ORGANIZANDO DADOS DE JOGADORES":^40}')
print('=' * 40)
lista_jogadores = []
while True:
    print('\n(Apenas primeiro nome ou sobrenome abreviado)')
    nome = str(input('Nome do jogador: ')).strip().title()
    while True:
        print('(Máximo de 7 partidas)')
        qtd_partidas = int(input('Quantidade de partidas jogadas: '))
        if qtd_partidas < 7:
            break
        print('\033[31mQuantidade inválida (excedeu o limite imposto)!\033[m')
    gols = []
    for p in range(1, qtd_partidas + 1):
        gol_partida = int(input(f'Gols marcados na {p}º partida: '))
        gols.append(gol_partida)
    total_gols = sum(gols)
    aproveitamento = 0
    if qtd_partidas > 0:
        aproveitamento = total_gols / qtd_partidas
    dados_jogador = {
        'nome': nome,
        'partidas_jogadas': qtd_partidas,
        'gols': gols[:],
        'total_gols': total_gols,
        'aproveitamento': aproveitamento
    }
    lista_jogadores.append(dados_jogador.copy())
    dados_jogador.clear()
    print('\033[32mCadastro realizado com sucesso!\033[m')
    while True:
        opcao = str(input('Deseja continuar? [SIM/NÃO] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mOpção inválida! Digite SIM ou NÃO.\033[m')
    print('=' * 40)
    if opcao == 'N':
        break
print(f'{"COD":<4}', end='| ')
print(f'{"NOME":<10}', end='| ')
print(f'{"GOLS":<25}', end='| ')
print(f'{"TOTAL":<5}')
print('-' * 50)
for ind, val in enumerate(lista_jogadores):
    print(f'{ind:<4}', end='| ')
    print(f'{val["nome"]:<10}', end='| ')
    print(f'{str(val["gols"]):<25}', end='| ')
    print(f'{val["total_gols"]:<5}')
tam_lista = len(lista_jogadores)
while True:
    print('\nDigite o código para visualizar dados individuais.')
    indice = int(input('Código do jogador: [999 para encerrar] '))
    if indice == 999:
        break
    elif indice < 0 or indice >= tam_lista:
        print('\033[31mCódigo inválido! Digite novamente.\033[m')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista_jogadores[indice]["nome"]}:')
        for ind, val in enumerate(lista_jogadores[indice]['gols']):
            print(f' => Na {ind + 1}º partida fez {val} gols.')
print('\nPrograma encerrado! Até mais.')
