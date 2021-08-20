class Dinheiro():
    """
    A classe representa uma quantia de dinheiro em uma certa moeda.


    Atributos
    ---------
    valor: float ou int 
        valor na moeda escolhida

    Métodos
    -------
    valor_em(moeda)
        retorna o valor inserido na moeda desejada
    """
    
    def __init__(self, valor, moeda):
        """
        Parâmetros
        ----------
        valor : float
            o valor na moeda definida
        moeda : str
            uma moeda entre USD, EUR, JPY, BRL
        """
        conversor = {'USD': 4.012, 'EUR': 4.451, 'JPY': 0.035, 'BRL': 1}
        self.valor = valor * conversor[moeda]

    def valor_em(self, moeda):
        """
        Retorna o valor do objeto convertido para a moeda desejada.
        

        Parâmetros
        ----------
        moeda : str
            a moeda 

        Retorna
        -------
        float
            o valor do objeto convertido para a moeda
        """
        conversor = {'USD': 4.012, 'EUR': 4.451, 'JPY': 0.035, 'BRL': 1}
        return self.valor / conversor[moeda]

    def __str__(self):
        return '{} BRL'.format(self.valor)


def BrexitEmployment(exit_cpfs, stay_cpfs, employed_cpfs, unemployed_cpfs):
    """
    Recebe 4 conjuntos de CPFs de pessoas (que votaram para sair da UE, que 
    votaram para permanecer na UE, pessoas empregadas e pessoas desempregadas)

    Retorna as porcentagens dos empregados e desempregados em cada grupo (que 
    votou para sair da UE e que votou para permanecer na UE).


    Parâmetros
    ----------
    exit_cpfs : set
        cpfs de pessoas que votaram para o Reino Unido sair da UE
    stay_cpfs : set
        cpfs de pessoas que votaram para o Reino Unido ficar na UE
    employed_cpfs : set
        cpfs de pessoas empregadas
    unemployed_cpfs : set
        cpfs de pessoas desempregadas

    Retorna
    -------
    str
        porcentagem de empregados e desempregados entre os que votaram para o 
        Reino Unido sair e os que votaram para não sair da UE na forma

        YES: w% trabalham, x% estão desempregados
        NO: y% trabalham, z% estão desempregados

        com até 2 casas decimais na porcentagem.
    """  
    # número de pessoas que votaram sim ou não
    all = len(exit_cpfs | stay_cpfs)

    # número de empregados e desempregados que votaram sim
    yes_emp, yes_unemp = sum((cpf in employed_cpfs for cpf in exit_cpfs)), \
                         sum((cpf in unemployed_cpfs for cpf in exit_cpfs))

    # númerode empregados e desempregados que votaram não
    no_emp, no_unemp = sum((cpf in employed_cpfs for cpf in stay_cpfs)), \
                       sum((cpf in unemployed_cpfs for cpf in stay_cpfs))

    out = ('YES: {:.2%} trabalham, {:.2%} estão desempregados\n' + 
          'NO: {:.2%} trabalham, {:.2%} estão desempregados').format(
              yes_emp / all, yes_unemp / all, no_emp / all, no_unemp / all
          )

    return out

