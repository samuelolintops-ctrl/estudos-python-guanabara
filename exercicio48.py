#=========== Desafio 48 ===========
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram 
# no intervalo de 1 até 500.

print("Soma de todos os ímpares múltiplos de 3 entre 1 e 500:")
soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        contador += 1
print(f"Quantidade de ímpares divisíveis por 3: {contador}\nResultado: {soma}")

'''Para economizar processos do computador, poderia ter otimizado esse programa dessa forma:
print("Soma de todos os ímpares múltiplos de 3 entre 1 e 500:")
soma = 0
# Começa no 3, vai até 500, pula de 6 em 6
for i in range(3, 501, 6):
    soma += i
print(f"Resultado: {soma}")'''