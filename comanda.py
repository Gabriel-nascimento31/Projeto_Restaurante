import os
import pickle
from datetime import datetime
from lista_encadeada import Lista
from cardapio import cardapio

def carregar_clientes_cadastrados():
  caminho_arquivo = "dados_lista.bin"
  if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        lista_clientes = pickle.load(f)
        return lista_clientes
    
      

class Comanda:
    contador = 1
    def __init__(self, cliente: str):
        self.numero = Comanda.contador
        Comanda.contador += 1
        self.cliente = cliente
        self.data_hora_abertura = datetime.now()
        self.refeicoes_pedidas = Lista()
        self.bebidas_pedidas = Lista()

    def calcular_total(self):
        total = 0.0
        atual = self.refeicoes_pedidas.inicio
        while atual:
            total += atual.dado.preco
            atual = atual.ponteiro

        atual = self.bebidas_pedidas.inicio
        while atual:
            total += atual.dado.preco
            atual = atual.ponteiro
        
        return total
    

    @staticmethod
    def abrir_comanda(comandas_ativas):
        print("\n ABRIR COMANDA ")
        clientes_salvos = carregar_clientes_cadastrados()

        cliente = ''
        if clientes_salvos and clientes_salvos.tamanho > 0:
            print('1 - Atender cliente da lista cadastrada ')
            print('2 - Atender novo cliente')
            opcao = input('Opção (1-2): ').strip()

            if opcao == '1':
                print('\n Clientes já cadastrados ')
                atual = clientes_salvos.inicio
                indice = 1
                while atual and indice <= 10:
                    print(f'{indice}. {atual.dado}')
                    atual = atual.ponteiro
                    indice += 1
                escolha = int(input('\n Digite o número do cliente: '))
                atual = clientes_salvos.inicio
                for c in range(escolha - 1):
                    if atual:
                        atual = atual.ponteiro
                if atual:
                    cliente = atual.dado
                else:
                    print('Cliente não encontrado! ')

            elif opcao == '2':
                cliente = input('Digite o nome do cliente: ').strip()
            

        nova_comanda = Comanda(cliente=cliente)
            
        comandas_ativas.adicionar(nova_comanda)
        print(f"Comanda {nova_comanda.numero} criada com sucesso para {cliente}!")
        
    

    @staticmethod
    def adicionar_itens_comanda(comandas_ativas):
        print("\n ADICIONAR ITENS À COMANDA ")
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

        print(f"Comanda {comanda.numero} | Cliente: {comanda.cliente}")
        print("--- CARDÁPIO DISPONÍVEL ---")
        atual = cardapio.inicio
        while atual:
            item = atual.dado
            print(f"- {item.nome} ({item.tipo}): R${item.preco:.2f}")
            atual = atual.ponteiro

        nome_item = input("\nDigite o nome do item que deseja adicionar: ").strip()
        item_encontrado = cardapio.buscar_item_cardapio(nome_item)

        if item_encontrado:
            if item_encontrado.tipo.lower() == 'bebida':
                comanda.bebidas_pedidas.adicionar(item_encontrado)
            else:
                comanda.refeicoes_pedidas.adicionar(item_encontrado)
            print(f"'{item_encontrado.nome}' adicionado com sucesso à Comanda {comanda.numero}!")
        else:
            print("Item não encontrado no cardápio!")
    

    @staticmethod
    def remover_item_comanda(comandas_ativas):
        print("\n REMOVER ITEM DA COMANDA ")
        if comandas_ativas.tamanho == 0:
            print("Nenhuma comanda aberta.")
            return

        num_input = input("Digite o número da comanda: ").strip()
        if not num_input.isdigit():
            print("Número inválido!")
            return

        comanda = comandas_ativas.buscar_comanda(int(num_input))
        if not comanda:
            print("Comanda não encontrada!")
            return

        nome_item = input("Digite o nome do item que deseja remover: ").strip()
        item_refeicao = comanda.refeicoes_pedidas.buscar_item_cardapio(nome_item)
        if item_refeicao and comanda.refeicoes_pedidas.deletar(item_refeicao):
            print(f"'{nome_item}' removido das refeições.")
            return

        item_bebida = comanda.bebidas_pedidas.buscar_item_cardapio(nome_item)
        if item_bebida and comanda.bebidas_pedidas.deletar(item_bebida):
            print(f"'{nome_item}' removido das bebidas.")
            return

        print("Item não encontrado nos pedidos da comanda.")
    

    @staticmethod
    def encerrar_comanda(comandas_ativas):
        print("\n ENCERRAR COMANDA ")
        if comandas_ativas.tamanho == 0:
            print("Não há comandas abertas para encerrar.")
            return

        num_input = input("Digite o número da comanda para encerrar: ").strip()
        if not num_input.isdigit():
            print("Número de comanda inválido!")
            return

        comanda = comandas_ativas.buscar_comanda(int(num_input))
        if not comanda:
            print(f"Comanda {num_input} não encontrada!")
            return

        comandas_ativas.deletar(comanda)
        print(f"Comanda {comanda.numero} do cliente '{comanda.cliente}' foi encerrada!")
