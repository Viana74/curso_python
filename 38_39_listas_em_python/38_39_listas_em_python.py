"""
Listas em Python
Fatiamento
append, inserir, pop, del, clear, extend, +
min, max
range
"""

texto = 'Valor'
#lista = [1, 2, 3, 4, 'Everton', 10.1, True] # Lista com diversos tipos, posso ter classes, funções, etc

"""
#         0    1    2    3    4
Lista = ['A', 'Bacana', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1

string = 'ABacanaCDE'

print(string[1]) #A string suporta somente 1 valor
print(Lista[1]) #A lista suporta diversos valores de varios tipos diferentes
print(Lista[-4]) #Indice negativo
print(Lista) #Lista inteira
"""

Lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(Lista)

Lista[5] = 'Qualquer outra coisa' # Substitui o 10.5 (flutuante) por uma string na Lista
print(Lista)


#Fatiamento
Lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(Lista[0:3]) #Não mostra o indice 3
#ou
print(Lista[:3])

print(Lista[-1]) #ultimo item da Lista
print(Lista[::2]) #pula de 2 em 2


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2 # Uma terceira lista concatenando l1 e l2
print(l1)

print('***** extende l1 com l2 *****')
l1.extend(l2)

print(l1)
print(l2)
print(l3)

print('*********** extend ***********')
l1 = [1,2,3]
l1.extend('a')
print(l1)

#Para isso pode-se usar o append que adiciona sempre no final da lista
print('*********** append ***********')
l2.append('b')
print(l2)

#Insert coloca em um indice específico
print('*********** Insert ***********')
l2 = [1,2,3]
print(l2)

l2.insert(1,'banana')
print(l2)

#pop elimina o ultimo elemento
print('********** pop ***************')
l2.pop()
print(l2)

print('********** del ***************')
l3 = [1,2,3,4,5,6,7,8,9]
print(l3)
del(l3[3:5]) #exclui os indices 4 e 5
print(l3)

print('********** insert e del ***********')
l3 = [1,2,3,4,5,6,7,8,9]
print(l3)
l3.insert(5,'abacate')
print(l3)
del(l3[5])
print(l3)

print('********** min e max ***********')
print(min(l3))
print(max(l3))

print('******** range e list ***********')
l2 = range(1,10)
print(l2)

l2 = list(range(1,10))
print(l2)

l2 = list(range(0,100,10))
print(l2)

print('******** iterando com o for ********')
l2 = [0,1,2,3,4,5,6,7,8,9]

for valor in l2:
    print(valor)

soma = 0
for valor in l2:
    soma = soma + valor
    print(soma)

l2 = ['String', True, 10, -10.1]
for elem in l2:
    print(f'O tipo do elemento {elem} é {type(elem)}')

print('****** jogo da Forca *********')
secreto = 'perfume'
digitadas = [] #lista vazia
teste = ['a']
chances = len(secreto)

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh, isso não vale!!! Digite apenas uma letra!')
        continue

    digitadas.append(letra)
    #print(digitadas)

    if letra in secreto:
        print(f'Uhuuu, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta!')
        digitadas.pop() #remove da lista de digitadas

    # substitui a letra no lugar o * se ela existir na palavra secreta
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print(f'Você ganhou! A palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')