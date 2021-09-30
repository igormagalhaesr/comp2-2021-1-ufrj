import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def alturas(n):
    """
    Recebe um inteiro n, retorna um array com n números aleatórios de uma 
    distribuição normal representando alturas corporais de uma população de n
    pessoas adultas. Salva um histograma do array 'alturas.png'

    Parâmetros
    ----------
    n : int
      número de alturas no array

    Retorna
    -------
    arr : np.ndarray
      array com as alturas aleatórias de uma distribuição normal
    """
    arr = st.norm.rvs(loc=1.7, scale=0.08, size=n)
    
    # plotando a figura
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title('Alturas')
    plt.hist(arr, bins=20, color='c')
    plt.savefig('alturas.png')

    return arr

def pesos(alturas):
    """
    Recebe um array de alturas, retorna um array de pesos de mesmo tamanho
    seguindo um índice de massa corporal retirado aleatoriamente de uma 
    distribuição normal. Salva um histograma do array 'pesos.png'
    
    Parâmetros
    ----------
    alturas : np.ndarray
      array de alturas

    Retorna
    -------
    pesos : np.ndarray
      array com os pesos
    """
    imcs = st.norm.rvs(loc=24.5, scale=4.3, size=len(alturas))
    pesos = imcs * (alturas ** 2)

    # plotando a figura
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_title('Pesos')
    plt.hist(pesos, bins=20, color='m')
    plt.savefig('pesos.png')

    return pesos

def regressaoLinear(alturas, pesos):
    """
    Recebe dois arrays de mesmo tamanho, um representando alturas e outro
    representando pesos. Calcula uma regressão linear, retorna uma tupla
    com o coeficiente angular e o coeficiente linear da reta. Salva um gráfico
    de dispersão e a reta calculada pela regressão 'regressao.png'

    Parâmetros
    ----------
    alturas : np.ndarray
      array com alturas
    pesos: np.ndarray
      array com pesos

    Retorna
    -------
    tuple
      tupla com o coeficiente angular e o coeficiente linear da reta calculada
      pela regressão linear
    """
    a, b = st.linregress(alturas, pesos)[:2]

    fig, ax = plt.subplots(figsize=(6, 6))

    y = lambda x : a * x + b
    x = np.linspace(alturas.min(), alturas.max())

    # plotando a figura
    ax.set_title('Altura vs. peso')
    plt.scatter(alturas, pesos)
    plt.plot(x, y(x), color='red')
    plt.savefig('regressao.png')
    plt.xlabel('Altura')
    plt.ylabel('Peso') 

    return a, b

