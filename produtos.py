from dados import produtos


def listar_produtos():
    return produtos


def procurar_produto_por_id(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto
    return "Produto não encontrado"


def filtrar_por_categoria(categoria):
    resultado = []

    for produto in produtos:
        if produto["categoria"].lower() == categoria.lower():
            resultado.append(produto)

    return resultado


def listar_produtos_novos():
    return [produto for produto in produtos if produto["novo"]]


def listar_produtos_em_promocao():
    return [produto for produto in produtos if produto["promocao"] is not None]


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