#=========== Desafio 18 ===========
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

print("Descobrindo o seno, cosseno e tangente de um ângulo.")
ang = float(input("Digite o ângulo: "))
ang_rad = radians(ang)
val_sen = sin(ang_rad)
val_cos = cos(ang_rad)
val_tg = tan(ang_rad)

print("\nO seu angulo tem:")
print(f"- o SENO de {val_sen:.3f};\n- o COSSENO de {val_cos:.3f};\n- a TANGENTE de {val_tg:.3f}.")