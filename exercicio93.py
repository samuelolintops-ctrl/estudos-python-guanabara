#=========== Desafio 93 ===========

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O 
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai 
# ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
# guardado em um dicionário, incluindo o total de gols feitos durante o 
# campeonato.

print('=' * 40)
print(f'{"ORGANIZANDO DADOS DE UM JOGADOR":^40}')
print('=' * 40)
nome = str(input('\nNome do jogador: ')).strip().title()
qtd_partidas = int(input('Quantidade de partidas jogadas: '))
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
print('=' * 40)
print()
for k, v in dados_jogador.items():
    if k == 'aproveitamento':
        print(f'O campo {k} tem o valor {v:.1f}.')
    else:
        print(f'O campo {k} tem o valor {v}.')
print('=' * 40)
print()
for ind, val in enumerate(dados_jogador['gols']):
    print(f' => Na {ind + 1}º partida o jogador marcou {val} gols.')
print(f'O jogador marcou no total {total_gols} gols.')
