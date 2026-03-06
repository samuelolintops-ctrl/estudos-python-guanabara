cor = {
    'limpa': '\033[m',
    'verm': '\033[31m',
    'verd': '\033[32m',
    'amar': '\033[33m',
    'azul': '\033[34m',
    'mage': '\033[35m',
    'cian': '\033[36m'
}

def colorir(texto, c='limpa'):
    return f'{cor[c]}{texto}{cor["limpa"]}'