"""
Funções - def em Python (Parte 1)
"""

"""
def funcao():
    print('Olá mundo!')

funcao()
funcao()
funcao()
"""

"""
def funcao(msg):
    print(msg)

funcao('cu')
funcao('cuu')
funcao('cuuu')
"""

"""
def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Luiz')
saudacao('Oi', 'Maria')
saudacao('Bom dia', 'José')
"""

"""
# Funcao com msg e nome Padrão
def saudacao(msg='E ai', nome='Cicrano'):
    nome = nome.replace('e', '3') # Replace
    msg = msg.replace('e', '3') # Replace
    print(msg, nome)

saudacao() # Sem agumento, ok porque tem padrão
saudacao(nome='Zezinho')
saudacao(nome='Zezinho', msg='Falllaa') # invertido mas definido
saudacao('Olá', 'Luiz')
saudacao('Oi', 'Maria')
saudacao('Bom dia', 'José')
"""


# Funcao com msg e nome Padrão
def saudacao(msg='E ai', nome='Cicrano'):
    #nome = nome.replace('e', '3') # Replace
    #msg = msg.replace('e', '3') # Replace
    return f'{msg} {nome}'

variavel = saudacao('Oi', 'Fulano') # Sem agumento, ok porque tem padrão
print(variavel)