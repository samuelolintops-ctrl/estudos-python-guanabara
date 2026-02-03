#=========== Desafio 24 ===========
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome da cidade: ")).strip()

cidade_split = cidade.split(' ', 1)
cidade_split = cidade_split[0].upper()
print(f"A cidade começa com 'SANTO' (-1 para não e 0 para sim): {cidade_split.find('SANTO')}")

# Forma mais fácil de resolver:
cidade = str(input("Digite o nome da cidade: ")).strip().upper()
print(f"A cidade começa com 'SANTO'? {cidade[:5] == 'SANTO'}")
