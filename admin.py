from dados import encomendas, produtos, formas_pagamento
def ordenar_por_data ():
    return sorted(encomendas, key=lambda e:e["data_desejada"])

def mostrar_produtos():
    return produtos

def alterar_estado_encomenda(id_encomenda, novo_estado):
    estados_validos = ["Pendente", "Em preparação", "Entregue", "Cancelada"]

    if novo_estado not in estados_validos:
        return "Estado inválido"

    for encomenda in encomendas:
        if encomenda["id"] == id_encomenda:
            encomenda["estado"] = novo_estado
            return "Estado da encomenda alterado com sucesso"

    return "Encomenda não encontrada"
    print(alterar_estado_encomenda(1, "Entregue"))
    print(encomendas[0]["estado"])

def verificar_stock(id_produto):
  for produto in produtos:
        if produto["id"] == id_produto:
            if produto["stock"] > 0 and produto["disponivel"] == True:
                return f'O produto {produto["nome"]} está disponível. Stock: {produto["stock"]}'
            else:
                return f'O produto {produto["nome"]} está indisponível ou sem stock.'
        else:
         return "Produto não encontrado"

def adicionar_produto(nome, categoria, preco, stock, sabores, tamanhos, cores, intolerancias):
    if produtos:
        novo_id = max(p["id"] for p in produtos) + 1
    else:
        novo_id = 1

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
    return f"Produto {nome} adicionado com sucesso!"

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

def mostrar_formas_pagamento():
    return formas_pagamento


def adicionar_forma_pagamento(nova_forma):
    formas_pagamento.append(nova_forma)
    return f'Forma de pagamento "{nova_forma}" adicionada com sucesso.'


def remover_forma_pagamento(forma):
    if forma in formas_pagamento:
        formas_pagamento.remove(forma)
        return f'Forma de pagamento "{forma}" removida com sucesso.'

    return "Forma de pagamento não encontrada."