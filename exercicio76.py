#=========== Desafio 76 ===========

# Crie um programa que tenha uma tupla única com nomes de produtos e seus 
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

produtos = ('Banana', 3.50, 'Maçã', 5.79, 'Creme capilar', 27.99, 
            'Leite em pó 1kg', 51.65, 'Desodorante', 10.99, 'Vinho', 49.00,
            'Refigerante', 7.95, 'Arroz', 4.99, 'Feijão', 8.49,'Massa de bolo', 
            7.15)

print('=' * 44)
titulo = 'LISTAGEM DE PREÇOS'
print(f'{titulo:^44}')
print('=' * 44)

tam_tupla = len(produtos)
for n in range(0, tam_tupla, 2):
    print(f'{produtos[n]:.<35}', end = '')
    print('RS' + f'{produtos[n + 1]:>7.2f}')