import copy

import admin
import encomendas
import produtos

from dados import (
    datas_bloqueadas,
    encomendas as lista_encomendas,
    produtos as lista_produtos,
    stock_maximo_mensal
)


produtos_originais = copy.deepcopy(lista_produtos)
encomendas_originais = copy.deepcopy(lista_encomendas)


def restaurar_dados():
    lista_produtos.clear()
    lista_produtos.extend(copy.deepcopy(produtos_originais))

    lista_encomendas.clear()
    lista_encomendas.extend(copy.deepcopy(encomendas_originais))

    datas_bloqueadas.clear()
    stock_maximo_mensal["limite"] = 50


def test_listar_produtos():
    restaurar_dados()

    resultado = produtos.listar_produtos()

    assert isinstance(resultado, list)
    assert len(resultado) > 0


def test_procurar_produto_por_id_existente():
    restaurar_dados()

    resultado = produtos.procurar_produto_por_id(1)

    assert isinstance(resultado, dict)
    assert resultado["id"] == 1
    assert resultado["nome"] == "Bolo de Chocolate"


def test_procurar_produto_por_id_inexistente():
    restaurar_dados()

    resultado = produtos.procurar_produto_por_id(999)

    assert resultado == "Produto não encontrado"


def test_filtrar_por_categoria():
    restaurar_dados()

    resultado = produtos.filtrar_por_categoria("bolo")

    assert isinstance(resultado, list)
    assert len(resultado) > 0
    assert all(produto["categoria"] == "bolo" for produto in resultado)


def test_calcular_preco_final_sem_promocao():
    restaurar_dados()

    resultado = produtos.calcular_preco_final(1)

    assert resultado == 25.0


def test_aplicar_promocao():
    restaurar_dados()

    resultado = produtos.aplicar_promocao(
        1,
        20,
        "2026-05-01",
        "2026-05-31"
    )

    preco_final = produtos.calcular_preco_final(1)

    assert resultado == "Promoção aplicada com sucesso"
    assert preco_final == 20.0


def test_avaliar_produto():
    restaurar_dados()

    resultado = produtos.avaliar_produto(1, 5, "Muito bom!")

    assert resultado == "Avaliação adicionada com sucesso"
    assert produtos.media_avaliacoes(1) == 5.0


def test_criar_encomenda():
    restaurar_dados()

    primeiro_produto = lista_produtos[0]
    assert isinstance(primeiro_produto, dict)

    stock_inicial = primeiro_produto["stock"]

    resultado = encomendas.criar_encomenda(
        cliente_nome="Ana",
        email="ana@email.com",
        telefone="912345678",
        tipo="produto existente",
        produto_id=1,
        quantidade=2,
        metodo_envio="Entrega",
        metodo_pagamento="MB WAY",
        morada="Rua Teste",
        data_desejada="2026-05-10"
    )

    ultima_encomenda = lista_encomendas[-1]
    assert isinstance(ultima_encomenda, dict)

    assert resultado == "Encomenda criada com sucesso"
    assert primeiro_produto["stock"] == stock_inicial - 2
    assert ultima_encomenda["cliente_nome"] == "Ana"


def test_criar_encomenda_stock_insuficiente():
    restaurar_dados()

    resultado = encomendas.criar_encomenda(
        cliente_nome="Ana",
        email="ana@email.com",
        telefone="912345678",
        tipo="produto existente",
        produto_id=1,
        quantidade=999,
        metodo_envio="Entrega",
        metodo_pagamento="MB WAY",
        morada="Rua Teste",
        data_desejada="2026-05-10"
    )

    assert resultado == "Stock insuficiente"


def test_cancelar_encomenda():
    restaurar_dados()

    encomendas.criar_encomenda(
        cliente_nome="Ana",
        email="ana@email.com",
        telefone="912345678",
        tipo="produto existente",
        produto_id=1,
        quantidade=1,
        metodo_envio="Entrega",
        metodo_pagamento="MB WAY",
        morada="Rua Teste",
        data_desejada="2026-05-10"
    )

    ultima_encomenda = lista_encomendas[-1]
    assert isinstance(ultima_encomenda, dict)

    id_encomenda = ultima_encomenda["id"]
    resultado = encomendas.cancelar_encomenda(id_encomenda)

    assert resultado == "Encomenda cancelada com sucesso"
    assert ultima_encomenda["estado"] == "Cancelada"


def test_alterar_estado_encomenda():
    restaurar_dados()

    primeira_encomenda = lista_encomendas[0]
    assert isinstance(primeira_encomenda, dict)

    resultado = admin.alterar_estado_encomenda(1, "Em preparação")

    assert resultado == "Estado da encomenda alterado com sucesso"
    assert primeira_encomenda["estado"] == "Em preparação"


def test_alterar_estado_invalido():
    restaurar_dados()

    resultado = admin.alterar_estado_encomenda(1, "Estado errado")

    assert resultado == "Estado inválido"


def test_alterar_preco_produto():
    restaurar_dados()

    primeiro_produto = lista_produtos[0]
    assert isinstance(primeiro_produto, dict)

    resultado = admin.alterar_precos(1, 35.0)

    assert resultado == (
        'Preço do produto "Bolo de Chocolate" atualizado para €35.0'
    )
    assert primeiro_produto["preco"] == 35.0


def test_remover_produto():
    restaurar_dados()

    primeiro_produto = lista_produtos[0]
    assert isinstance(primeiro_produto, dict)

    resultado = admin.remover_produto(1)

    assert resultado == 'Produto "Bolo de Chocolate" marcado como indisponível.'
    assert primeiro_produto["disponivel"] is False


def test_bloquear_data():
    restaurar_dados()

    resultado = admin.bloquear_data("2026-05-20")

    assert resultado == "Data bloqueada com sucesso"
    assert "2026-05-20" in datas_bloqueadas


def test_criar_encomenda_data_bloqueada():
    restaurar_dados()

    admin.bloquear_data("2026-05-20")

    resultado = encomendas.criar_encomenda(
        cliente_nome="Ana",
        email="ana@email.com",
        telefone="912345678",
        tipo="produto existente",
        produto_id=1,
        quantidade=1,
        metodo_envio="Entrega",
        metodo_pagamento="MB WAY",
        morada="Rua Teste",
        data_desejada="2026-05-20"
    )

    assert resultado == "Data indisponível para encomendas"