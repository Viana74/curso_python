"""
Exercícios
"""

"""
1 - Pedir para o usuário digitar um número inteiro e exibir se é par ou impar.
Caso o usuário não digite um número inteiro, informar que o número não é inteiro
"""
"""
num = input("Digite um número inteiro: ") #  A funcao input sempre retorna uma string

if num.isdigit():

    resto = int(num) % 2
    if resto != 0:
        print(f"O número {int(num)} é impar")
    else:
        print(f"O número {int(num)} é par")
else:
    print('Por favor, digite um número inteiro')
"""


"""
2 - Faça um programa que pergunte a hora para o usuario e se baseando na hora informada, exiba a respectiva saudação
Ex.: 0-11h (Bom dia), 12h - 17h (Boa tarde), 18h - 23h (Boa noite)
"""

hora = input('Digite a hora no formato 24h (hh:mm): ')
if hora[2] != ':':
    print('Formato errado!\n')

hh = int(hora[0] + hora[1])
mm = int(hora[3] + hora[4])

if hh<0 or hh==24 or mm<0 or mm>59:
    print('Formato errado! Fora dos limites')

elif (hh>=0 and hh<=11):
    print('Bom dia')
elif (hh>=12 and hh<=17):
    print('Boa tarde')
elif hh>=18 and hh<=23:
    print('Boa noite')


"""
3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Se nome é curto"; Se tiver de 5 a 6 letras escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é grande"
"""
"""
nome = input("Digite seu primeiro nome: ")

len = len(nome)

if len <= 4:
    print("Seu nome é curto")
elif len >=5 and len <= 6:
    print("Seu nome é normal")
elif len > 6:
    print("Seu nome é grande")
"""