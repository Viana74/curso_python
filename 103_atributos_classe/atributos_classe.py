class A:
    vc = 123 # variavel de classe (disponivel para todas as instancias)

# cria instancias da classe
a1 = A()
a2 = A()

# Imprimir utilizando a instancia
print(a1.vc)
print(a2.vc)
print(A.vc)