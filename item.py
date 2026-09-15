class Item:
    def __init__(self, nome = str, preco = float, tipo = str):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo

    def printar_item_preco(self):
        print(f'{self.nome}: R${self.preco:.2f} ')
