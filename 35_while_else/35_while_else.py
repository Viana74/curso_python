"""
While / Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 100:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')

"""
while True:
    nome = input("Qual o seu nome?")
    print(f'Olá {nome}!')  #Nunca sai daqui

print(f'Essa expressão não será executada, pois está fora do bloco do while')

x = 0
while x < 100:
    print(x)
    x = x + 1

print('Acabou')
"""

"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue #pula para o próximo bloco de código (laço)

    print(x)
    x = x + 1

print('Acabou')
"""

"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break #sai do bloco de código

    print(x)
    x = x + 1

print('Acabou')
"""

"""
x = 0 # coluna
y = 0 # linha

while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1 # y = y + 1
    x += 1 # x = x + 1
"""