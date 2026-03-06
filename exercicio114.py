#=========== Desafio 114 ===========

# Crie um código em Python que teste se o site Pudim (pudim.com.br) está
# acessível pelo computador usado no momento. Você precisará tratar a
# exceção caso o site esteja fora do ar ou o computador esteja sem
# internet.

from urllib.request import urlopen, Request
import urllib.error
try:
    # Criamos um "disfarce" (Header) de navegador
    headers = {'User-Agent': 'Mozilla/5.0'}
    requisicao = Request('http://www.pudim.com.br', headers=headers)
    site = urlopen(requisicao)
except urllib.error.URLError:
    # Erro de rede (internet caída ou site fora do ar)
    print('\033[31mO site Pudim não está acessível no momento!\033[m')
except Exception as erro:
    print(f'\033[31mErro inesperado: {erro.__class__}\033[m')
else:
    print('\033[32mConsegui acessar o site do pudim com sucesso!\033[m')

