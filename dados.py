produtos = [
    {
        "id": 1,
        "nome": "Bolo de Chocolate",
        "categoria": "bolo",
        "preco": 25.0,
        "stock": 10,
        "disponivel": True,
        "sabores": ["chocolate"],
        "tamanhos": ["pequeno", "medio", "grande"],
        "cores": ["castanho"],
        "intolerancias": ["sem glúten"],
        "promocao": None,
        "novo": False,
        "avaliacoes": []
    },
    {
        "id": 2,
        "nome": "Cupcake de Morango",
        "categoria": "cupcake",
        "preco": 3.5,
        "stock": 20,
        "disponivel": True,
        "sabores": ["morango"],
        "tamanhos": ["unico"],
        "cores": ["rosa"],
        "intolerancias": [],
        "promocao": None,
        "novo": False,
        "avaliacoes": []
    },
    {
        "id": 3,
        "nome": "Cookies de Chocolate",
        "categoria": "bolacha",
        "preco": 5.0,
        "stock": 30,
        "disponivel": True,
        "sabores": ["chocolate"],
        "tamanhos": ["pack"],
        "cores": ["castanho"],
        "intolerancias": [],
        "promocao": None,
        "novo": False,
        "avaliacoes": []
    },
    {
        "id": 4,
        "nome": "Donut de Chocolate",
        "categoria": "donut",
        "preco": 2.5,
        "stock": 25,
        "disponivel": True,
        "sabores": ["chocolate"],
        "tamanhos": ["unico"],
        "cores": ["castanho"],
        "intolerancias": [],
        "promocao": None,
        "novo": True,
        "avaliacoes": []
    },
    {
        "id": 5,
        "nome": "Bolo Red Velvet",
        "categoria": "bolo",
        "preco": 30.0,
        "stock": 0,
        "disponivel": False,
        "sabores": ["baunilha", "cacao"],
        "tamanhos": ["medio", "grande"],
        "cores": ["vermelho"],
        "intolerancias": [],
        "promocao": None,
        "novo": True,
        "avaliacoes": []
    }
]


encomendas = [
    {
        "id": 1,
        "cliente_nome": "Maria",
        "email": "maria@email.com",
        "telefone": "912345678",
        "tipo": "personalizada",
        "produto_id": 1,
        "personalizacao": {
            "sabor": "baunilha",
            "tamanho": "medio",
            "cor": "rosa"
        },
        "quantidade": 1,
        "metodo_envio": "Entrega",
        "metodo_pagamento": "MB WAY",
        "morada": "Rua X",
        "data_desejada": "2026-04-30",
        "total": 30.0,
        "estado": "Pendente",
        "comentarios": ""
    }
]


metodos_pagamento = [
    "MB WAY",
    "Cartão de crédito",
    "Cartão de débito",
    "PayPal",
    "Transferência bancária",
    "Pagamento na entrega",
    "Multibanco",
    "Dinheiro",
    "Cartão"
]


metodos_envio = [
    "Correio",
    "Entrega",
    "Levantamento",
    "recolha"
]


estados_encomenda = [
    "Pendente",
    "Em preparação",
    "Pronto para recolha",
    "Enviado",
    "Entregue",
    "Cancelada"
]


datas_bloqueadas = []


stock_maximo_mensal = {
    "limite": 50
}


lista_compras = [
    "Farinha",
    "Açúcar",
    "Ovos",
    "Chocolate"
]


rede_social = {
    "instagram": "https://instagram.com/doceria"
}


usuarios = []