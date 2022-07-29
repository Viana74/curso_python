"""
Escopo de variavel
"""

variavel = 'valor' #variavel global

def func1():
    print(variavel)

def func2():
    #global variavel
    variavel = 'outro valor' # é outra variavel criada dentro do escopo desta função (escopo local)
    print(variavel)          # neste caso, para o escopo global essa variavel = valor. Fazendo
                             # global variavel antes a variavel é alterada sob um escopo global

func1()
func2()

print(variavel)