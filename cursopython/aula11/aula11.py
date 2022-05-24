"""
Operadores relacionais
== > >= < <= !=
"""

"""
print(2 == 4)
if (2 == 2):
    print('OK')
else:
    print('NAK')
"""

"""
num1 = 2  # int
num2 = '2'  # string
print(num1, num2)

print(num1 == num2)  # Tipos diferentes
"""

"""
num1 = 2  # int
num2 = 2  # int
expressao = num1 > num2  # A expressao é uma pergunta
print(expressao)
"""

"""
num1 = 3  # int
num2 = 2  # int
expressao = num1 > num2  # A expressao é uma pergunta
print(expressao)
"""

"""
num1 = 3  # int
num2 = 2  # int
expressao = num1 >= num2  # A expressao é uma pergunta
print(expressao)
"""

"""
num1 = 2  # int
num2 = 2  # int
expressao = num1 != num2  # A expressao é uma pergunta
print(expressao)
"""

"""
num1 = 2  # int
num2 = 4  # int
expressao = type(num1) == type(num2)  # A expressao é uma pergunta
print(expressao)
"""

"""
num1 = 2  # int
num2 = '4'  # string
expressao = type(num1) == type(int(num2))  # faço un cast antes
print(expressao)
"""


"""
idade_min = 18

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if (int(idade) >= idade_min):
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÂO pode pegar o empréstimo')
"""


idade_min = 18
idade_max = 30

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if (int(idade) >= idade_min) and (int(idade) <= idade_max):
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÂO pode pegar o empréstimo')