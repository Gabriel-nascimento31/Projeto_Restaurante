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



def cadastrar_item_cardapio():
    print("\n CADASTRAR NOVO ITEM NO CARDÁPIO ")
    nome = input("Nome do item: ").strip()

    preco = float(input("Preço (R$): "))
    tipo = input("Tipo (refeição / bebida): ").strip().lower()
    
    novo_item = Item(nome, preco, tipo)
    cardapio.adicionar(novo_item)
    print(f"'{nome}' foi adicionado ao cardápio!")


def remover_item_cardapio():
    print("\n REMOVER ITEM DO CARDÁPIO ")
    if cardapio.tamanho == 0:
        print("O cardápio está vazio.")
        return

    nome = input("Digite o nome do item que deseja remover: ").strip()
    item = cardapio.buscar_item_cardapio(nome)

    if item and cardapio.deletar(item):
        print(f"Item '{nome}' removido do cardápio!")
    else:
        print(f"Item '{nome}' não foi encontrado no cardápio.")