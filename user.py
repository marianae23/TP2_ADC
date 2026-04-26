from dados import encomendas, produtos
from admin import *
def adicionar_comentario_encomenda(id_encomenda, comentario):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["comentarios"] = comentario
            return "Comentário adicionado com sucesso!"

    return "encomenda não encontrada"

def fazer_pedido(cliente_nome, email, telefone, produto_id, quantidade, metodo_envio, morada, data_desejada, comentario):
    produto_escolhido = None

    for produto in produtos:
        if produto["id"] == produto_id:
            produto_escolhido = produto
            break

    if produto_escolhido is None:
        return "Produto não encontrado."

    if produto_escolhido["disponivel"] == False:
        return "Produto indisponível."

    if produto_escolhido["stock"] < quantidade:
        return "Stock insuficiente."

    novo_id = max(e["id"] for e in encomendas) + 1 if encomendas else 1
    total = produto_escolhido["preco"] * quantidade

    nova_encomenda = {
        "id": novo_id,
        "cliente_nome": cliente_nome,
        "email": email,
        "telefone": telefone,
        "tipo": "normal",
        "produto_id": produto_id,
        "personalizacao": {},
        "quantidade": quantidade,
        "metodo_envio": metodo_envio,
        "morada": morada,
        "data_desejada": data_desejada,
        "total": total,
        "estado": "Pendente",
        "comentarios": comentario
    }

    encomendas.append(nova_encomenda)
    produto_escolhido["stock"] -= quantidade

    if produto_escolhido["stock"] == 0:
        produto_escolhido["disponivel"] = False

    return f'Pedido criado com sucesso! Total: €{total}'

while True:
    print("\nMENU DE USUARIO")
    print("1 - Ver produtos")
    print("2 - Fazer comentário na encomenda")
    print("3 - Fazer uma encomenda")
    print("0 - Sair")

    opcao = input("Escolhe: ")

    if opcao == "1":
        print(mostrar_produtos())

    elif opcao == "2":
        id_enc = int(input("ID da encomenda: "))
        comentario = input("Comentário: ")
        print(adicionar_comentario_encomenda(id_enc, comentario))

    elif opcao == "3":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))
        metodo_envio = input("Método de envio: ")
        morada = input("Morada: ")
        data = input("Data desejada: ")
        comentario = input("Comentário/personalização: ")
        print(fazer_pedido(nome, email, telefone, produto_id, quantidade, metodo_envio, morada, data, comentario))

    elif opcao == "0":
        break

def adicionar_comentario_encomenda(id_encomenda, comentario):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["comentarios"] = comentario
            return "Comentário adicionado com sucesso!"

    return "Encomenda não encontrada"