"""
split - dividir um string # str
join - juntar uma lista # str
enumerate - enumerar elementos da lista # lista (objeto iteráveis)
"""

string = "O Brasil é o o o o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

palavra = ' '
count = 0

#for valor in lista1:
#    print(f'A palavra "{valor}" apareceu {lista1.count(valor)}x na frase.')

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > count:
        count = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({count}x).')


for valor in lista2:
    print(valor.strip().capitalize())
    print(valor.strip().upper())

###########
# join

string = 'O Brasil é penta'
lista = string.split(' ')
print(lista)
string2 = ','.join(lista)


print(string)
print(lista)
print(string2)

###########
# enumerate
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice]) # valor = lista[valor]

list = [
    [1,2],
    [3,4],
    [5,6],
]

for v in list:
    print(v[0], v[1]) # mesmo print(v)

# desempacotamento sem o enumerate
list2 = [
    [0,'Joao'],
    [1,'Maria'],
    [2,'José'],
]

for indice, nome in list2:
    print(indice, nome) # mesmo print(v)

# Usando enumerate para desempacotar
list3 = ['Joao', 'Maria', 'José']
for indice, nome in enumerate(list3):
    print(indice, nome)


n1, n2, n3 = list3
print(n1)