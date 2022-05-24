"""
For in em Python
iterando strings com For
Função range(start=0, stop, step=1)
"""


"""
Com while é complexo
c = 0
texto = 'Python'
while c < len(texto):
    print(texto[c])
    c += 1
"""

# Jeito mais fácil
texto = 'Python'
nova_string = ''
for letra in texto:
    print(letra)

print('##########################')
print('Com enumerate')
for n, letra in enumerate(texto):
    print(n, letra)

print('##########################')
for n in range(10): # (0,10,1)
    print(n)

print('##########################')
# Acha os multiplos
for n in range(0, 100, 8):
    print(n)

print('##########################')
for n in range(100):
    if n % 8 == 0:
        print(n)

print('##########################')
for letra in texto:
    if letra == 't':
        #continue #vai para a próxima condição (elif)
        break
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break #sai do laço for
    else:
        nova_string += letra

print(nova_string)