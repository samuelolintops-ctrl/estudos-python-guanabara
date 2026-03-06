#=========== Desafio 105 ===========

# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas.
# - A maior nota.
# - A menor nota.
# - A média da turma.
# - A situação (opcional: BOA, RAZOÁVEL ou RUIM).

def notas(*notas, sit=False):
    """
    Recebe qualquer quantidade de notas e retorna um dicionário com:
    - quantidade de notas;
    - maior nota;
    - menor nota;
    - média do aluno;
    - situação (opcional).
    :param notas: aceita qualquer quantidade de notas
    :param sit: (opcional) adiciona a situação do aluno
    :return: retorna um dicionário com alguns dados do aluno
    """
    qtd_notas = len(notas)
    if qtd_notas > 0:
        menor_nota = min(notas)
        maior_nota = max(notas)
        media = sum(notas) / qtd_notas
        alunos = {
            'quantidade_de_notas': qtd_notas,
            'menor_nota': menor_nota,
            'maior_nota': maior_nota,
            'media': media
        }
        if sit:
            if media >= 7:
                situacao = 'BOA'
            elif media >= 5:
                situacao = 'RAZOÁVEL'
            else:
                situacao = 'RUIM'
            alunos['situacao'] = situacao
    else:
        alunos = {'erro': 'nenhuma nota registrada'}
    return alunos


# Programa principal
alns = notas()
for k, v in alns.items():
    print(f'{k.replace("_", " ").capitalize()}: {v}')
