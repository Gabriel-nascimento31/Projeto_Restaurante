class Nó_lista:
    def __init__(self, dado=dict):
        self.dado = dado
        self.ponteiro = None



class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0


    def adicionar(self, dado):
        nó = Nó_lista(dado)
        if self.fim:
            self.fim.ponteiro = nó
            self.fim = nó
        else:
            self.inicio = nó
            self.fim = nó
        self.tamanho += 1

    def deletar(self, dado):
        atual = self.inicio
        anterior = self.inicio
        while atual:
            if atual.dado == dado:
                if atual == self.inicio:
                    self.inicio = atual.ponteiro
                    if self.inicio is None:
                        self.fim = None

                else:
                    anterior.ponteiro = atual.ponteiro
                    if atual == self.fim:
                        self.fim = anterior

                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.ponteiro


    def esvaziar_lista(self):
        self.fim = None
        self.inicio = None
        self.tamanho = 0


    

    def buscar_comanda(self, numero):
        atual = self.inicio
        while atual:
            if atual.dado.número == int(numero):
                return atual.dado
            atual = atual.ponteiro
        return None

    def buscar_item_cardapio(self, nome_item):
        atual = self.inicio
        while atual:
            if atual.dado.nome.lower() == nome_item.lower():
                return atual.dado
            atual = atual.ponteiro
        return None