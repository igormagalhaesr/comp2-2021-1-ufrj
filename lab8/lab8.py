import matplotlib.pyplot as plt
import numpy as np

def racional(n):
    """
    Recebe um parâmetro n : int e plota n pontos das funções $y=\frac{1}{x}$
    e $y=\frac{1}{x^2}$ no intervalo [0.1, 2].
    
    Retorna None
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    x = np.linspace(0.1, 2, n)

    # definindo as funções
    y1 = 1 / x
    y2 = 1 / (x ** 2)

    # plotando
    ax.plot(x, y1, 'cs-', linewidth=2, label=r'$y=\frac{1}{x}$')
    ax.plot(x, y2, 'mo-', linewidth=2, label=r'$y=\frac{1}{x^2}$')

    # título e legenda
    ax.set_title('Funções racionais')
    ax.legend()
    
    # alterando o eixo x
    plt.xticks([0, 1, 2])
    plt.show()

    return None

def polinomios(n):
    """
    Recebe um parâmetro n : int e plota todas as funções y=x**i para i de 1 até n
    no intervalo [-1, 1].

    Retorna None
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    x = np.linspace(-1, 1, 100)
    i_arr = np.linspace(1, n, n, dtype=int)
    
    # nas variações de i, plotamos cada função x ** i
    for i in i_arr:
      y_temp = x ** i
      plt.plot(x, y_temp, linewidth=2, label='y=x**{}'.format(i))

    plt.yticks([-1, 0, 1])
    plt.xticks([-1, 0, 1])
    
    ax.legend()
    plt.show()

    return None

def fun(a, b, n):
    """
    Recebe dois floats a e b que representam o intervalo [a, b] e um inteiro n. 
    Plota a função $y=\frac{1}{sin(x)}$

    Retorna os pontos removidos do intervalo por não satisfazerem a condição:
    np.abs(np.diff(np.sign(np.sin(x)))) > 1)
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    funct = lambda x: 1 / np.sin(x)
    x = np.linspace(a, b, n)
    x = x[np.where(np.sin(x) != 0)]
    x = x[np.where(np.abs(funct(x)) < 20)]

    y = funct(x)

    to_remove = np.where(np.abs(np.diff(np.sign(np.sin(x)))) > 1)[0] + 1
    x[np.where(to_remove)] = np.nan
    y[np.where(to_remove)] = np.nan

    x = np.insert(x, to_remove, np.nan)
    y = np.insert(y, to_remove, np.nan)

    plt.plot(x, y, 'c-o', label=r'$\frac{1}{sin(x)}$')
    plt.legend(loc='upper center')
    plt.show()

    return to_remove

