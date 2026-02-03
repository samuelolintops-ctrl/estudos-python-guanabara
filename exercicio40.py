#=========== Desafio 40 ===========
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo 
# com a média atingida:
# - Média abaixo de 5,0: REPROVADO
# - Média entre 5,0 e 6,9: RECUPERAÇÃO
# - Média 7,0 ou superior: APROVADO 

print("Digite suas duas notas e obtenha sua sua situação")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("\nVocê está \033[31mREPROVADO\033[m!")
elif media > 5 and media < 7:
    print("\nVocê está de \033[33mRECUPERAÇÃO\033[m!")
elif media > 7 and media <= 10:
    print("\nVocê está \033[32mAPROVADO\033[m!")
else:
    print("\n", "\033[31mMédia acima de 10, verifique se digitou as notas corretamente!\033[m!")