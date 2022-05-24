"""
Exercícios
"""

"""
Pedir para o usuário digitar um número inteiro e exibir se é par ou impar.
Caso o usuário não digite um número inteiro, informar que o número não é inteiro
"""

num = input('Digite um número inteiro: ')
print(int(num))

if 'str' in num:
    resto = num%2
    if resto != 0:
        print('O numero é impar')
    else:
        print('O numero é par')
else:
    print('O número digitado não é inteiro!')
