from dados import (
    encomendas,
    produtos,
    datas_bloqueadas,
    stock_maximo_mensal,
    metodos_pagamento,
    metodos_envio
)


ESTADOS_CANCELAMENTO_BLOQUEADO = [
    "Entregue",
    "Cancelada"
]


TIPOS_ENCOMENDA = [
    "personalizada",
    "produto existente"
]


def listar_encomendas():
    return encomendas


def procurar_encomenda_por_id(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return encomenda

    return "Encomenda não encontrada"


def procurar_produto_por_id(produto_id):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    return None


def calcular_preco_com_promocao(produto):
    preco = produto["preco"]

    if produto["promocao"] is None:
        return preco

    desconto = produto["promocao"]["desconto"]
    preco_final = preco - (preco * desconto / 100)

    return round(preco_final, 2)


def contar_encomendas_mes(ano_mes):
    total = 0

    for encomenda in encomendas:
        if encomenda["data_desejada"].startswith(ano_mes):
            total += encomenda["quantidade"]

    return total


def verificar_data_disponivel(data_desejada):
    return data_desejada not in datas_bloqueadas


def verificar_limite_mensal(data_desejada, quantidade):
    ano_mes = data_desejada[:7]
    total_atual = contar_encomendas_mes(ano_mes)

    return total_atual + quantidade <= stock_maximo_mensal["limite"]


def criar_encomenda(
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
    personalizacao=None
):
    if quantidade <= 0:
        return "Quantidade inválida"

    if tipo not in TIPOS_ENCOMENDA:
        return "Tipo de encomenda inválido"

    if metodo_envio not in metodos_envio:
        return "Método de envio inválido"

    if metodo_pagamento not in metodos_pagamento:
        return "Método de pagamento inválido"

    if not verificar_data_disponivel(data_desejada):
        return "Data indisponível para encomendas"

    if not verificar_limite_mensal(data_desejada, quantidade):
        return "Limite mensal de encomendas atingido"

    produto = procurar_produto_por_id(produto_id)

    if produto is None:
        return "Produto não encontrado"

    if not produto["disponivel"]:
        return "Produto indisponível"

    if produto["stock"] < quantidade:
        return "Stock insuficiente"

    novo_id = max((e["id"] for e in encomendas), default=0) + 1
    preco_unitario = calcular_preco_com_promocao(produto)
    total = round(preco_unitario * quantidade, 2)

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
        "metodo_pagamento": metodo_pagamento,
        "morada": morada,
        "data_desejada": data_desejada,
        "total": total,
        "estado": "Pendente",
        "comentarios": ""
    }

    encomendas.append(nova_encomenda)
    produto["stock"] -= quantidade

    if produto["stock"] == 0:
        produto["disponivel"] = False

    return "Encomenda criada com sucesso"


def cancelar_encomenda(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            if encomenda["estado"] in ESTADOS_CANCELAMENTO_BLOQUEADO:
                return "Não é possível cancelar esta encomenda"

            produto = procurar_produto_por_id(encomenda["produto_id"])

            if produto is not None:
                produto["stock"] += encomenda["quantidade"]
                produto["disponivel"] = True

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
    if not verificar_data_disponivel(nova_data):
        return "Data indisponível para encomendas"

    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            quantidade = encomenda["quantidade"]

            if not verificar_limite_mensal(nova_data, quantidade):
                return "Limite mensal de encomendas atingido"

            encomenda["data_desejada"] = nova_data
            return "Data de entrega alterada com sucesso"

    return "Encomenda não encontrada"


def encomendas_pendentes():
    return listar_encomendas_por_estado("Pendente")


def encomendas_entregues():
    return listar_encomendas_por_estado("Entregue")


def encomendas_canceladas():
    return listar_encomendas_por_estado("Cancelada")


def total_vendas():
    total = 0

    for encomenda in encomendas:
        if encomenda["estado"] == "Entregue":
            total += encomenda["total"]

    return round(total, 2)


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
                "metodo_envio": encomenda["metodo_envio"],
                "metodo_pagamento": encomenda["metodo_pagamento"],
                "total": encomenda["total"],
                "estado": encomenda["estado"],
                "data_entrega": encomenda["data_desejada"],
                "comentarios": encomenda.get("comentarios", "")
            }

    return "Encomenda não encontrada"


def estimar_tempo_espera(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            if encomenda["tipo"] == "personalizada":
                return "Tempo estimado: 3 a 5 dias úteis"

            return "Tempo estimado: 1 a 2 dias úteis"

    return "Encomenda não encontrada"


def alerta_atraso(id_encomenda, motivo):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return (
                f'A encomenda {id_encomenda} pode sofrer atraso. '
                f'Motivo: {motivo}'
            )

    return "Encomenda não encontrada"