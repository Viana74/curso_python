"""
Tipos de dados "primitivos"
str - string (textos dentro de aspas simples/duplas)
int - inteiro (123456,-10, -20,1000,0,...)
float - flutuante (1.2,-4.3,3.3,...-0.5)
bool - valor booleano (0/1)
"""

print('Éverton', type('Everton'))  # Retorna a classe que é str
print(11,type(11))  # Retorna a classe que é int
print(1.1, type(1.1))  # Retorna a classe que é float
print(10 == 10,type(10 == 10))  # Retorna a classe que é bool
print('L' == 'L',type('L' == 'L'))  # Retorna a classe que é bool
print('L' == 'l',type('L' == 'l'))  # Retorna a classe que é bool

print(bool(''))  #String vazia é avaliada como false

print('Everton',type('Everton'), bool('Éverton')) #Qualquer valor dentro da string é avaliado como true


print('10',type('10'), type(int('10')))

print('Éverton', float('10.2')) #converte string para float

print('10' + '10')  #Concatena

print(10+10)  #Soma

"""
Exercício
"""

# print nome
print('Everton Viana', type('Éverton Viana'))

# print idade
print(35, type(35))

# print altura
print(1.78, type(1.78))

# print se é maior de idade
print(35>18, bool(35 > 20))