"""
Variáveis
"""

# Sempre incia a variavel com letra, letra minusculas, se separar usar "_"
nome = 'Éverton'
idade = 35
altura = 1.78
peso = 80
e_maior = idade > 18
imc = peso/(altura**2)

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('Peso: ', peso)
print('É maior? ', e_maior)

#####
print(nome, 'tem', idade, 'anos e o seu IMC é', imc)
print(f'{nome} tem {idade} anos e o seu IMC é {imc:.2f}')
print('{} tem {} anos e o seu IMC é {}'.format(nome,idade,imc))

#OU
print('{0} tem {1} anos e o seu IMC é {2}'.format(nome,idade,imc))
print('{n} tem {i} anos e o seu IMC é {im}'.format(n=nome,i=idade,im=imc))