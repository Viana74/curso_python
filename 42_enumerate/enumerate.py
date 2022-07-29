"""
enumerate - enumera os elementos de uma lista
"""

         # 0      1        2
lista = [
        ['Chico', 'Juvenal', 'Joao'], # 0
        ['Maria', 'Aline', 'Jose'], # 1
        ['Marina', 'Jair', 'Luis'] #2
        ]

print(lista[1]) # Chico, Juvenal, Joao

print(lista[1][2]) # Jose


enumerada = list(enumerate(lista))
# Exibe tuplas (valor enumerado + lista):
# Tupla 1: [(0, ['Chico', 'Juvenal', 'Joao'])
# Tupla 2: [(1, ['Maria', 'Aline', 'Jose'])
# Tupla 3: [(2, ['Marina', 'Jair', 'Luis'])

#print(list(enumerada)) # cast from enumerate to list

print(enumerada[1][1][2])


# Enumerar a partir de um valor qualquer

for v1, v2 in enumerate(lista, 53):
        print(v1, v2)