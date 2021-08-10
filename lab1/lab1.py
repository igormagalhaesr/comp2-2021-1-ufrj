from math import factorial, fabs, e

def concatena(str1, str2, m, n):
    """
    Recebe duas strings str1 e str2 e dois inteiros m e n 

    Retorna a concatenação da primeira string sem os primeiros m caracteres e 
    a segunda string sem os últimos n caracteres
    """
    return str1[m:] + str2[:-n]


def sublista(number_list, m, n):
    """
    Recebe uma lista de números (ints ou floats) e dois números m e n

    Retorna os elementos da lista que são maiores que m e menores que n
    """
    return [num for num in number_list if (num > m) and (num < n)]


def fun(palavra, lista_strings):
    """
    Recebe uma string palavra e uma lista de strings lista_strings

    Retorna uma string representada palavra e as strings da lista_strings
    separadas por um espaço ' '
    """
    return ' '.join([palavra] + lista_strings)


def numeroEuler(n):
    """
    Recebe um número inteiro n

    Retorna uma aproximação do número de Euler e somando n + 1 termos da série 1/(k!)
    com k variando de 0 até n
    """
    return sum((1/factorial(k) for k in range(n + 1)))


def precisaoEuler(erro):
    """
    Recebe um número real erro

    Retorna o número necessário n para a função numeroEuler(n) atingir uma aproximação
    que tem uma diferença igual ao parâmetro erro do e no módulo math
    """
    # checamos quantas vezes iterar para chegar a um erro menor que o input
    n = 0
    while fabs(numeroEuler(n) - e) > erro:
      n += 1

    return n


def main():
    # recebendo erro como um input do usuário
    erro = float(input('Entre o erro tolerância máxima da aproximação de e: '))
  
    # checamos quantas vezes iterar para chegar a um erro menor que o input
    n = 0
    while fabs(numeroEuler(n) - e) > erro:
      n += 1

    return n

if __name__ == "__main__":
    print(main())
