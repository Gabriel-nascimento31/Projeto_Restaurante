from lista_encadeada import Lista
from comanda import Comanda
from estoque import estoque
from pagamento import Pagamento
from relatorios import gerar_relatorios

comandas_ativas = Lista()
historico_pagamentos = Lista()

while True:
    print("\n" + "=" * 35)
    print("      SISTEMA DE RESTAURANTE      ")
    print("=" * 35)
    print("1 - Abrir comanda")
    print("2 - Adicionar itens à comanda")
    print("3 - Remover itens da comanda")
    print("4 - Ver estoque / Vencimentos")
    print("5 - Receber pagamento e Baixar estoque")
    print("6 - Encerrar comanda manualmente")
    print("7 - Relatório de vendas")
    print("8 - Sair do sistema")
    print("=" * 35)

    opcao = input("Escolha uma opção (1-8): ").strip()

    if opcao == "1":
        Comanda.abrir_comanda(comandas_ativas)

    elif opcao == '2':
        Comanda.adicionar_itens_comanda(comandas_ativas)

    elif opcao == '3':
        Comanda.remover_item_comanda(comandas_ativas)

    elif opcao == '4':
        estoque.percorrer()

    elif opcao == '5':
        Pagamento.receber_pagamento(comandas_ativas, historico_pagamentos)

    elif opcao == '6':
        Comanda.encerrar_comanda(comandas_ativas)

    elif opcao == '7':
        gerar_relatorios(historico_pagamentos)

    elif opcao == '8':
        print('Encerrando o sistema...')
        break
    else:
        print('Opção inválida! Digite um número de 1 a 8.')

