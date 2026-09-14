from item import Item
from lista_encadeada import Lista


cardapio = Lista()

    
itens_iniciais = [
    Item('macarronada', 10.00, 'refeição'),
    Item('arroz-feijão', 5.00, 'refeição'),
    Item('lazanha', 20.00, 'refeição'),
    Item('nhoque', 15.00, 'refeição'),
    Item('filé de frango', 12.00, 'refeição'),
    Item('bife frito', 25.00, 'refeição'),
    Item('almondenga', 18.00, 'refeição'),
    Item('batata frita', 8.00, 'refeição'),
    Item('polenta', 15.00, 'refeição'),
    Item('carne moida', 18.00, 'refeição'),
    Item('hamburguer', 20.00, 'refeição'),
    Item('pastel', 11.00, 'refeição'),
    Item('frango assado', 30.00, 'refeição'),
    Item('salada', 5.00, 'refeição'),
    Item('estrogonofe', 20.00, 'refeição'),
    Item('refrigerante', 8.00, 'bebida'),
    Item('suco', 5.00, 'bebida'),
    Item('agua com gas', 3.00, 'bebida')
]


for item in itens_iniciais:
    cardapio.adicionar(item)
    