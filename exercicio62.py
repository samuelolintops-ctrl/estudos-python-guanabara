#=========== Desafio 62 ===========
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará 
# quando ele disser que quer mostrar 0 termos.

print("\nDescobrindo os 10 primeiros termos de uma P.A.: ")
prim_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = prim_termo
mais = 10
total = 0
cont = 1

while mais > 0:
    total += mais
    while cont <= total:
        print(f"{termo} ", end = '')
        print('-> ' if cont < total else '', end = '')
        termo += razao
        cont+= 1
    mais = int(input("\nDeseja mostrar mais quantos termos? "))
print(f"P.A. finalizada com {total} termos mostrados.")