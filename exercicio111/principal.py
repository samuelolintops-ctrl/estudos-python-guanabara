#=========== Desafio 111 ===========

# Crie um pacote chamado utilidadesCeV que tenha dois pacotes internos chamados
# moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 
# 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

n = float(input('Digite um valor: '))
moeda.resumo(n, 20, 30)
