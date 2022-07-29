"""
Entrada de dados
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nasc = 2022-int(idade)

print(f'{nome} tem {idade} anos.  ')
print(f'{nome} nasceu em {ano_nasc}.')

# Calculadora
nro1 = input(f'Digite o primeiro número: ')  #Função input sempre retorna um string
nro2 = input(f'Digite o segundo número: ')

print(f'A soma do primeiro número com o segundo número é: {nro1+nro2}') # Concatenou, i.e., preciso de um cast
print(f'A soma do primeiro número com o segundo número é: {int(nro1)+int(nro2)}') #Corrigido
print(f'O primeiro número elevado ao segundo número é: {int(nro1)**int(nro2)}') #Potenciação