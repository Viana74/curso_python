"""
Crie uma função1 que receba uma função2 como parametro e retorne o valor da função 2 executada
"""

def f2(a,b):
    return a+b

def f1(f2):
    return f2(a,b)


a = 1
b = 2
print(f1(f2))


"""
Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
Faça a funcao1 executar duas funcoes que recebam um numero diferente de argumentos
"""

def f5(c,d,e):
    return c+d+e

def f4(a,b):
    return a+b

def f6(f4,f5):
    return f4(a,b)+f5(c,d,e)


a = 1
b = 2
c = 3
d = 4
e = 5
print(f6(f4,f5))