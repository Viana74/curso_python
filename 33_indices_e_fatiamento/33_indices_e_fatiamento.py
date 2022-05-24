"""
Manipulando strings
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

Você pode conferir tudo isso em:
http://docs.python.org/3/library/stdtypes.html (tipos buit-in)
http://docs.python.org/3/library/functions.html (funções buit-in)
"""

# positivos [012345678]
texto = 'Python s2'
print(texto[2])  #indice 2 que é a letra t
print(texto[6])  #indice 6 que é vazio
#print(texto[9])  #indice 9 que nao existe, logo dá erro

print(texto[2:6]) #fatiamento [inicio:fim]
print(texto[:6])  #fatiamento com inicio implicíto [:fim]
print(texto[7:])  #fatiamento com fim implicíto [início:]

#negativos -[9876543210]
url = 'www.google.com.br/'
print(url)  #com a barra
print(url[:-1])  #Excluindo a barra

#usando negativos
nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-1]  #Exclui o 2 do fim
print(nova_string)


nova_string = texto[:6:2]  #Do 0 ao 6 pulando de 2 em 2
print(nova_string)

texto = 'Python_s2'
nova_string = texto[::3]  #Do 0 ao 6 pulando de 3 em 3
print(nova_string)

print( len(url) )