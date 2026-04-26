import admin
import encomendas


def menu_principal():
    while True:
        print("\n=== DOCERIA ===")
        print("1 - Modo Cliente")
        print("2 - Modo Administrador")
        print("0 - Sair")

        opcao = input("Escolhe: ")

        if opcao == "1":
            menu_cliente()

        elif opcao == "2":
            menu_admin()

        elif opcao == "0":
            print("A sair do sistema...")
            break

        else:
            print("Opção inválida.")


def menu_cliente():
    while True:
        print("\n=== CLIENTE ===")
        print("1 - Ver produtos")
        print("2 - Criar encomenda")
        print("3 - Ver encomendas")
        print("4 - Cancelar encomenda")
        print("5 - Ver tempo estimado")
        print("0 - Voltar")

        opcao = input("Escolhe: ")

        if opcao == "1":
            print(admin.mostrar_produtos())

        elif opcao == "2":
            try:
                cliente_nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                tipo = input("Tipo (personalizada/produto existente): ")
                produto_id = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                metodo_envio = input("Método de envio: ")
                metodo_pagamento = input("Método de pagamento: ")
                morada = input("Morada: ")
                data_desejada = input("Data desejada (YYYY-MM-DD): ")

                print(
                    encomendas.criar_encomenda(
                        cliente_nome,
                        email,
                        telefone,
                        tipo,
                        produto_id,
                        quantidade,
                        metodo_envio,
                        metodo_pagamento,
                        morada,
                        data_desejada
                    )
                )

            except ValueError:
                print("Dados inválidos.")

        elif opcao == "3":
            print(encomendas.listar_encomendas())

        elif opcao == "4":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(encomendas.cancelar_encomenda(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(encomendas.estimar_tempo_espera(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_admin():
    while True:
        print("\n=== ADMIN ===")
        print("1 - Ver produtos")
        print("2 - Verificar stock")
        print("3 - Alterar preço")
        print("4 - Remover produto")
        print("5 - Alterar estado encomenda")
        print("6 - Ver checkout")
        print("7 - Ver histórico cliente")
        print("8 - Ver encomendas ordenadas")
        print("0 - Voltar")

        opcao = input("Escolhe: ")

        if opcao == "1":
            print(admin.mostrar_produtos())

        elif opcao == "2":
            try:
                id_prod = int(input("ID do produto: "))
                print(admin.verificar_stock(id_prod))
            except ValueError:
                print("ID inválido.")

        elif opcao == "3":
            try:
                id_prod = int(input("ID do produto: "))
                preco = float(input("Novo preço: "))
                print(admin.alterar_precos(id_prod, preco))
            except ValueError:
                print("Valor inválido.")

        elif opcao == "4":
            try:
                id_prod = int(input("ID do produto: "))
                print(admin.remover_produto(id_prod))
            except ValueError:
                print("ID inválido.")

        elif opcao == "5":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                novo_estado = input("Novo estado: ")
                print(
                    admin.alterar_estado_encomenda(
                        id_encomenda,
                        novo_estado
                    )
                )
            except ValueError:
                print("ID inválido.")

        elif opcao == "6":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(admin.ver_checkout_encomenda(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "7":
            email = input("Email do cliente: ")
            print(admin.historico_compras_cliente(email))

        elif opcao == "8":
            print(admin.ordenar_por_data())

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


menu_principal()