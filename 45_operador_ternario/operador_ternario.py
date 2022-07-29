"""
Operaçao ternaria em Python
"""


#Operacao classica

logged_user = True

if logged_user:
    msg = "Usuario logado"
else:
    msg = "Usuario nao logado"

print(msg)


#Usando o ternario
logged_user = False
msg = "Usuario logado" if logged_user else "Usuario precisa logar"

print(msg)



############################################
idade = 17

if idade>= 18:
    print("Pode acessar")
else:
    print("Não pode acessar")

idade2 = input('Qual a sua idade? ')

if not idade2.isnumeric():
    print('Digite somente numeros!')

print("É de maior, pode acessar" if int(idade2) >= 18 else "É de menor, não pode acessar")