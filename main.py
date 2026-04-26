import admin
import encomendas
import produtos

from dados import metodos_envio, metodos_pagamento


def mostrar_lista(titulo, lista):
    print(f"\n=== {titulo} ===")

    if not lista:
        print("Sem resultados.")
        return

    for item in lista:
        print(item)


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
        print("2 - Procurar produto por nome")
        print("3 - Filtrar por categoria")
        print("4 - Filtrar por sabor")
        print("5 - Filtrar por tamanho")
        print("6 - Filtrar por cor")
        print("7 - Criar encomenda")
        print("8 - Ver encomendas")
        print("9 - Cancelar encomenda")
        print("10 - Ver tempo estimado")
        print("11 - Avaliar produto")
        print("12 - Ver avaliações de produto")
        print("13 - Ver produto do dia")
        print("0 - Voltar")

        opcao = input("Escolhe: ")

        if opcao == "1":
            mostrar_lista("Produtos", produtos.listar_produtos())

        elif opcao == "2":
            nome = input("Nome do produto: ")
            mostrar_lista("Resultados", produtos.procurar_por_nome(nome))

        elif opcao == "3":
            categoria = input("Categoria: ")
            mostrar_lista(
                "Produtos por categoria",
                produtos.filtrar_por_categoria(categoria)
            )

        elif opcao == "4":
            sabor = input("Sabor: ")
            mostrar_lista("Produtos por sabor", produtos.filtrar_por_sabor(sabor))

        elif opcao == "5":
            tamanho = input("Tamanho: ")
            mostrar_lista(
                "Produtos por tamanho",
                produtos.filtrar_por_tamanho(tamanho)
            )

        elif opcao == "6":
            cor = input("Cor: ")
            mostrar_lista("Produtos por cor", produtos.filtrar_por_cor(cor))

        elif opcao == "7":
            criar_encomenda_cliente()

        elif opcao == "8":
            mostrar_lista("Encomendas", encomendas.listar_encomendas())

        elif opcao == "9":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(encomendas.cancelar_encomenda(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "10":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(encomendas.estimar_tempo_espera(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "11":
            avaliar_produto_cliente()

        elif opcao == "12":
            try:
                id_produto = int(input("ID do produto: "))
                mostrar_lista(
                    "Avaliações",
                    produtos.listar_avaliacoes(id_produto)
                )
            except ValueError:
                print("ID inválido.")

        elif opcao == "13":
            print(produtos.produto_do_dia())

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def criar_encomenda_cliente():
    try:
        cliente_nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        tipo = input("Tipo (personalizada/produto existente): ")
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))

        print("\nMétodos de envio disponíveis:")
        print(metodos_envio)
        metodo_envio = input("Escolhe método de envio: ")

        print("\nMétodos de pagamento disponíveis:")
        print(metodos_pagamento)
        metodo_pagamento = input("Escolhe método de pagamento: ")

        morada = input("Morada: ")
        data_desejada = input("Data desejada (YYYY-MM-DD): ")

        personalizacao = {}

        if tipo == "personalizada":
            personalizacao = {
                "sabor": input("Sabor personalizado: "),
                "tamanho": input("Tamanho: "),
                "cor": input("Cor: ")
            }

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
                data_desejada,
                personalizacao
            )
        )

    except ValueError:
        print("Dados inválidos.")


def avaliar_produto_cliente():
    try:
        id_produto = int(input("ID do produto: "))
        nota = int(input("Nota (1 a 5): "))
        comentario = input("Comentário: ")

        print(
            produtos.avaliar_produto(
                id_produto,
                nota,
                comentario
            )
        )

    except ValueError:
        print("Dados inválidos.")


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
        print("9 - Ver produtos novos")
        print("10 - Ver produtos em promoção")
        print("11 - Ver lista de compras")
        print("12 - Ver redes sociais")
        print("13 - Bloquear data")
        print("14 - Ver datas bloqueadas")
        print("15 - Adicionar promoção")
        print("16 - Ver métodos de pagamento")
        print("0 - Voltar")

        opcao = input("Escolhe: ")

        if opcao == "1":
            mostrar_lista("Produtos", admin.mostrar_produtos())

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
            alterar_estado_admin()

        elif opcao == "6":
            try:
                id_encomenda = int(input("ID da encomenda: "))
                print(admin.ver_checkout_encomenda(id_encomenda))
            except ValueError:
                print("ID inválido.")

        elif opcao == "7":
            email = input("Email do cliente: ")
            mostrar_lista(
                "Histórico do cliente",
                admin.historico_compras_cliente(email)
            )

        elif opcao == "8":
            mostrar_lista("Encomendas ordenadas", admin.ordenar_por_data())

        elif opcao == "9":
            mostrar_lista("Produtos novos", admin.listar_produtos_novos())

        elif opcao == "10":
            mostrar_lista(
                "Produtos em promoção",
                admin.listar_produtos_em_promocao()
            )

        elif opcao == "11":
            mostrar_lista("Lista de compras", admin.ver_lista_compras())

        elif opcao == "12":
            print(admin.ver_rede_social())

        elif opcao == "13":
            data = input("Data a bloquear (YYYY-MM-DD): ")
            print(admin.bloquear_data(data))

        elif opcao == "14":
            mostrar_lista("Datas bloqueadas", admin.listar_datas_bloqueadas())

        elif opcao == "15":
            adicionar_promocao_admin()

        elif opcao == "16":
            mostrar_lista(
                "Métodos de pagamento",
                admin.mostrar_metodos_pagamento()
            )

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def alterar_estado_admin():
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


def adicionar_promocao_admin():
    try:
        id_produto = int(input("ID do produto: "))
        desconto = float(input("Desconto (%): "))
        data_inicio = input("Data de início (YYYY-MM-DD): ")
        data_fim = input("Data de fim (YYYY-MM-DD): ")

        print(
            admin.adicionar_promocao(
                id_produto,
                desconto,
                data_inicio,
                data_fim
            )
        )

    except ValueError:
        print("Dados inválidos.")


if __name__ == "__main__":
    menu_principal()