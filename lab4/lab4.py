def contatos(dict_list):
    """
    Recebe uma lista de dicionários e retorna um dicionário com as chaves 
    e valores dos dicionários na lista.

    Atributos
    ---------
    dict_list: list[dict]
        uma lista de dicionários
    
    Saída
    -------
    out: dict
        um dicionário com as chaves e valores dos dicionários em dict_list
    """
    # keys é uma versão planificada das chaves dos dicionários em dict_list
    keys, out = [key for dic in dict_list for key in dic], {}

    # para cada key, uma lista é criada com os elementos de keys com mesmo nome
    for key in keys:
      out[key] = [dic[key] for dic in dict_list if key in dic]

    return out

def piano(notas):
    """
    Recebe uma string com notas e suas posições da forma 'C1A2D3B4G3' onde
    cada letra em uma posição i representa uma nota e o número na posição i + 1
    representa a sa posição relativa no piano. 

    Retorna uma lista com as frequências de cada nota na respectiva posição informada.

    Atributos
    ---------
    notas: str
        uma string com notas e suas posições no piano da forma 'C1A2D3B4G3'

    Saída
    -------
    list
        uma lista de números que representam as frequências das notas
    """
    reference = {'C': 262, 'D': 294, 'E': 330, 'F': 349, 'G': 392, 'A': 440, 'B': 494}
  
    # notando que 'notas' estão em posição par e 'posições' em posição ímpar
    notas_list = [notas[i] for i in range(0, len(notas), 2)]
    positions_list = [int(notas[i]) for i in range(1, len(notas), 2)]
  
    return [reference[key] * (2 ** (i - 3)) for i, key in zip(positions_list, notas_list)]


def rezistor(cor1, cor2, cor3):
    """
    Recebe 3 strings que representam cores do código de um resistor, retorna 
    o valor da resistência baseado nos códigos de cores.

    Atributos
    ---------
    cor1: str
        cor da primeira faixa no resistor
    cor2: str
        cor da segunda faixa no resistor
    cor3: str
        cor da terceira faixa no resistor

    Saída
    -----
    int
        valor da resistência pelo código de cores informado
    """
    reference = {'Preto': 0, 'Marrom': 1, 'Vermelho': 2, 'Laranja': 3, 'Amarelo': 4}
    return (reference[cor1] * 10) + reference[cor2] * (10 ** reference[cor3])

