#=========== Desafio 112 ===========

# Dentro do pacote dado que você criou no desafio 111, crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma
# validação de dados para aceitar apenas valores que sejam monetários
# (aceitando vírgula e ponto).

from utilidadesCeV import moeda, dado

n = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(n, 20, 30)
