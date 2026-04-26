from dados import (
    encomendas,
    produtos,
    datas_bloqueadas,
    stock_maximo_mensal,
    lista_compras,
    rede_social
)


ESTADOS_VALIDOS = [
    "Pendente",
    "Em preparação",
    "Pronto para recolha",
    "Enviado",
    "Entregue",
    "Cancelada"
]


def ordenar_por_data():
    return sorted(encomendas, key=lambda e: e["data_desejada"])


def mostrar_produtos():
    return produtos


def mostrar_produtos_disponiveis():
    return [
        produto for produto in produtos
        if produto["disponivel"] and produto["stock"] > 0
    ]


def alterar_estado_encomenda(id_encomenda, novo_estado):
    if novo_estado not in ESTADOS_VALIDOS:
        return "Estado inválido"

    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["estado"] = novo_estado
            return "Estado da encomenda alterado com sucesso"

    return "Encomenda não encontrada"


def verificar_stock(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            if produto["stock"] > 0 and produto["disponivel"]:
                return (
                    f'O produto {produto["nome"]} está disponível. '
                    f'Stock: {produto["stock"]}'
                )
            return f'O produto {produto["nome"]} está indisponível ou sem stock.'

    return "Produto não encontrado"


def adicionar_produto(
    nome,
    categoria,
    preco,
    stock,
    sabores,
    tamanhos,
    cores,
    intolerancias
):
    if preco <= 0:
        return "Preço inválido"

    if stock < 0:
        return "Stock inválido"

    novo_id = max((p["id"] for p in produtos), default=0) + 1

    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "stock": stock,
        "disponivel": stock > 0,
        "sabores": sabores,
        "tamanhos": tamanhos,
        "cores": cores,
        "intolerancias": intolerancias,
        "promocao": None,
        "novo": True,
        "avaliacoes": []
    }

    produtos.append(novo_produto)
    return f'Produto "{nome}" adicionado com sucesso!'


def remover_produto(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["disponivel"] = False
            return f'Produto "{produto["nome"]}" marcado como indisponível.'

    return "Produto não encontrado."


def alterar_precos(id_produto, novo_preco):
    if novo_preco <= 0:
        return "Preço inválido"

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["preco"] = novo_preco
            return f'Preço do produto "{produto["nome"]}" atualizado para €{novo_preco}'

    return "Produto não encontrado"


def editar_stock(id_produto, novo_stock):
    if novo_stock < 0:
        return "Stock inválido"

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["stock"] = novo_stock
            produto["disponivel"] = novo_stock > 0
            return f'Stock do produto "{produto["nome"]}" atualizado.'

    return "Produto não encontrado"


def adicionar_promocao(id_produto, desconto, data_inicio, data_fim):
    if desconto <= 0 or desconto >= 100:
        return "Desconto inválido"

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["promocao"] = {
                "desconto": desconto,
                "data_inicio": data_inicio,
                "data_fim": data_fim
            }
            return f'Promoção adicionada ao produto "{produto["nome"]}".'

    return "Produto não encontrado"


def remover_promocao(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["promocao"] = None
            return f'Promoção removida do produto "{produto["nome"]}".'

    return "Produto não encontrado"


def listar_produtos_novos():
    return [produto for produto in produtos if produto["novo"]]


def listar_produtos_em_promocao():
    return [
        produto for produto in produtos
        if produto["promocao"] is not None
    ]


def ver_checkout_encomenda(id_encomenda):
    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            return {
                "cliente": encomenda["cliente_nome"],
                "email": encomenda["email"],
                "telefone": encomenda["telefone"],
                "morada": encomenda["morada"],
                "data_desejada": encomenda["data_desejada"],
                "metodo_envio": encomenda["metodo_envio"],
                "metodo_pagamento": encomenda.get("metodo_pagamento", "Não definido"),
                "total": encomenda["total"],
                "estado": encomenda["estado"]
            }

    return "Encomenda não encontrada"


def historico_compras_cliente(email):
    return [
        encomenda for encomenda in encomendas
        if encomenda["email"] == email
    ]


def bloquear_data(data):
    if data in datas_bloqueadas:
        return "Esta data já está bloqueada"

    datas_bloqueadas.append(data)
    return "Data bloqueada com sucesso"


def desbloquear_data(data):
    if data not in datas_bloqueadas:
        return "Esta data não está bloqueada"

    datas_bloqueadas.remove(data)
    return "Data desbloqueada com sucesso"


def listar_datas_bloqueadas():
    return datas_bloqueadas


def definir_stock_maximo_mensal(limite):
    if limite <= 0:
        return "Limite inválido"

    stock_maximo_mensal["limite"] = limite
    return "Stock máximo mensal atualizado"


def contar_encomendas_mes(ano_mes):
    total = 0

    for encomenda in encomendas:
        if encomenda["data_desejada"].startswith(ano_mes):
            total += encomenda["quantidade"]

    return total


def verificar_limite_mensal(ano_mes):
    total = contar_encomendas_mes(ano_mes)

    if total >= stock_maximo_mensal["limite"]:
        return "Limite mensal atingido"

    restante = stock_maximo_mensal["limite"] - total
    return f"Ainda pode aceitar {restante} encomendas"


def adicionar_ingrediente(nome):
    if nome in lista_compras:
        return "Ingrediente já existe na lista"

    lista_compras.append(nome)
    return "Ingrediente adicionado à lista de compras"


def remover_ingrediente(nome):
    if nome not in lista_compras:
        return "Ingrediente não encontrado"

    lista_compras.remove(nome)
    return "Ingrediente removido da lista de compras"


def ver_lista_compras():
    return lista_compras


def atualizar_rede_social(nome, link):
    rede_social[nome] = link
    return "Rede social atualizada com sucesso"


def ver_rede_social():
    return rede_social