# Tuplas não pode adicionar, modificar ou remover elementos
t1 = ()

print(type(t1))
t2 = (1,2,3,'a','Eu')
print(t2)
print(t2[4])

for v in t2:
    print(v)

print(t2[2:])

#############################################
# criar uma tupla sem os parenteses

t3 = 1,2,3,'a','b'
print(type(t3))


#############################################
#tupla unica
t4 = 1 #vai ser um inteiro
print(type(t4))
t4 = 1, #apenas adiciono uma virgula para deixar de ser inteiro
print(type(t4))



#############################################
#Concatenar tuplas
t1 = 1,2,'Luiz',4,5
t2 = 6,7,8,9,10
t3 = t1 + t2
print(t3)


#############################################
#Desempacotar em variaveis

n1, n2, n3, *_, n10 = t3 # resto igual a Luiz e a ultima em n10

print(n10)


#############################################
#Multiplica a tupla
t1 = (1,2,3,'a','Eu') * 20
print(t1)


#############################################
#Converter a tupla em lista
t1 = (1,2,3,'a','Eu') 
print(type(t1))
t1 = list(t1)
print(type(t1))
t1[1] = 3000

print(t1)

t1 = tuple(t1)
print(type(t1))
print(t1)