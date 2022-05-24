
#        0123456789......................33
frase = 'O rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)

contador = 0
nova_string = ''

"""

while contador < tamanho_frase:
    #print(contador, frase[contador])
    nova_string += frase[contador]
    print(contador, nova_string)
    contador += 1
"""

"""
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1
print(nova_string)
"""

input_do_usuario = input('Qual letra você deseja colocar maiuscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)