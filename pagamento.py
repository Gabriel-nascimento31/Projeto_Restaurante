from datetime import datetime
from lista_encadeada import Lista

class Pagamento:
    def __init__(self, pagador=str, comanda=int, forma=str, valor=float):
        self.pagador = pagador
        self.comanda = comanda
        self.forma = forma
        self.valor = valor
        self.data_hora_pagamento = datetime.now()

pagamento = Pagamento()
lista_pagamentos = Lista()




        
        
          