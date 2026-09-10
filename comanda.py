class Comanda:
    def __init__(self, número, cliente, data_abertura, hora_abertura, refeições_pedidas, bebidas_pedidas):
        self.número = número
        self.cliente = cliente
        self.data_abertura = data_abertura
        self.hora_abertura = hora_abertura
        self.refeições_pedidas = refeições_pedidas
        self.bebidas_pedidas = bebidas_pedidas
    def adicionar_refeicoes(self, refeição):
        if self.refeições_pedidas is None:
            self.refeições_pedidas = refeição
        else:
            self.refeições_pedidas = refeição
    def adicionar_bebidas(self, bebida):
        if self.bebidas_pedidas is None:
            self.bebidas_pedidas = bebida
        else:
            self.bebidas_pedidas = bebida
    
