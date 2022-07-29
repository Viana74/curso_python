"""
Expressoes lambda - funcoes anonimas
ordenando listas dentro de listas
"""

# Funcao classica
def funcao(arg1, arg2):
    return arg1 * arg2

var = funcao(2,2)
print(var)

# Expressões Lambda ou funcoes anonimas
a = lambda x, y: x*y
print(a(2,2))


##############################

lista = [['P1',13], ['P2',6], ['P3',7], ['P4',50], ['P5',8]]

def func(item):
    return item[1]

#print(lista)

lista.sort(key=func) # ordenado pelo preço do produto mais barato para o mais caro
lista.sort(key=func, reverse=True) # ordenado pelo preço do produto do mais caro ao mais barato
print(lista)

#######
# Usando lambda (não precisa mais da funcao func)
lista.sort(key=lambda item: item[1], reverse=True) #ordena pelo preço do maior->menor
lista.sort(key=lambda item: item[1], reverse=False) #ordena pelo preço do menor->maior
print(lista)

# Usando sorted
print(sorted(lista, key=lambda i: i[0], reverse=True)) #ordenando pelo nome do maior->menor