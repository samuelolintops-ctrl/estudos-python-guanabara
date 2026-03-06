#=========== Desafio 72 ===========

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
             'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input("Digite um valor qualquer no intervalo de 0 a 20: "))
        if num >= 0 and num <= 20:
            break
        print('\n' '\033[31mValor digitado inválido! Digite um número entre 0 ' 
            'e 20.\033[m')
    
    print(f'\n{num} por extenso é {contagem[num]}.')

    while True:
        opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[31mDigite uma opção válida! S ou N.\033[m')
    
    if opcao == 'N':
        break
print('\nFim do programa! Até mais.')