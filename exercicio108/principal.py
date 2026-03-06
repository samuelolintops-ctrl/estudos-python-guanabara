#=========== Desafio 108 ===========

# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado
# (ex: R$ 10,00).

import moeda

n = float(input('Digite um valor: '))
print(f'Aumentando em 15% o valor {moeda.moeda(n)}: '
      f'{moeda.moeda(moeda.aumentar(n, 15))}')
print(f'Diminuindo em 15% o valor {moeda.moeda(n)}: '
      f'{moeda.moeda(moeda.diminuir(n, 15))}')
print(f'O dobro de {moeda.moeda(n)}: {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)}: {moeda.moeda(moeda.metade(n))}')
