from dados import encomendas, produtos
from encomendas import criar_encomenda


def adicionar_comentario_encomenda(id_encomenda, comentario):
    """
    Adiciona um comentário a uma encomenda existente
    :param id_encomenda: ID da encomenda
    :param comentario: Comentário ou observação do cliente
    :return: Mensagem de confirmação ou erro
    """
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
    """
    Cliente cria uma nova encomeda
    :param cliente_nome: Nome do cliente
    :param email: Email do cliente
    :param telefone: Número de telefone do cliente
    :param produto_id: ID do produto escolhido
    :param quantidade: Quantidade encomendada
    :param metodo_envio: Método de envio escolhido
    :param metodo_pagamento: Método de pagamento escolhido
    :param morada: Morada de entrega
    :param data_desejada: Data desejada para a encomenda
    :param comentario: Comentário ou personalização adicional
    :return: Mensagem de sucesso ou erro
    """
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
    """
    Lista as encomendas feitas por um cliente com o mesmo email
    :param email: Email do cliente
    :return: Lista de encomendas associadas ao email
    """
    return [
        encomenda for encomenda in encomendas
        if encomenda["email"] == email
    ]


def ver_estado_pedido(id_encomenda):
    """
    Consulta o estado atual de uma encomenda
    :param id_encomenda: ID da encomenda
    :return: Estado da encomenda ou mensagem de erro
    """
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return encomenda["estado"]

    return "Encomenda não encontrada"


def listar_produtos_cliente():
    """
    Lista os produtos disponíveis para o cliente
    :return: Lista de produtos disponíveis e com stock
    """
    return [
        produto for produto in produtos
        if produto["disponivel"] and produto["stock"] > 0
    ]