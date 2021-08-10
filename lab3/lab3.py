class VeiculoAutomotor():
    """
    A classe representa um veículo automotor.
    

    Atributos
    ---------
    dono: str 
        nome do dono do veículo
    placa: str 
        dígitos da placa do veículo
    combustivel: str
        tipo de combustível do veículo
    """
    def __init__(self, dono, placa, combustivel):
        self.dono = dono
        self.placa = placa
        self.combustivel = combustivel
        
    def __str__(self):
        return "Dono: {}, placa: {}, combustível: {}".format(self.dono, self.placa,\
        self.combustivel)


class Automovel(VeiculoAutomotor):
    """
    A classe representa um automóvel.
    

    Atributos
    ---------
    dono: str 
        nome do dono do veículo
    placa: str 
        dígitos da placa do veículo
    combustivel: str
        tipo de combustível do veículo

    lugares: int 
        quantos lugares o automóvel possui
    portas: int 
        quantas portas o automóvel possui
    ano: int 
        ano de fabricação do carro
    """
    def __init__(self, dono, placa, combustivel, lugares, portas, ano):
        self.lugares = lugares
        self.portas = portas
        self.ano = ano
        super().__init__(dono, placa, combustivel)

    def __str__(self):
        return 'Dono: {}, placa: {}, combustível: {}, lugares: {}, portas: {}, ' \
        'ano: {}'.format(self.dono, self.placa, self.combustivel, 
                        self.lugares, self.portas, self.ano)
        
    def trocarDono(self, novo):
        self.dono = novo


class Caminhao(VeiculoAutomotor):
    """
    A classe representa um caminhão.
    
    
    Atributos
    ---------
    dono: str
        nome do dono do veículo
    placa: str
        dígitos da placa do veículo
    combustivel: str
        tipo de combustível do veículo

    cargaMax: float
        carga máxima suportada em toneladas
    """
    def __init__(self, dono, placa, combustivel, cargaMax):
        self.cargaMax = cargaMax
        super().__init__(dono, placa, combustivel)
    
    def __str__(self):
        return 'Dono: {}, placa: {}, combustível: {}, carga máxima: {} toneladas'.format(
            self.dono, self.placa, self.combustivel, self.cargaMax)

