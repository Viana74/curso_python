"""
Desempacotamento de Listas em Python
"""

lista = ['Luiz','Joao','Maria']

n1, n2, n3 = lista

#n1, n2, = lista #Deu erro pq falta variável, então uso *qq_nome
n1, n2, *_ = lista #underline para ignorar os ultimos ou *, conforme abaixo
n1, n2, *outra_lista = lista #gera uma outra lista com os valores da lista

print(n1)
print(n2)
print(outra_lista)


#Exemplo
lista2 = ['Luiz','Joao','Maria',1,2,3,4,5,6,7,8,9,10]

n3, n4, *lista_nova = lista2
print(n3)
print(n4)
print(lista_nova)


n3, n4, *lista_nova, ultimo_da_lista = lista2
print(lista_nova) #até o 9
print(ultimo_da_lista) #somente o ultimo

#A mesma lógica vale para o começo
*lista_nova, n3, n4 = lista2
print(lista_nova)  #somente o começo, fora os dois ultimos
print(n3)
print(n4)