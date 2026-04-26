from admin import *
from user import *
from dados import encomendas, estados_encomenda, metodos_envio, formas_pagamento


while True:
    print("\nSISTEMA")
    print("1 - Admin")
    print("2 - Utilizador")
    print("0 - Sair")

    opcao_sistema = input("Escolhe: ")

    if opcao_sistema == "1":
        while True:
            print("\n MENU DE ADMIN")
            print("1 - Ver produtos")
            print("2 - Verificar stock")
            print("3 - Alterar preço")
            print("4 - Remover produto")
            print("5 - Alterar estado de encomenda")
            print("6 - Ver encomendas")
            print("0 - Voltar")

            opcao_admin = input("Escolhe: ")

            if opcao_admin == "1":
                print(mostrar_produtos())

            elif opcao_admin == "2":
                id_prod = int(input("ID do produto: "))
                print(verificar_stock(id_prod))

            elif opcao_admin == "3":
                id_prod = int(input("ID: "))
                preco = float(input("Novo preço: "))
                print(alterar_precos(id_prod, preco))

            elif opcao_admin == "4":
                id_prod = int(input("ID: "))
                print(remover_produto(id_prod))

            elif opcao_admin == "5":
                id_enc = int(input("ID da encomenda: "))

                print("Estados disponíveis:")
                for i, estado in enumerate(estados_encomenda, 1):
                    print(f"{i} - {estado}")

                opcao_estado = int(input("Escolhe o novo estado: "))

                if opcao_estado < 1 or opcao_estado > len(estados_encomenda):
                    print("Opção inválida")
                else:
                    novo_estado = estados_encomenda[opcao_estado - 1]
                    print(alterar_estado_encomenda(id_enc, novo_estado))

            elif opcao_admin == "6":
                print("\nENCOMENDAS:")
                for encomenda in encomendas:
                    print(encomenda)

            elif opcao_admin == "0":
                break

    elif opcao_sistema == "2":
        while True:
            print("\nMENU DE USUARIO")
            print("1 - Ver produtos")
            print("2 - Fazer comentário na encomenda")
            print("3 - Fazer uma encomenda")
            print("0 - Voltar")

            opcao_user = input("Escolhe: ")

            if opcao_user == "1":
                print(mostrar_produtos())

            elif opcao_user == "2":
                id_enc = int(input("ID da encomenda: "))
                comentario = input("Comentário: ")
                print(adicionar_comentario_encomenda(id_enc, comentario))

            elif opcao_user == "3":
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                produto_id = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))

                print("Métodos de envio disponíveis:")
                for i, envio in enumerate(metodos_envio, 1):
                    print(f"{i} - {envio}")

                opcao_envio = int(input("Escolhe o método de envio: "))

                if opcao_envio < 1 or opcao_envio > len(metodos_envio):
                    print("Opção inválida")
                    continue

                metodo_envio = metodos_envio[opcao_envio - 1]

                morada = input("Morada: ")
                data = input("Data desejada: ")
                comentario = input("Comentário/personalização: ")

                print("Formas de pagamento disponíveis:")
                for i, pagamento in enumerate(formas_pagamento, 1):
                    print(f"{i} - {pagamento}")

                opcao_pagamento = int(input("Escolhe a forma de pagamento: "))

                if opcao_pagamento < 1 or opcao_pagamento > len(formas_pagamento):
                    print("Opção inválida")
                    continue

                forma_pagamento = formas_pagamento[opcao_pagamento - 1]

                print(fazer_pedido(nome, email, telefone, produto_id, quantidade, metodo_envio, morada, data, comentario, forma_pagamento))

            elif opcao_user == "0":
                break

    elif opcao_sistema == "0":
        break