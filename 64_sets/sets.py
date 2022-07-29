"""
add (adiction), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
simetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

# A maior diferenca entre os sets e as listas/tuplas/dicionarios é que o sets só suporta elementos unicos
# sets só recebem valores (não possuem chaves) e não possui indices, i.e., elementos unicos.
# Logo não é possivel acessar o valor diretamente

s1 = {1,2,3,4,5,6}
print(s1)

s1 = {} #em branco assim é um dicionario
s1 = set() #agora sim, crio um set em branco

#add
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
print(s2)

#discard
s2.discard(3) #remove a tupla
print(s2)

#update
s2.update('Python') #similar a funcao add, recebe um iteravel e itera sobre um elemento
print(s2) #note que não respeita ordem, aparece de forma aleatoria



s3 = set()
s3.update([1,2,3,4,5], {5,6,7,8,}) #adiciona uma lista e mais um conjunto
print(s3) #note que o sets não aceita itens duplicados, i.e., mantém somente 1 elemento de cada


l1 = [1,2,1,3,4,5,6,6,6,6,6,6,7,7,7,7,7,8,9,9,9,9,'egg', 'egg']
l1 = set(l1) #fazendo um casting os itens repetidos são omitidos
print(l1)

l1 = list(l1) #faço novamente um cast, pode ser que os elementos venham fora de ordem
print(l1)
print(l1[-1])

#union
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}

s3 = s1 | s2
print(s3)


#intersection
s4 = s1 & s2
print(s4)

#difference
s1 = {1,2,3,4,5,7}
s5 = s1 - s2 #mostra apenas os elementos que estão no set da esquerda
print(s5)

#simetric difference
s6 = s2 ^ s1
print(s6) #pega o 6 e o 7


l1 = ['egg', 'potato', 'onion']
l2 = ['egg', 'potato', 'onion', 'onion', 'potato', 'potato']
print(l1 == l2) # False: são diferentes

l1 = set(l1)
l2 = set(l2)

print(l1 == l2) #True: agora sao iguais

