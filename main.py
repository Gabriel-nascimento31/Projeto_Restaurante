


from lista_encadeada import Lista
from comanda import Comanda, Item
from estoque import Fila, estoque  
from cardapio import cardapio    
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
    print("3 - Ver estoque (Fila)")
    print("4 - Receber pagamento do cliente")
    print("5 - Encerrar comanda")
    print("6 - Relatório de vendas")
    print("7 - Encerrar sistema")
    print("=" * 35)

    opcao = input("Escolha uma opção (1-7): ").strip()

    if opcao == "1":
        Comanda.abrir_comanda(comandas_ativas)

    elif opcao == '2':
        Comanda.adicionar_itens_comanda(comandas_ativas)

    elif opcao == '3':
        estoque.percorrer()

    elif opcao == '4':
        Pagamento.receber_pagamento(comandas_ativas, historico_pagamentos)

    elif opcao == '5':
        Comanda.encerrar_comanda(comandas_ativas)

    elif opcao == '6':
        gerar_relatorios(historico_pagamentos)

    elif opcao == '7':
        print('Encerrando o sistema')
        break
    else:
        print('Opção inválida')



