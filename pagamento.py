from datetime import datetime
from lista_encadeada import Lista
from estoque import estoque


class Pagamento:
    def __init__(self, pagador: str, comanda: int, forma: str, valor: float):
        self.pagador = pagador
        self.comanda = comanda
        self.forma = forma
        self.valor = valor
        self.data_hora_pagamento = datetime.now()



    @staticmethod
    def receber_pagamento(comandas_ativas, historico_pagamentos):
        print("\n RECEBER PAGAMENTO ")
        if comandas_ativas.tamanho == 0:
            print("Não há comandas abertas para receber pagamento.")
            return

        num_input = input("Informe o número da comanda a ser paga: ").strip()
        if not num_input.isdigit():
            print("Número de comanda inválido!")
            return

        comanda = comandas_ativas.buscar_comanda(int(num_input))
        if not comanda:
            print(f"Comanda {num_input} não encontrada!")
            return

        total = comanda.calcular_total()
        print(f"Cliente: {comanda.cliente}")
        print(f"Total a pagar: R${total:.2f}")

        if total == 0:
            print("Esta comanda não possui consumo registrado.")
            return

        forma = input("Forma de pagamento (Dinheiro, Cartão, PIX): ").strip()

        
        atual = comanda.refeicoes_pedidas.inicio
        while atual:
            estoque.baixar_estoque_item(atual.dado.nome)
            atual = atual.ponteiro

        atual = comanda.bebidas_pedidas.inicio
        while atual:
            estoque.baixar_estoque_item(atual.dado.nome)
            atual = atual.ponteiro

        novo_pagamento = Pagamento(
            pagador=comanda.cliente,
            comanda=comanda.numero,
            forma=forma,
            valor=total
        )
        historico_pagamentos.adicionar(novo_pagamento)

        print(f"\nPagamento de R${total:.2f} registrado com sucesso via {forma}!")
        
        
        
        comandas_ativas.deletar(comanda)
        print(f"Comanda {comanda.numero} encerrada.")
          