#=========== Desafio 107 ===========

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse
# módulo e use algumas dessas funções.

import moeda

n = float(input('Digite um valor: '))
print(f'Aumentando em 15% o valor RS{n:.2f}: RS{moeda.aumentar(n, 15):.2f}')
print(f'Diminuindo em 15% o valor RS{n:.2f}: RS{moeda.diminuir(n, 15):.2f}')
print(f'O dobro de RS{n:.2f}: RS{moeda.dobro(n):.2f}')
print(f'A metade de RS{n:.2f}: RS{moeda.metade(n):.2f}')
