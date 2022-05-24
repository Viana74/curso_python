"""
Operadores lógicos
and, or, not
in e not in
"""

# verdadeiro E verdadeiro = verdadeiro
#comp1 and compa2

# verdadeiro OU verdadeiro = verdadeiro
#comp1 or compa2


# not
"""
a = 2
b = 3

if not b > a:
    print('b é maior que a')
else:
    print('a é maior que b')
"""

"""
b = 1

if not b:
    print('Digite um valor não nulo para b')
"""

"""
nome = 'Éverton'

if 'ver' in nome:
    print('Existe')
else:
    print('Não existe')
"""

"""
nome = 'Éverton'

if 'C' not in nome:
    print('Não existe')
else:
    print('Existe')
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuario: ')

usuario_bd = 'everton'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema!')
else:
    print('Usuário ou senha inválidos!')