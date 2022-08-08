
#ex1
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1] #joga cada valor iterado de l1 em variavel e cria uma nova lista
print(l2)


#ex2
l3 = [v * 2 for v in l1]
print(l3)

#ex3
l4 = [(v,v2) for v in l1 for v2 in range(3)] #um for para cada "v", formando uma tupla
print(l4)

#ex4
l5 = ['Luiz', 'Mauro', 'Maria']
l6 = [v.replace('a','@').upper() for v in l5]
print(l6)

#ex5
tupla = (
    ('chave','valor'),
    ('chave2','valor2'),
)

l7 = [(y,x) for x,y in tupla]
print(l7) #inverte a ordem


#ex6
l8 = list(range(100))
l9 = [v for v in l8 if v % 2 == 0] #Todos os numeros divisiveis por 2
print(l9)


#ex7
l10 = list(range(100))
l11 = [v for v in l8 if v % 3 == 0 if v % 8 == 0] #Todos os numeros divisiveis por 3 e 8
print(l11)

#ex8
l12 = [v if v % 3 == 0 else 'Não é' for v in l10] #usando else
print(l12)

#exe9
l13 = [v if v % 3 == 0 and v % 8 == 0 else 'Não é' for v in l10] #usando else
print(l13)