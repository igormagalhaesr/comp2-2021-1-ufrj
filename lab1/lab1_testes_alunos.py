from lab1 import *

print("====== Questão 1 - expectativa: ")
print("""(math.sin(a1)math.cos

2346543""")
print("------seu resultado:")
print(concatena("calcularAngulo(math.sin(a1)", "math.cos(a1)", 14, 4))
print(concatena("01234", "6543210", 14, 9))
print(concatena("01234", "6543210", 2, 3))


print("====== Questão 2 - expectativa: ")
print("""[0.2, 0.6]
[6, 8]
[0, 0.2, -0.6, 0.6, -2.5]""")
print("------seu resultado:")
lista = [-5, 0, 0.2, -0.6, 0.6, -2.5, 6, 8]
print(sublista(lista,0,1))
print(sublista(lista,1,10))
print(sublista(lista,-3,1))


print("====== Questão 3 - expectativa: ")
print("""palavras com espaço de  entrada é uma string palavra""")
print("------seu resultado:")
print(fun("palavras com espaço", ["de", "", "entrada", "é uma string palavra"]))


print("====== Questão 4a - expectativa: ")
print("""2.7166666666666663""")
print("------seu resultado:")
print(numeroEuler(5))


print("====== Questão 4b - expectativa: ")
print("""7""")
print("------seu resultado:")
print(precisaoEuler(0.0001))


