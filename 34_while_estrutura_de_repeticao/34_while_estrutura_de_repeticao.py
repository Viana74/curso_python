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