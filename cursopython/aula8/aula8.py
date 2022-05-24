nome = 'Éverton'
idade = 36
altura = 1.78
peso = 79
ano_atual = 2022
imc = (peso)/(altura**2)
ano_nasc = ano_atual - idade

print(f'{nome} nasceu em {ano_nasc}, logo tem {idade} anos. Tem {altura} de altura, {peso} de peso e possui indice IMC de {imc:.2f}')
#print('{0} nasceu em {1}, logo tem {2} anos, {3} de altura, {4} de peso e possui indice IMC de {5}'.format(nome,ano_nasc,idade,altura,peso,imc))