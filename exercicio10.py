#=========== Desafio 10 ===========
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

val = float(input("Digite quanto você possui de dinheiro: "))
dol = 5.39
val_dol = val / dol

print(f"Com RS{val:.2f}, você pode comprar USS{val_dol:.2f}.")