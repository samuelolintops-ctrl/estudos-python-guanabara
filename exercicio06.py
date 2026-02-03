#=========== Desafio 06 ===========
# Crie um algoritmo que leia um número emostre o seu dobro, triplo e raíz quadrada

num = int(input("Digite um número inteiro: "))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)

print(f"Valor lido: {num}")
print(f"Dobro: {dob}; Triplo: {tri}; Raiz quadrada: {raiz:.2f}")