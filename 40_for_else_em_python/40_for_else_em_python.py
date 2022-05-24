"""
FOR/ELSE em Python
"""

"""
variavel = ['Everton', 'Joao', 'Maria']

for item in variavel:
    if item.startswith('E'):
        print(f'{item} começa com E')
    else:
        print(f'{item} não começa com E')
    #break #sai do laco
    #continue #pula para a proxima iteracao do laco
"""
variavel = ['Everton', 'joao', 'Maria']
for valor in variavel:
    if valor.upper().startswith('J'): #Verifica se existe João ou joão, pois converte para maisucula primeiro
        break
else:
    print('Não existe uma palavra que começa com J.')