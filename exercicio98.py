#=========== Desafio 98 ===========

# Faça um programa que tenha uma função chamada contador(), que receba três 
# parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
# através da função criada:
# De 1 até 10, de 1 em 1.
# De 10 até 0, de 2 em 2.
# Uma contagem personalizada (lendo do teclado).
# Nota: A função precisa lidar com passos negativos e passo 0 (que deve ser 
# tratado como 1).

from time import sleep

def contador(inicio, fim, passo):
    """
    Função que faz a contagem de um início até um fim especificados.
    Passo igual a zero é convertido para ser passo um.
    """
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'\nContando de {inicio} a {fim} de {passo} em {passo}.')
    sleep(2)
    if inicio < fim:
        for n in range(inicio, fim + 1, passo):
            print(f' {n} ', end='', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for n in range(inicio, fim - 1, (passo * -1)):
            print(f' {n} ', end='', flush=True)
            sleep(0.5)
        print('FIM!') 


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('\nAgora defina a contagem.')
while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    if inicio != fim:
        break
    print('\033[31mInício e fim iguais! Digite novamente.\033[m')
passo = int(input('Passo: '))
contador(inicio, fim, passo)
#-------------------------------------------------------------------------------