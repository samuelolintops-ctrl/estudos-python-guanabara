#=========== Desafio 83 ===========

# Crie um programa onde o usuário digite uma expressão qualquer que use 
# parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

print('=' * 40)
print(f'{"VALIDANDO EXPRESSÕES":^40}')
print('=' * 40)

expressao = str(input('Digite a expressão: ')).strip()
pilha = []
for caracter in expressao:
    if caracter == '(':
        pilha.append(caracter)
    elif caracter == ')':
        if len(pilha) == 0:
            pilha.append(caracter)
            break
        else:
            pilha.pop()

tam_pilha = len(pilha)
if tam_pilha == 0:
    print('\n' '\033[32mSua expressão é VÁLIDA!\033[m')
else:
    print('\n' '\033[31mSua expressão é INVÁLIDA!\033[m')
