from datetime import date

class Produto:
    def __init__(self, nome:str, preco_compra:float, preco_venda:float, quantidade:float, data_compra:date = None, data_vencimento:date = None):
        self.nome = nome
        self.preço_compra = preco_compra
        self.preço_venda = preco_venda
        self.data_compra = date
        self.data_vencimento = date
        self.quantidade = quantidade


    def __str__(self):
        return f"{self.nome}  Qtde: {self.quantidade}  Venc: {self.data_vencimento.strftime('%d/%m/%Y')}  Preço Venda: R${self.preco_venda:.2f}"
    
