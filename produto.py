from datetime import date

class Produto:
    def __init__(self, nome:str, preco_compra:float, preco_venda:float, quantidade:float, data_compra:date = None, data_vencimento: date = None):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra if data_compra else date.today()
        self.data_vencimento = data_vencimento if data_vencimento else date.today()
        self.quantidade = quantidade


    def __str__(self):
        return f"{self.nome}  Qtde: {self.quantidade}  Venc: {self.data_vencimento.strftime('%d/%m/%Y')}  Preco Venda: R${self.preco_venda:.2f}"
    
