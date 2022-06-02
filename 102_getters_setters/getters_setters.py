class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        #self._nome = valor.lower() # todas letras minusculas
        #self._nome = valor.title() # primeira letra maiuscula
        self._nome = valor.replace('A','@') # substitui A por @

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preco = valor


p1 = Produto('camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('caneca',15)
p2.desconto(10)
print(p2.preco)

p3 = Produto('caneca','R$15') #Erro pq o preço é uma string
p3.desconto(10)
print(p3.preco)

# Enviando o nome dos produtos mal formatados.
# Retorna tudo em minuscula
p4 = Produto('CAMISETA', 50)
p4.desconto(10)
print(p4.nome, p4.preco)

p5 = Produto('CANECA','R$15') #Erro pq o preço é uma string
p5.desconto(10)
print(p5.nome, p5.preco)