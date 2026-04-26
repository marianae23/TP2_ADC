from admin import *
while True:
    print("ADMIN")
    print("1 - Ver produtos")
    print("2 - Verificar stock")
    print("3 - Alterar preço")
    print("4 - Remover produto")
    print("0 - Sair")

    opcao = input("Escolhe: ")

    if opcao == "1":
        print(produtos)

    elif opcao == "2":
        id_prod = int(input("ID do produto: "))
        print(verificar_stock(id_prod))

    elif opcao == "3":
        id_prod = int(input("ID: "))
        preco = float(input("Novo preço: "))
        print(alterar_precos(id_prod, preco))

    elif opcao == "4":
        id_prod = int(input("ID: "))
        print(remover_produto(id_prod))

    elif opcao == "0":
        break