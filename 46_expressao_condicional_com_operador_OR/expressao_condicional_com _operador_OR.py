nome = input('Qual o seu nome? ')

#Operacao classica
"""
if nome:
    print(nome)
else:
    print('Voce não digitou nada!')
"""

#Operador OR (forma simplificada de fazer uma condicao)
print(nome or 'Voce nao digitou nada!')

#print(nome or None or 0 or False or 'Voce nao digitou nada!')


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'A'

variavel = a or b or c or d or e or f or g
print(variavel) #Faz print do primeiro verdadeiro que encontrar