#=========== Desafio 46 ===========
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 
# até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

cor = {'limpa': '\033[m',
       'verm': '\033[31m',
       'verd': '\033[32m',
       'amar': '\033[33m',
       'azul': '\033[34m'}
print("Contagem regressiva para a queima de fogos de artifício!!")
sleep(1)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(f"""{cor['verm']} |/
-O-
/| {cor['limpa']}""")
sleep(0.5)
print(f"""{cor['verd']} |/
-O-
/| {cor['limpa']}""")
sleep(0.5)
print(f"""{cor['amar']} |/
-O-
/| {cor['limpa']}""")
sleep(0.5)
print(f"""{cor['azul']} |/
-O-
/| {cor['limpa']}""")
