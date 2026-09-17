from produto import Produto
from datetime import date, timedelta, datetime

class Nó_fila:
    def __init__(self, dado=None, proximo=None, anterior=None):
        self.dado = dado
        self.proximo = proximo
        self.anterior = anterior


class FilaEstoque: 
    def __init__(self): 
        self.inicio = None 
        self.fim = None 
        self.tamanho = 0 

    def enfileirar(self, produto: Produto):
        novo_no = Nó_fila(produto)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            atual = self.inicio
            inserido = False
            while atual:
                if produto.data_vencimento < atual.dado.data_vencimento:
                    if atual.anterior:
                        atual.anterior.proximo = novo_no
                        novo_no.anterior = atual.anterior
                    else:
                        self.inicio = novo_no
                    novo_no.proximo = atual
                    atual.anterior = novo_no
                    inserido = True
                    break
                atual = atual.proximo

            if not inserido:
                novo_no.anterior = self.fim
                self.fim.proximo = novo_no
                self.fim = novo_no

        self.tamanho += 1


    def baixar_estoque_item(self, nome_item: str, quantidade: float = 1.0):
        atual = self.inicio
        while atual:
            if atual.dado.nome.lower() == nome_item.lower() and atual.dado.quantidade > 0:
                if atual.dado.quantidade >= quantidade:
                    atual.dado.quantidade -= quantidade
                    return True
                else:
                    quantidade -= atual.dado.quantidade
                    atual.dado.quantidade = 0
            atual = atual.proximo
        return False

    
    def editar_quantidade(self, nome_item: str, nova_quantidade: float):
        atual = self.inicio
        while atual:
            if atual.dado.nome.lower() == nome_item.lower():
                atual.dado.quantidade = nova_quantidade
                return True
            atual = atual.proximo
        return False
    
    def percorrer(self):
        if self.tamanho == 0:
            print("Estoque vazio.")
            return
        atual = self.inicio
        print("\n ITENS EM ESTOQUE (Ordenados por Vencimento) ")
        while atual:
            print(atual.dado)
            atual = atual.proximo
        print("")
    
    



estoque = FilaEstoque()


hoje = date.today()
estoque.enfileirar(Produto("macarronada", 4.0, 10.0, 50, data_vencimento=date.today() + timedelta(days=5)))
estoque.enfileirar(Produto("arroz", 2.0, 5.0, 20, data_vencimento=date.today() + timedelta(days=30)))
estoque.enfileirar(Produto("feijão", 12.0, 18.0, 30, data_vencimento=date.today() + timedelta(days=5)))
estoque.enfileirar(Produto("refrigerante", 3.0, 8.0, 40, data_vencimento=date.today() + timedelta(days=200)))
estoque.enfileirar(Produto("suco", 2.0, 5.0, 30, data_vencimento=date.today() + timedelta(days=90)))
estoque.enfileirar(Produto("agua com gas", 1.0, 3.0, 50, data_vencimento=date.today() + timedelta(days=150)))
estoque.enfileirar(Produto("lazanha", 50.0, 70.0, 8, data_vencimento=date.today() + timedelta(days=5)))
estoque.enfileirar(Produto("nhoque", 30.0, 40.0, 10, data_vencimento=date.today() + timedelta(days=3)))
estoque.enfileirar(Produto("frango assado", 35.0, 80.0, 5, data_vencimento=date.today() + timedelta(days=2)))
estoque.enfileirar(Produto("almondenga", 10.0, 18.0, 30, data_vencimento=date.today() + timedelta(days=5)))
estoque.enfileirar(Produto("hamburguer", 25.0, 35.0, 20, data_vencimento=date.today() + timedelta(days=2)))
estoque.enfileirar(Produto("bife frito", 65.0, 70.0, 50, data_vencimento=date.today() + timedelta(days=3)))
estoque.enfileirar(Produto("filé de frango", 20.0, 30.0, 100, data_vencimento=date.today() + timedelta(days=1)))
