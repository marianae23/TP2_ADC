from dados import encomendas, produtos


def listar_encomendas():
    return encomendas


def procurar_encomenda_por_id(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return encomenda

    return "Encomenda não encontrada"


def criar_encomenda(
    cliente_nome,
    email,
    telefone,
    tipo,
    produto_id,
    quantidade,
    metodo_envio,
    morada,
    data_desejada,
    personalizacao=None
):
    produto = None

    for p in produtos:
        if p["id"] == produto_id:
            produto = p
            break

    if produto is None:
        return "Produto não encontrado"

    if produto["stock"] < quantidade:
        return "Stock insuficiente"

    novo_id = max((e["id"] for e in encomendas), default=0) + 1
    total = produto["preco"] * quantidade

    nova_encomenda = {
        "id": novo_id,
        "cliente_nome": cliente_nome,
        "email": email,
        "telefone": telefone,
        "tipo": tipo,
        "produto_id": produto_id,
        "personalizacao": personalizacao if personalizacao else {},
        "quantidade": quantidade,
        "metodo_envio": metodo_envio,
        "morada": morada,
        "data_desejada": data_desejada,
        "total": total,
        "estado": "Pendente"
    }

    encomendas.append(nova_encomenda)
    produto["stock"] -= quantidade

    if produto["stock"] == 0:
        produto["disponivel"] = False

    return "Encomenda criada com sucesso"


def cancelar_encomenda(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            if encomenda["estado"] == "Entregue":
                return "Não é possível cancelar uma encomenda entregue"

            encomenda["estado"] = "Cancelada"
            return "Encomenda cancelada com sucesso"

    return "Encomenda não encontrada"


def listar_encomendas_por_estado(estado):
    return [
        encomenda for encomenda in encomendas
        if encomenda["estado"].lower() == estado.lower()
    ]


def calcular_total_encomenda(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return encomenda["total"]

    return "Encomenda não encontrada"


def alterar_data_entrega(id_encomenda, nova_data):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["data_desejada"] = nova_data
            return "Data de entrega alterada com sucesso"

    return "Encomenda não encontrada"


def encomendas_pendentes():
    return [
        encomenda for encomenda in encomendas
        if encomenda["estado"] == "Pendente"
    ]


def encomendas_entregues():
    return [
        encomenda for encomenda in encomendas
        if encomenda["estado"] == "Entregue"
    ]


def encomendas_canceladas():
    return [
        encomenda for encomenda in encomendas
        if encomenda["estado"] == "Cancelada"
    ]


def total_vendas():
    total = 0

    for encomenda in encomendas:
        if encomenda["estado"] == "Entregue":
            total += encomenda["total"]

    return total


def ordenar_encomendas_por_data():
    return sorted(
        encomendas,
        key=lambda encomenda: encomenda["data_desejada"]
    )


def resumo_encomenda(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return {
                "cliente": encomenda["cliente_nome"],
                "produto_id": encomenda["produto_id"],
                "quantidade": encomenda["quantidade"],
                "total": encomenda["total"],
                "estado": encomenda["estado"],
                "data_entrega": encomenda["data_desejada"]
            }

    return "Encomenda não encontrada"