import datetime

class Produto:
    def __init__(self, nome=str, preço_compra=float, preço_venda=float, quantidade=float):
        self.nome = nome
        self.preço_compra = preço_compra
        self.preço_venda = preço_venda
        self.data_compra = datetime.date
        self.data_vencimento = datetime.date
        self.quantidade = quantidade
    
