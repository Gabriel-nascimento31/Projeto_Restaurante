from lista_encadeada import Lista

historico_pagamentos = Lista()

def gerar_relatorios(historico_pagamentos):
    print(" RELATÓRIO DE VENDAS E CONSUMO ")
    if historico_pagamentos.tamanho == 0:
        print("Nenhum pagamento registrado até o momento.")
        return

    total_faturado = 0.0
    total_transacoes = 0

    print("\nHistórico de Transações:")
    print("-" * 50)
    
    atual = historico_pagamentos.inicio
    while atual:
        pg = atual.dado
        print(f"Comanda {pg.comanda}  Cliente: {pg.pagador}  Forma: {pg.forma}  Valor: R${pg.valor:.2f}")
        total_faturado += pg.valor
        total_transacoes += 1
        atual = atual.ponteiro

    print("-" * 50)
    print(f"Total de Transações: {total_transacoes}")
    print(f"Faturamento Total: R${total_faturado:.2f}")
    print("-" * 50)