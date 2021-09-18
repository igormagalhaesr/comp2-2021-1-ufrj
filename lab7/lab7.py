import numpy as np

def senoPositivo(a, b, n):
    """
    Recebe os limites a e b de um intervalo e um inteiro n

    Separa o intervalo em n pontos e retorna os elementos cujo seno é positivo

    Parâmetros
    ----------
    a : float
      primeiro ponto do intervalo
    b : float
      último ponto do intervalo
    n : int
      número de pontos que o intervalo será dividido

    Retorna
    -------
    numpy.ndarray
      array com os pontos do array original dividido cujos senos sãp positivos
    """
    arr = np.linspace(a, b, n)
    
    return arr[np.where(np.sin(arr) > 0)] 

def polinomio(arr, z):
    """
    Recebe um array e um número z

    Retorna o valor do polinômio p(x) = a0 + a1 * x + a2 * x ** 2 + ... no ponto z

    Parâmetros
    ----------
    arr : np.ndarray
      primeiro ponto do intervalo
    z : float ou int
      ponto para testar os valores do polinômio
    
    Retorna
    -------
    float ou int
      valor de p(z)
    """
    pot = np.cumproduct(np.full((len(arr)), z))
    pot[0] = 1
    
    return sum(arr * pot)

def ortogonal(arr):
    """
    Recebe um array arr

    Retorna True caso seja ortogonal e False caso não seja

    Parâmetros
    ----------
    arr : np.ndarray
      array com uma ou duas dimensões
    
    Retorna
    -------
    bool
      True caso a matriz seja ortogonal e False caso contrário
    """
    out = False
    
    if (len(arr.shape) == 1) and (arr.shape[0] == 1):
        out = True

    elif (arr.shape == 2) and (arr.shape[0] == arr.shape[1]):
        out = np.allclose(np.linalg.inv(arr), (arr.T))

    return out

