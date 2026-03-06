import utilidades

def listar_cadastros(nome):
    # Verifica se o arquivo está vazio antes de listar
    with open(nome, 'r') as arquivo:
        tamanho = len(arquivo.read())
        if tamanho == 0:
            print('Nenhum cadastro realizado!')
            return
    
    utilidades.cabecalho('CADASTROS')
    print(f'{"NOME":<35}' f'{"IDADE"}')
    with open(nome, 'r') as arquivo:
        for p in arquivo.readlines():
            p = p.replace('\n', '').split(';')
            if len(p) == 2:
                print(f'{p[0]:<35}{p[1]:>4}')
