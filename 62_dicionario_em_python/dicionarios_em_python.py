"""
Nas listas o python gera um indice automaticamente
No dicionario você controla o indice, preciso inserir uma chave (indice) e valor

d1 = {'chave': 'valor'}
"""

d1 = {'chave1':'valor da chave'}
print(d1)

#Adicionando uma nova chave:
d1['nova_chave'] = 'valor da nova chave'

#Tudo que tem dentro de colchetes é o indice da lista
print(d1['chave1'])
print(d1['nova_chave'])


################################################################
d2 = dict(chave1='valor da chave1', chave2='valor da chave 2')
d2['chave3'] = 'valor da chave 3'

print(d2)

################################################################
d3 = {1:'valor da chave1', 2:'valor da chave 2', 3:'valor da chave 3'}

print(d3)

#Achave deve ser única, caso contrario, preserva o ultimo valor conforme exemplo abaixo:
d4 = {1:'valor da chave1', 2:'valor da chave 2', 2:'valor da chave 3'}
print(d4)


#################################################################
#Posso usar qualquer dado imutavel como chave:
# string, inteiros, tuplas...

d5 = {
    'str' : 'valor_string',
    123 : 'valor_inteiro',
    (1,2,3) : 'valor da tupla',
}

print(d5[(1,2,3)]) #chave especifica
print(d5)


##################################################################
#print(d5['chave nao existe') #chave inexistente. python lanca uma excessao

d5['chave nao existe'] = 'Valor da chave nao existe'

if 'chave nao existe' in d5:
    print(d5['chave nao existe'])

print('Ola')


##################################################################
#Usando get
if d5.get('chave nao existe') is not None:
    print(d5.get('chave nao existe'))

print(123)

d5.update({'nova_chave':'novo_valor'})
print(d5)


#########################################################
#Metodo mais simples para incluir/excluir valor

d6 = {
    'str' : 'string',
    123 : 'inteiro',
    (1,2,3) : 'tupla',
    1.6 : 'float'
}

#exclusao
del d6['str']
print('str' in d6) #dá False pq  foi excluido
print('tupla' in d6.values()) #dá True pois existe um valor chamado tupla
print(1.6 in d6.keys()) #dá True pois existe uma chave 1.6

print(len(d6)) #Mostra quantos pares (chave/valor) existe em d6


d7 = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3',
    'chave4' : 'valor4'
}

for k in d7:
    print(k)


for v in d7.values():
    print(v)

#Modo 1
for k in d7.items():
    print(k)

#Modo 2
for k in d7.items():
    print(k[0],k[1])

#Modo 3
for k,v in d7.items():
    print(k,v)

#################################################################
#Dicionarios dentro de dicionarios
cliente = {
    'cliente1' : {
      'nome' : 'Luiz',
      'sobrenome' : 'Otavio'
    },
    'cliente2': {
        'nome': 'Joao',
        'sobrenome': 'Moreira'
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira'
    },
}

for clientes_k, clientes_v in cliente.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


###################################################################
d1 = {1: 'a', 2 : 'b', 3 : 'c'}
v = d1

#sao identicos
print(d1)
print(v)


#Em python altera os dois dicionarios, o sinal de igual não cria um novo objeto
#ambos apontam para a mesma localizacao da memoria (tipo ponteiro)
v[1] = 'Luiz'
print(d1)
print(v)

#copia rasa
v = d1.copy()
v[1] = 'a'
print(d1)
print(v)


d1 = {1:'a', 2:'b', 3:'c', 'd':['Luiz', 'Otavio']}
v = d1.copy()

v[1] = 'Luiz'
#print(v['d'][0])# print na chave d indice0

#altera nos dois
v['d'][0] = 'Joaozinho'
print(d1)
print(v)
#Se d for uma tupla, ela nao pode ser alterada, pois tupla e imutavel
#Neste caso teria que substuir a tupla em outra ou fazer cast para lista...

#usando o deep copy (cópia profunda)
import copy
d1 = {1:'a', 2:'b', 3:'c', 'd':['Luiz', 'Otavio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'][0] = 'Joaozinho'
print(d1)
print(v)


######################################################
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d1.pop(4) #elimina a chave 4
print(d1)
d1.popitem() #elimina o ultimo item independe de qual item
print(d1)

d2 = {
    'a': 'b',
    'c': 'd',
}

#Concatena os dicionarios
d1.update(d2)
print(d1)