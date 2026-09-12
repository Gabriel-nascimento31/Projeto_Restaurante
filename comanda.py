import datetime
from lista_encadeada import Lista



class Item:
    def __init__(self, nome = str, preço = float, tipo = str):
        self.nome = nome
        self.preço = preço
        self.tipo = tipo

    def printar_item_preço(self):
        print(f'{self.nome}: R${self.preco} ')




class Comanda:
    def __init__(self, número = int, cliente = str, refeições_pedidas = Item, bebidas_pedidas = Item):
        self.número = número
        self.cliente = cliente
        self.data_hora_abertura = datetime.now()
        self.refeições_pedidas = refeições_pedidas
        self.bebidas_pedidas = bebidas_pedidas


    def abrir_comanda(self, comanda):
        comanda = Comanda
        Lista.adicionar(comanda)
        print('Comanda: {número} foi aberta')

    def fechar_comanda(self, comanda):
        Lista.deletar(comanda)
        print('Comanda: {número} foi fechada')

    
        





        
        
    
    

    
    
