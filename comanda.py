from datetime import datetime
from lista_encadeada import Lista

comandas_ativas = Lista()



class Comanda:
    def __init__(self, número, cliente, refeições_pedidas, bebidas_pedidas):
        self.número = número
        self.cliente = cliente
        self.data_hora_abertura = datetime.now()
        self.refeições_pedidas = refeições_pedidas
        self.bebidas_pedidas = bebidas_pedidas

    def calcular_total(self):
        total = 0.0
        atual = self.refeições_pedidas.inicio
        while atual:
            total += atual.dado.preco
            atual = atual.ponteiro

        atual = self.bebidas_pedidas.inicio
        while atual:
            total += atual.dado.preco
            atual = atual.ponteiro
        
        return total
    

    def abrir_comanda(comandas_ativas):
        print(" ABRIR COMANDA ")
        cliente = input("Nome do cliente: ").strip()
        nova_comanda = Comanda(
            número=contador_comanda,
            cliente=cliente,
            refeições_pedidas=Lista(), 
            bebidas_pedidas=Lista()
        )
        comandas_ativas.adicionar(nova_comanda)
        print(f"Comanda {contador_comanda} criada para {cliente}!")
        contador_comanda = 1
    
    def adicionar_itens_comanda(comandas_ativas):
        print(" ADICIONAR ITENS À COMANDA ")
        if comandas_ativas.tamanho == 0:
            print("Nenhuma comanda aberta no momento.")
            return

        num_input = input("Informe o número da comanda: ").strip()
        if not num_input.isdigit():
            print("Número de comanda inválido!")
            return

        comanda = comandas_ativas.buscar_comanda(int(num_input))
        if not comanda:
            print(f"Comanda {num_input} não encontrada!")
            return

        print(f"Comanda {comanda.número}  Cliente: {comanda.cliente}")
        print(" CARDÁPIO DISPONÍVEL")
        atual = cardapio.inicio
        while atual:
            item = atual.dado
            print(f" {item.nome} ({item.tipo}): R${item.preco:.2f}")
            atual = atual.ponteiro

        nome_item = input("\nDigite o nome do item que deseja adicionar: ").strip()
        item_encontrado = cardapio.buscar_item_cardapio(nome_item)

        if item_encontrado:
            if item_encontrado.tipo.lower() == 'bebida':
                comanda.bebidas_pedidas.adicionar(item_encontrado)
            else:
                comanda.refeições_pedidas.adicionar(item_encontrado)
            print(f"'{item_encontrado.nome}' adicionado com sucesso à Comanda {comanda.número}!")
        else:
            print("Item não encontrado no cardápio!")
    

    def encerrar_comanda(comandas_ativas):
        print(" ENCERRAR COMANDA ")
        if comandas_ativas.tamanho == 0:
            print("Não há comandas abertas para encerrar.")
            return

        num_input = input("Informe o número da comanda para encerrar: ").strip()
        if not num_input.isdigit():
            print("Número de comanda inválido!")
            return

        comanda = comandas_ativas.buscar_comanda(int(num_input))
        if not comanda:
            print(f"Comanda {num_input} não encontrada!")
            return

    
        comandas_ativas.deletar(comanda)
        print(f"Comanda {comanda.número} do cliente '{comanda.cliente}' foi encerrada com sucesso!")
    
    
    
lista_comandas = Lista()
comandas_ativas = Lista()



