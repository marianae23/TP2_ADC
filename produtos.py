import random

from dados import produtos


def listar_produtos():
    return produtos


def listar_produtos_disponiveis():
    return [
        produto for produto in produtos
        if produto["disponivel"] and produto["stock"] > 0
    ]


def procurar_produto_por_id(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto

    return "Produto não encontrado"


def procurar_por_nome(nome):
    return [
        produto for produto in produtos
        if nome.lower() in produto["nome"].lower()
    ]


def filtrar_por_categoria(categoria):
    return [
        produto for produto in produtos
        if produto["categoria"].lower() == categoria.lower()
    ]


def filtrar_por_sabor(sabor):
    return [
        produto for produto in produtos
        if sabor.lower() in [s.lower() for s in produto["sabores"]]
    ]


def filtrar_por_cor(cor):
    return [
        produto for produto in produtos
        if cor.lower() in [c.lower() for c in produto["cores"]]
    ]


def filtrar_por_preco(preco_maximo):
    if preco_maximo <= 0:
        return "Preço inválido"

    return [
        produto for produto in produtos
        if produto["preco"] <= preco_maximo
    ]


def filtrar_sem_intolerancia(intolerancia):
    return [
        produto for produto in produtos
        if intolerancia.lower()
        not in [i.lower() for i in produto["intolerancias"]]
    ]


def listar_produtos_novos():
    return [
        produto for produto in produtos
        if produto["novo"]
    ]


def listar_produtos_em_promocao():
    return [
        produto for produto in produtos
        if produto["promocao"] is not None
    ]


def produtos_stock_baixo(limite=5):
    return [
        produto for produto in produtos
        if produto["stock"] <= limite
    ]


def aplicar_promocao(id_produto, desconto):
    if desconto <= 0 or desconto > 100:
        return "Desconto inválido"

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["promocao"] = desconto
            return "Promoção aplicada com sucesso"

    return "Produto não encontrado"


def remover_promocao(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["promocao"] = None
            return "Promoção removida com sucesso"

    return "Produto não encontrado"


def calcular_preco_final(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            preco = produto["preco"]
            promocao = produto["promocao"]

            if promocao is not None:
                preco -= preco * (promocao / 100)

            return round(preco, 2)

    return "Produto não encontrado"


def avaliar_produto(id_produto, avaliacao):
    if avaliacao < 1 or avaliacao > 5:
        return "Avaliação inválida"

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["avaliacoes"].append(avaliacao)
            return "Avaliação adicionada com sucesso"

    return "Produto não encontrado"


def media_avaliacoes(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            if not produto["avaliacoes"]:
                return "Sem avaliações"

            media = sum(produto["avaliacoes"]) / len(produto["avaliacoes"])
            return round(media, 2)

    return "Produto não encontrado"


def produto_mais_bem_avaliado():
    melhor_produto = None
    melhor_media = 0

    for produto in produtos:
        if produto["avaliacoes"]:
            media = sum(produto["avaliacoes"]) / len(produto["avaliacoes"])

            if media > melhor_media:
                melhor_media = media
                melhor_produto = produto

    if melhor_produto is None:
        return "Sem avaliações"

    return melhor_produto


def recomendar_produto():
    disponiveis = listar_produtos_disponiveis()

    if not disponiveis:
        return "Sem produtos disponíveis"

    return random.choice(disponiveis)


def produto_do_dia():
    if not produtos:
        return "Não existem produtos"

    return random.choice(produtos)


def resumo_produto(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            preco_final = calcular_preco_final(id_produto)

            return {
                "nome": produto["nome"],
                "categoria": produto["categoria"],
                "preco_original": produto["preco"],
                "preco_final": preco_final,
                "stock": produto["stock"],
                "disponivel": produto["disponivel"],
                "novo": produto["novo"],
                "promocao": produto["promocao"],
                "media_avaliacoes": media_avaliacoes(id_produto)
            }

    return "Produto não encontrado"