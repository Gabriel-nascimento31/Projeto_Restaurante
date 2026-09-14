def gerar_relatorios(historico_pagamentos):
    print("\n" + "=" * 40)
    print("        RELATÓRIO DE VENDAS       ")
    print("=" * 40)

    if historico_pagamentos.tamanho == 0:
        print("Nenhum pagamento registrado até o momento.")
        return

    total_acumulado = 0.0
    atual = historico_pagamentos.inicio
    
    while atual:
        p = atual.dado
        print(f"Comanda {p.comanda}  Cliente: {p.pagador}  Forma: {p.forma}  Valor: R${p.valor:.2f}  Data: {p.data_hora_pagamento.strftime('%d/%m/%Y %H:%M')}")
        total_acumulado += p.valor
        atual = atual.ponteiro

    print("-" * 40)
    print(f"TOTAL GERAL DE VENDAS: R${total_acumulado:.2f}")
    print("=" * 40)



