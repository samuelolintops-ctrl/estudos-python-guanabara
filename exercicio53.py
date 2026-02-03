#=========== Desafio 53 ===========
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (frase que se lê igual de trás para 
# frente), desconsiderando os espaços.

'''
# Forma que eu fiz:
print("\n")
frase = str(input("Digite uma frase: ")).strip().upper().split()
frase = "".join(frase)

frase_comp = frase[::-1]

if frase_comp == frase:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo")
'''

# Versão corrigida (para o propósito de uso do for):

frase = str(input("Digite uma frase: ")).strip().upper().replace(" ", "")
invertida = ""
for letra in range(len(frase) - 1, -1, -1):
    invertida += frase[letra]
if invertida == frase:
    print("É um palíndromo")
else:
    print("Sua frase não é um palíndromo")
