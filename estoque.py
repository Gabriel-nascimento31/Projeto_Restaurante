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
        self.tamanho -= 1 

    def percorrer(self):
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.proximo
        print("")

    
        
        
            
            
