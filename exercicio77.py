#=========== Desafio 77 ===========

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('COPA', 'DECIMAL', 'ESPERAR', 'TERMO', 'PORTA', 'TEMPO', 'PARASITA', 
         'LOMBAR', 'PROGRAMAR', 'LISTA', 'CINCO', 'LONTRA', 'PATO', 'DEZ',
         'IGNORAR', 'MORTE', 'MAIOR', 'MENOR', 'IGUAL', 'FATAL', 'PONTE', 'TCC')

for n in tupla:
    if 'A' in n or 'E' in n or 'I'in n or 'O' in n or 'U'in n:
        print(f'Vogais em {n}: ', end = '')
        for vogal in n:
            if vogal in 'AEIOU':
                print(vogal, end = ' ')
        print()
    else:
        print(f'Não há vogais em {n}.')
