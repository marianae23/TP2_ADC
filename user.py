from dados import encomendas, produtos, formas_pagamento, metodos_envio
from admin import *


def adicionar_comentario_encomenda(id_encomenda, comentario):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["comentarios"] = comentario
            return "Comentário adicionado com sucesso!"

    return "Encomenda não encontrada"


def fazer_pedido(cliente_nome, email, telefone, produto_id, quantidade, metodo_envio, morada, data_desejada, comentario, forma_pagamento):
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
        "comentarios": comentario,
        "forma_pagamento": forma_pagamento
    }

    encomendas.append(nova_encomenda)
    produto_escolhido["stock"] -= quantidade

    if produto_escolhido["stock"] == 0:
        produto_escolhido["disponivel"] = False

    return f"Pedido criado com sucesso! Total: €{total}"
