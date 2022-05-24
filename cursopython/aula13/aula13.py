"""
len - Quantidade de caracteres
obs.: Esta função não funciona com tipos numericos
"""

"""
usuario = input('Digite o seu nome: ')
qtd_carac = len(usuario)

print(usuario, qtd_carac, type(qtd_carac))

if qtd_carac < 6:
    print('A quantidade de caracteres é menor que 6')
else:
    print(f'A quantidade de caracteres é {qtd_carac}')
"""

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

#print(f'A quantidade total de caracteres foi {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__()) #Varios metodos dentro da string
