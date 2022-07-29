"""
Funções (def) em Python - *args **kwargs
"""
"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None): #nome com default=none. Se vier argumento depois, tem que ter default
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Luiz', a6=7) # uma vez chamado um argumento nomeado, os que vem depois também devem ser nomeados

print(var)

"""

def func(*args):
    print(args) #exibe uma tupla, que é igual a uma lista, porém, que não pode ser alterada.
    print(args[0])
    print(args[-1])
    print(len(args))

    args= list(args)
    #args[0] = 20 #TypeError: 'tuple' object does not support item assignment
    print(args) #agora é uma lista

lista1 = [1,2,3,4,5]
#n1, n2, *n = lista #Desempacotando a list em n1 e n2 e empacotando o restante em n através de n*
#print(n1, n2, n)
print(*lista1) # é igual a print(1,2,3,4,5)
print(*lista1,sep='-')

func(*lista1, 6) #Estou enviando a lista desempacotada

lista2 =[6,7,8,9,10]
func(*lista1, *lista2) #mesclando as listas


def func2(*args, **kwargs): #usando key words
    print(args)
    #print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')
    print(nome)

    idade=kwargs.get('idade')
    if idade is None:
        print("Esse argumento nao foi passado")
    else:
        print(idade)

lista3 =[10,20,30,40,50]
lista4 =[60,70,80,90,100]
func2(*lista3, *lista4, nome='Ze', sobrenome='Luiz')
func2(*lista3, *lista4, nome='Ze', sobrenome='Luiz', idade='60')