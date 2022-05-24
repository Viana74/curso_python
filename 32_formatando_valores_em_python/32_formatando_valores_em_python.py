"""
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiro (int)
:f - numero de ponto flutuante
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)

< Esq.
> Dir.
^ Centro
"""

"""
num_1 = 10
num_2 = 3

div = num_1/num_2
# casas decimais e um numero de ponto flutuante
print('{:.2f}'.format(div))  #1a opcao: com funcao format
print(f'{div:.2f}')  #2a opcao com fstrings


nome = 'Everton Viana'
print(f'{nome:s}')  #somente falando que é uma string
"""

"""
num_1 = 1
print(f'{num_1:0>10}')  #numero com 10 casas. Neste caso preenche com 0 à esquerda até 10 caracteres (9 zeros)


num_2 = 1150
print(f'{num_2:0>10}')  #Preenche com 6 zeros à esquerda

num_2 = 1150
print(f'{num_2:0^10}')  #Prenche com 0 a esquerda e direita, i.e., 1150 no centro e 3 zeros para cada lado

num_2 = 1150
print(f'{num_2:0<10}')  #Preenche com 6 zeros à direita

num_2 = 1150
print(f'{num_2:.2f}')  #Formatado como float, i.e., casas decimais

num_2 = 1150
print(f'{num_2:0>10.2f}')  #Preenche com 3 zeros para completar 10 caracteres (4 digitos do 1150+ponto+2 casas decimais=7 caractestes)

nome = 'Otavio Miranda'
nro = int((50-len(nome))/2)
print(f'{nome:#^{nro}}')

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome_formatado = '{:@>14}'.format(nome) #Nada acontece pq a variavel já tem 14 caracteres
print(nome_formatado)

nome_formatado = '{:@>15}'.format(nome) #adiciona 1 @ a esquerda da variavel
print(nome_formatado)

nome_formatado = '{n:0<20}'.format(n=nome) #adiciona 1 @ a esquerda da variavel
print(nome_formatado)

"""


#"""
nome = 'Otavio'
sobrenome = 'Miranda'

nome_formatado = '{0} {1:#^50}'.format(nome, sobrenome)  #Formata somente o sobrenome
print(nome_formatado)
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome) #Formata nome e sobrenome
print(nome_formatado)

print(nome.ljust(10, '#'))  #Método que justifica o nome à esquerda e preenche com #
print(nome.lower()) #Método para tudo minusculo
print(nome.upper()) #Método para tudo maiusculo
nome = 'LuIz OtAvIo MiRaNdA'  #nome Bagunçado
print(nome.title()) #Método para só as primeiras maiusculas
#"""