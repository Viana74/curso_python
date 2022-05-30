#p1 = Pessoa() # cria uma instancia chamada p1 da classe Pessoa
#p2 = Pessoa() # cria uma instancia chamada p2 da classe Pessoa

#print(p1)
#print(p2)

"""
nota-se que p1 não é igual a p2, são varias pessoas vindas de
um mesmo molde
"""

#p1.nome = 'Luiz'
#p2.idade = 39

# Apesar de p1 e p2 "nascerem" do mesmo molde, a variavel
# nome só exise em p1 e idade so existe em p2

# print(p2.nome) # erro de atributo

#p1.falar()
#p2.falar()
from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)

p1.comer('maça')
p1.comer('bergamota')
p1.parar_comer()
p1.parar_comer()
p1.comer('bergamota')
p1.falar('futebol')
p1.parar_comer()
p1.falar('futebol')
p1.falar('novela')
p1.parar_falar()
p1.falar('novela')
p1.parar_falar()

p2 = Pessoa('Joao',35)
p2.comer('Torta')
p1.comer('pao')

#print(p1.ano_atual)
#print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())

print(p2.get_ano_nascimento())

#print(p1)
#p1.nome = 'Luiz'