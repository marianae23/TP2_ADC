from dados import encomendas, produtos
from encomendas import criar_encomenda


def adicionar_comentario_encomenda(id_encomenda, comentario):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["comentarios"] = comentario
            return "Comentário adicionado com sucesso!"

    return "Encomenda não encontrada"


def fazer_pedido(
    cliente_nome,
    email,
    telefone,
    produto_id,
    quantidade,
    metodo_envio,
    metodo_pagamento,
    morada,
    data_desejada,
    comentario=""
):
    resultado = criar_encomenda(
        cliente_nome=cliente_nome,
        email=email,
        telefone=telefone,
        tipo="produto existente",
        produto_id=produto_id,
        quantidade=quantidade,
        metodo_envio=metodo_envio,
        metodo_pagamento=metodo_pagamento,
        morada=morada,
        data_desejada=data_desejada
    )

    if resultado != "Encomenda criada com sucesso":
        return resultado

    encomenda_criada = encomendas[-1]
    encomenda_criada["comentarios"] = comentario

    return f'Pedido criado com sucesso! Total: €{encomenda_criada["total"]}'


def listar_pedidos_cliente(email):
    return [
        encomenda for encomenda in encomendas
        if encomenda["email"] == email
    ]


def ver_estado_pedido(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return encomenda["estado"]

    return "Encomenda não encontrada"


def listar_produtos_cliente():
    return [
        produto for produto in produtos
        if produto["disponivel"] and produto["stock"] > 0
    ]