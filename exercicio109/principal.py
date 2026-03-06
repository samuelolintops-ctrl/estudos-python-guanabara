#=========== Desafio 109 ===========

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

n = float(input('Digite um valor: '))
print(f'Aumentando em 15% o valor {moeda.moeda(n)}: '
      f'{moeda.aumentar(n, 15, True)}')
print(f'Diminuindo em 15% o valor {moeda.moeda(n)}: '
      f'{moeda.diminuir(n, 15, True)}')
print(f'O dobro de {moeda.moeda(n)}: {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)}: {moeda.metade(n, True)}')
