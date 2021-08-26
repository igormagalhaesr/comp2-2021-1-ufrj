def absoluto(number):
    """
    Recebe um número e retorna seu valor absoluto. O número recebido pode ser um
    int, float ou str. 

    Atributos
    ---------
    number
        um número que pode ser um float, int ou str
    
    Saída
    -------
    out: float
        o valor absoluto de number
    """
    try:
        number = float(number)

        if number < 0:
          number = -number

        return number

    except ValueError:
        print("ValueError para '{}'".format(number))
        
        return None

    except TypeError:
        print('TypeError para {}'.format(type(number)))
        
        return None

class Loja():
    """
    A classe representa uma loja com um nome, categorias e seus respectivos produtos.


    Atributos
    ---------
    nome : str 
        o nome da loja

    produtos : dict
        um dicionário cujas chaves representam categorias de produtos, seus respectivos
        valores representam as marcas presentes nessas categorias na loja.

    Métodos
    -------
    adicionarProduto(categoria, marca)
        adiciona uma marca a uma categoria em produtos

    verCategoria(categoria)
        retorna as marcas em uma certa categoria, imprime uma mensagem se a categoria
        não existir em produtos

    removerMarca(marca)
        remove uma marca de todas as categorias que a tiverem em produtos
    """
    def __init__(self, nome, produtos={}):
        """
        Parâmetros
        ----------
        nome : str
            o nome da loja

        produtos={} : dict
            categorias e suas respectivas marcas em uma loja
        """
        self.nome = nome
        self.produtos = produtos

    def adicionarProduto(self, categoria, marca):
        """
        Adiciona uma marca a uma categoria em produtos. Se a categoria não existir,
        uma categoria com o nome passado é criada e a marca é adicionada.
        

        Parâmetros
        ----------
        categoria : str
            a categoria em produtos a se inserir uma marca

        marca : str
            a marca que vai ser inserida em uma categoria em produtos
        """
        try:
            self.produtos[categoria].add(marca)
        
        except KeyError:
            self.produtos[categoria] = {marca}

    def verCategoria(self, categoria):
        """
        Recebe uma categoria, retorna um conjunto com as marcas presentes na categoria
        passada. Se a categoria não existir, retorna None e imprime uma mensagem.
        

        Parâmetros
        ----------
        categoria : str
            a categoria de produtos

        Retorna
        -------
        set
            um conjunto com as marcas na categoria passada
        """
        try:
            return self.produtos[categoria]
        
        except KeyError:
            print('Categoria {} não catalogada.'.format(categoria))
            return None

    def removerMarca(self, marca):
        """
        Recebe uma marca, remove a marca de todas as categorias em produtos. 
        

        Parâmetros
        ----------
        marca : str
            a marca que vai ser removida das categorias em produtos
        """
        for categoria in self.produtos:
            try:
                self.produtos[categoria].remove(marca)
            
            # nota: embora o programa passe quando o erro é achado, um antipattern, esse
            # código roda mais rapidamente que testando marca in categoria para cada categoria
            except KeyError:
                pass
