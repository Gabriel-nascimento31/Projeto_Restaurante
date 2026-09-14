from datetime import datetime
from lista_encadeada import Lista
from comanda import comandas_ativas

historico_pagamentos = Lista()


class Pagamento:
    def __init__(self, pagador=str, comanda=int, forma=str, valor=float):
        self.pagador = pagador
        self.comanda = comanda
        self.forma = forma
        self.valor = valor
        self.data_hora_pagamento = datetime.now()



    def receber_pagamento(comandas_ativas, historico_pagamentos):
        print(" RECEBER PAGAMENTO ")
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
            print("Esta comanda não possui consumição registrada.")
            return

        forma = input("Forma de pagamento (Dinheiro, Cartão, PIX): ").strip()
    
    
        novo_pagamento = Pagamento(
            pagador=comanda.cliente,
            comanda=comanda.número,
            forma=forma,
            valor=total
        )
        historico_pagamentos.adicionar(novo_pagamento)
    
        print(f"\nPagamento de R${total:.2f} registrado com sucesso via {forma}!")
        print("Dica: Lembre-se de encerrar a comanda na Opção 5.")



pagamento = Pagamento()
lista_pagamentos = Lista()




        
        
          