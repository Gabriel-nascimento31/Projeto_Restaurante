from lista_encadeada import Lista
from comanda import Comanda
from estoque import estoque
from pagamento import Pagamento
from relatorios import gerar_relatorios
from cardapio import cadastrar_item_cardapio, remover_item_cardapio

comandas_ativas = Lista()
historico_pagamentos = Lista()

while True:
    print("\n" + "=" * 35)
    print("      SISTEMA DE RESTAURANTE      ")
    print("=" * 35)
    print("1 - Abrir comanda")
    print("2 - Adicionar itens à comanda")
    print("3 - Remover itens da comanda")
    print("4 - Adicionar itens ao cardápio")
    print("5 - Remover itens do cardápio") 
    print("6 - Ver estoque / Vencimentos")
    print("7 - Adicionar produtos ao estoque ")
    print("8 - Receber pagamento e Baixar estoque")
    print("9 - Encerrar comanda manualmente")
    print("10 - Relatório de vendas")
    print("11 - Sair do sistema")
    print("=" * 35)

    opcao = input("Escolha uma opção (1-11): ").strip()

    if opcao == "1":
        Comanda.abrir_comanda(comandas_ativas)

    elif opcao == '2':
        Comanda.adicionar_itens_comanda(comandas_ativas)

    elif opcao == '3':
        Comanda.remover_item_comanda(comandas_ativas)

    elif opcao == '4':
        cadastrar_item_cardapio()

    elif opcao == '5':
        remover_item_cardapio()

    elif opcao == '6':
        estoque.percorrer()

    elif opcao == '7':
        cadastrar_produto_estoque(estoque)

    elif opcao == '8':
        Pagamento.receber_pagamento(comandas_ativas, historico_pagamentos)
        
    elif opcao == '9':
        Comanda.encerrar_comanda(comandas_ativas)

    elif opcao == '10':
        gerar_relatorios(historico_pagamentos)

    elif opcao == '11':
        print('Encerrando o sistema! ')
        break

    else:
        print('Opção inválida! Digite um número de 1 a 11.')

