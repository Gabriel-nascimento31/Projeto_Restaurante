from produto import Produto


class Nó_fila:
    def __init__(self, dado=None, proximo=None, anterior=None):
        self.dado = dado
        self.proximo = proximo
        self.anterior = anterior


class Fila: 
    def __init__(self): 
        self.inicio = None 
        self.fim = None 
        self.tamanho = 0 

    def enfileirar(self, dado): 
        novo_no = Nó_fila(dado, None, None) 
        if self.inicio == None: 
            self.inicio = novo_no
            self.fim = self.inicio
        else: 
            novo_no.anterior = self.fim 
            self.fim.proximo = novo_no 
            self.fim = novo_no

        self.tamanho += 1 


    def desinfileirar(self): 
        if self.tamanho == 1: 
            self.tamanho -= 1 
            self.inicio = None 
            self.fim = None 
        elif self.tamanho > 1: 
            self.inicio = self.inicio.proximo 
            self.inicio.anterior = None 
        elif self.tamanho <1:
            print("A fila está vazia")
        

    def percorrer(self):
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.proximo
        print("")

    
estoque = Fila()

produto1 = Produto()
produto2 = Produto()
produto3 = Produto()
produto4 = Produto()
produto5 = Produto()
produto6 = Produto()
produto7 = Produto()
produto8 = Produto()
produto9 = Produto()
produto10 = Produto()


estoque.enfileirar(produto1)
estoque.enfileirar(produto2)
estoque.enfileirar(produto3)
estoque.enfileirar(produto4)
estoque.enfileirar(produto5)
estoque.enfileirar(produto6)
estoque.enfileirar(produto7)
estoque.enfileirar(produto8)
estoque.enfileirar(produto9)
estoque.enfileirar(produto10)

        
            
            
