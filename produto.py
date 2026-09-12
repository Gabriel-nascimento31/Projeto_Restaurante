import datetime

class Produto:
    def __init__(self, nome=str, preco_compra=float, preco_venda=float, quantidade=float):
        self.nome = nome
        self.preço_compra = preco_compra
        self.preço_venda = preco_venda
        self.data_compra = datetime.date
        self.data_vencimento = datetime.date
        self.quantidade = quantidade
    
