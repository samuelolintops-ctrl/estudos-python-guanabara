#=========== Desafio 03 ===========
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
soma = num1 + num2

# Para descobrir o tipo da variável:
# print(type(num1))

print("A soma entre", num1, "e", num2, "é", soma)

# Outra forma de printar a soma, sem o uso da virgula, é usando o 'f' após abrir parenteses e
# antes das aspas. Assim, depois, basta colocar a (s) variável (eis) dentro de de chaves '{}'
# O comando seria:
print(f"A soma entre {num1} e {num2} é {soma}")