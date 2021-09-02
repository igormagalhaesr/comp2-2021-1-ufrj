def escreverNoArquivo(nome, lista):
    """
    Escreve uma lista em um arquivo de texto com cada elemento da lista em uma linha.
    Retorna o número de caracteres escritos no arquivo. Se o arquivo não existir, 
    cria um novo com o nome, se já existir, sobrescreve seu conteúdo.

    Parâmetros
    ----------
    nome : str
        o nome do arquivo a ser escrito, deve terminar com .txt
    lista : lst
        lista com os elementos que serão escritos no arquivo

    Retorna
    -------
    int
        número de caracteres escritos no arquivo
    """
    f = open(nome, 'w')
    characters = 0
  
    for obj in lista:
        f.write('{}\n'.format(obj))
        characters += len('{}\n'.format(obj))
  
    f.close()
  
    return characters

def retornarLista(str_list):
    """
    Recebe uma string de uma lista com números e strings como possíveis elementos
    Retorna uma lista com os elementos numéricos em float e strings em str
    Requer que a lista tenha nenhum espaço antes de vírgulas e exatamente um espaço
    após a vírgula.
    
    Parâmetros
    ----------
    str_list : str
        uma lista em formato de string

    Retorna
    -------
    list
        lista formada a partir da string
    """
    out = str_list[1:-1].split(', ')
    out = [float(el) if el[0] not in {'"', "'"} else el[1:-1] for el in out]
 
    return out
 
def lerArquivo(arq):
    """
    Recebe o nome de um arquivo de texto. Lê cada linha e retorna uma lista com 
    as respectivas linhas em seus tipos adequados.
    
    Parâmetros
    ----------
    arq : str
        nome do arquivo a ser lido

    Retorna
    -------
    list
        lista com cada linha do arquivo convertida em um elemento de tipo adequado
    """
    out = []
    f = open(arq, 'r')
  
    for line in f.readlines():
        # se o tipo for uma lista, usa a função retornarLista definida anteriormente
        if line[0] + line[-2] == '[]':
            out.append(retornarLista(line[:-1]))
    
        else:
            try:
                out.append(float(line))
            except:
                out.append(line[:-1])
 
    f.close()
  
    return out

#####################################################################################
# Essa parte não entra de fato na lista de exercícios, foi feita mais por curiosidade

def split_(s, delim=None):
    """
    separa uma string em uma lista de strings assim como o método split, mas não
    adiciona strings vazias ao começo e fim da lista.
    """ 
    return [x for x in s.split(delim) if x]

def find_lists(str_list):
    """
    Retorna uma lista com tuplas representando o começo e fim de listas na string
    """
    positions, n = [], str_list.count('[')
    
    for i in range(n):
        start = str_list.rfind('[')
        end = str_list.find(']')
        positions.append((start, end))

        str_list = str_list[:start] + '-' + str_list[start + 1:end] + '-' + str_list[end:]

    return positions

def to_list(str_list):
    """
    Recebe uma string de uma lista com números, strings e outras listas como possíveis elementos
    Retorna uma lista com os elementos numéricos em float e strings em str

    Compromissos: a lista virá em uma forma [1, 2, '3', [...], 2.0], 
    sem espaçamento antes de vírgulas e com um espaço após vírgulas; 
    a lista só terá os caracteres '[' e ']' se for pra representar outra lista.
    
    Parâmetros
    ----------
    str_list : str
        uma lista em formato de string

    Retorna
    -------
    list
        lista formada a partir da string
    """
    str_list = str_list[1:-1]
    possible_list = ('[' in str_list) and (']' in str_list)

    
    if possible_list:
        # aqui tratamos o caso de listas com apenas um elemento como sublista
        try:
            # identificamos onde está essa sublista
            start = str_list.find('[')
            end = str_list.rfind(']')

            # então dividimos a superlista em 3 partes, antes, sublista e depois
            # para uma sublista, chamamos a própria função to_list
            # para antes e depois, apenas fazemos um split

            internal_list = to_list(str_list[start:end + 1])
            first_sub = split_(str_list[:start], ', ')
            second_sub = split_(str_list[end + 1:], ', ')

            # convertendo os floats para float, retirando o marcador de strings
            first_sub = [float(el) if el[0] not in {'"', "'"} else el[1:-1] for el in first_sub]
            second_sub = [float(el) if el[0] not in {'"', "'"} else el[1:-1] for el in second_sub]

        # aqui tratamos listas com qualquer quantidade de sublistas maior que 1
        except:
            # a ideia é fazer um processo parecido com o descrito acima, mas para
            # quaisquer listas dentro da string, o que pode ser feito pelas
            positions = find_lists(str_list)
            raise NotImplementedError 

        # finalmente juntando as partes, 
        out = first_sub + [internal_list] + second_sub
    
    else: 
        out = str_list.split(', ')
        out = [float(el) if el[0] not in {'"', "'"} else el[1:-1] for el in out]

    return out

