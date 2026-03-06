#=========== Desafio 73 ===========

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense (ou outro time à sua 
# escolha).

brasileirao_2026 = ('RB Bragantino', 'Palmeiras', 'Mirassol', 'São Paulo', 
                    'Botafogo', 'Chapecoense', 'Grêmio', 'Fluminense', 'Bahia',
                    'Athletico PR', 'Vitória', 'Atlético MG', 'Flamerda', 
                    'Internacional', 'Santos', 'Remo', 'Vasco', 'Corinthians', 
                    'Coritiba', 'Cruzeiro')

# A)
print(f'\nOs 5 primeiros colocados: {brasileirao_2026[:5]}')

# B)
print(f'\nOs 4 últimos colocados: {brasileirao_2026[-4:]}')

# C)
print(f'\nClubes organizados em ordem alfabética: {sorted(brasileirao_2026)}')

# D)
pos_gremio = brasileirao_2026.index('Grêmio') + 1
print(f'\nPosição do Grêmio na tabela: {pos_gremio}º')