"""
Funções - def em Python (Parte 2)
"""

"""
def funcao(var):
    return #return var

variavel = funcao('Mensagem')

if variavel:
    print(variavel)
else:
    print('Nenhum valor retornado da funcao.')
"""

"""
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1/n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta invalida.')
"""
"""
def dumb():
    return [1,2,3,4,5]

var = dumb()
print(var, type(var))
"""

"""
def f(var):
    print(var)

def dumb():
    return f # Sem os parenteses, a função não é executada

print(f, type(f))

var = dumb()
print(var, type(var))

print(id(var), id(f)) #var e f sao os mesmos objetos na memoria
"""

# Tuplas
# tuplas são listas que não podem ser alteradas
def dumb():
    return('Luiz', 'Otavio')

var=dumb()

print(var,type(var))