#=========== Desafio 25 ===========
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo: ")).strip().upper()

print(f"Você possui 'SILVA' no nome (0 para não e 1 para sim): {nome.count('SILVA')}")

# Outra forma de resolver:

print(f"Você possui 'SILVA' no nome? {'SILVA' in nome}")
