#=========== Desafio 26 ===========
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em 
# que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace('Á', 'A')
frase = frase.replace('À', 'A')
frase = frase.replace('Ã', 'A')
frase = frase.replace('Â', 'A')

print(f"A letra 'A' aparece {frase.count('A')} na frase.")
aparicao1 = frase.find('A')
print(f"Posição do primeiro 'A' (0 se não houver): {aparicao1 + 1}")
aparicao_ultimo = frase.rfind('A')
print(f"Posição do último 'A'(0 se não houver): {aparicao_ultimo  + 1}")