#=========== Desafio 04 ===========
val = input("Digite algo e obtenha as informações sobre: ")

print("Tipo:", type(val))
print("É numérico:", val.isnumeric())
print("É uma letra:", val.isalpha())
print("É uma letra/número:", val.isalnum())
print("É ASCII:", val.isascii()) # Verifica se contém apenas caracteres da tabela ASCII (sem acentos complexos ou emojis)
print("É decimal:", val.isdecimal()) # Verifica se contém apenas dígitos decimais (0-9)
print("É um dígito:", val.isdigit()) # Similar ao decimal, mas aceita subscritos e outros dígitos especiais
print("É um identificador:", val.isidentifier()) # Verifica se pode ser um nome de variável válido no Python
print("É um título:", val.istitle()) # Verifica se cada palavra começa com maiúscula (Ex: "Olá Mundo")
print("É apenas espaço:", val.isspace()) # Verifica se a string contém apenas espaços, tabs ou quebras de linha
print("É maiúsculo:", val.isupper())
print("É minúsculo:", val.islower())
print("É printável:", val.isprintable()) # Verifica se não há caracteres invisíveis (como o comando de nova linha \n)