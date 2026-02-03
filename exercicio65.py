#=========== Desafio 65 ===========
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos 
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não 
# continuar a digitar valores.

print("\nMédia e comparação de valores digitados")

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input("Digite um número (0 para encerrar): "))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Deseja continuar a digitar valores [S/N]? "))
    if resp not in 'SNsn':
        while resp not in 'SNsn':
            resp = str(input("Opção inválida, digite novamente: "))
media = soma / quant
print(f"\nMédia dos valores {quant} digitados: {media};\nMaior entre eles: {maior};\nMenor entre eles: {menor}.")