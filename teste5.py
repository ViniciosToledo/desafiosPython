# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


# RESOLUÇÃO
def inverte_string(string):
    nova_string = ''
    indice = len(string) - 1

    while indice >= 0:
        nova_string += string[indice]
        indice -= 1

    return nova_string


texto = str(input('Digite um texto: '))
print(inverte_string(texto))
