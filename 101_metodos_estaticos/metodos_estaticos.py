from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # está relacionado a instancia pos recebe o self.
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Classmethod está relacionado a classe, isto é, não precisa de uma instancia.
    # diferente de um método normal que é relacionado a estância
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #Estatic method não esta relacionado a instancia e nem da classe, mas utiliza a mesmas para
    # executar o metodo
    @staticmethod
    def gera_id():
        rand = randint(10000, 20000)
        return rand

p1 = Pessoa('Luiz',32)
print(p1.idade)
p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Luiz', 1990)
print(f'{p1.nome} tem {p1.idade} anos de idade.')

print(Pessoa.gera_id())
print(p1.gera_id())