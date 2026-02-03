#=========== Desafio 20 ===========
# O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# Há duas maneiras de fazer esse exercício, usando a função sample (que eu usei) e a função shuffle (que o professor usou)

from random import sample, shuffle

aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))

ordem = sample((aluno1, aluno2, aluno3, aluno4), k = 4) # Para usar o sample eu passo por parâmetro o que eu quero embaralhar e uma constante da quantidade de 
                                                        # itens que vão para a lista, neste caso 'ordem', e vão quatro dos itens que passei por parâmetro, ou seja,
                                                        # todos.

print(f"\nA ordem de apresentação será:\n{ordem}")

# Fazendo pelo método do professor a diferença é que que eu deveria criar uma lista (vetor) para armazenar aluno1, aluno2...
# No shuffle eu passo por parâmetro apenas a lista e essa função altera diretamente o conteúdo dela. Depois é só printar a lista.

ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)
print(f"\nA ordem de apresentação será:\n{ordem}")
