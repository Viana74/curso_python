"""
Operadores aritiméticos
+,-,*,/,//,**,%,()
"""

print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 8)
print('Multiplicão * ', 10 * 2)
print('Divisão / ', 10 / 5)

#####
# * como operador de repetição
print('Repetição com * ', 10 * '10')
print('Repetição com * ', 10 * 'k')

# + para concatenação
print('Everton' + ' ' + 'Viana e ele tem ' + str(35) + ' anos')

##########
print(10 // 3)  # Retorna a divisão inteira (arredonda)
print(10 / 3)   # Retorna um ponto flutuante
print(10 % 3)   # Retorna o resto da divisão


# Precedencia
print(2 + 10 * 5)
print((2 + 10) * 5)

# Poliformismo (mesmo operador tem várias funções)
print(20*'A')
print(20*10)