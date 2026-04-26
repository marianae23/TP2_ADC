Sistema de Gestão de Doceria
============================

Descrição
=========

O **Sistema de Gestão de Doceria** é uma aplicação desenvolvida em Python para gestão de produtos, encomendas e operações administrativas de uma doceria.

O sistema permite a separação de funcionalidades entre clientes e administradores, facilitando o processo de compra, personalização de encomendas, gestão de stock, promoções e controlo interno.

Objetivos do Projeto
====================

- Organizar catálogo de produtos
- Permitir encomendas normais e personalizadas
- Gerir stock de produtos
- Gerir promoções
- Permitir avaliações de clientes
- Controlar datas disponíveis para encomendas
- Melhorar organização administrativa

Funcionalidades do Cliente
==========================

- Visualizar catálogo de produtos
- Procurar produtos por nome
- Filtrar produtos por categoria
- Filtrar produtos por sabor
- Filtrar produtos por tamanho
- Filtrar produtos por cor
- Fazer encomendas
- Cancelar encomendas
- Consultar estado da encomenda
- Consultar tempo estimado de entrega
- Avaliar produtos
- Consultar avaliações
- Consultar produto do dia

Funcionalidades do Administrador
================================

- Visualizar produtos
- Verificar stock
- Adicionar produtos
- Remover produtos
- Alterar preços
- Gerir promoções
- Alterar estado de encomendas
- Consultar checkout
- Consultar histórico de compras
- Bloquear datas
- Gerir lista de compras
- Gerir métodos de pagamento
- Gerir redes sociais
- Definir stock máximo mensal

Estrutura do Projeto
====================

.. code-block:: text

   SistemaDoceria/
   │── admin.py
   │── dados.py
   │── encomendas.py
   │── produtos.py
   │── user.py
   │── main.py
   │── testes.py
   │── README.md
   │── docs/

Estrutura dos Módulos
=====================

dados.py
--------

Módulo responsável pelo armazenamento central de dados do sistema em memória.

Contém:

- catálogo de produtos
- encomendas registadas
- métodos de pagamento
- métodos de envio
- estados de encomenda
- datas bloqueadas
- stock máximo mensal
- lista de compras
- redes sociais
- utilizadores

produtos.py
-----------

Módulo responsável pela gestão e manipulação do catálogo de produtos.

Funcionalidades:

- listagem de produtos
- pesquisa por ID
- pesquisa por nome
- filtros por categoria
- filtros por sabor
- filtros por tamanho
- filtros por cor
- filtros por preço
- filtros por intolerâncias
- gestão de promoções
- cálculo de preço final
- sistema de avaliações
- cálculo de média de avaliações
- recomendação de produtos
- resumo detalhado de produtos

encomendas.py
-------------

Módulo responsável pela gestão das encomendas.

Funcionalidades:

- listar encomendas
- procurar encomendas
- criar encomendas
- cancelar encomendas
- alterar data de entrega
- validar stock
- validar datas disponíveis
- validar limite mensal
- calcular total
- estimar tempo de espera
- gerar resumo de encomenda
- emitir alerta de atraso

user.py
-------

Módulo responsável pelas operações do cliente.

Funcionalidades:

- fazer pedidos
- adicionar comentários
- consultar pedidos
- consultar estado do pedido
- listar produtos disponíveis

admin.py
--------

Módulo responsável pelas operações administrativas.

Funcionalidades:

- gestão de produtos
- gestão de stock
- gestão de promoções
- gestão de métodos de pagamento
- gestão de datas bloqueadas
- gestão de encomendas
- gestão de histórico de clientes
- gestão de lista de compras
- gestão de redes sociais
- controlo de stock máximo mensal

main.py
-------

Módulo principal do sistema.

Responsável por:

- iniciar aplicação
- apresentar menus
- separar acesso cliente e administrador
- recolher dados do utilizador
- chamar operações do sistema

testes.py
---------

Módulo de testes automatizados com Pytest.

Testes implementados:

- listagem de produtos
- pesquisa de produtos
- filtros
- promoções
- avaliações
- criação de encomendas
- cancelamento de encomendas
- alteração de estados
- alteração de preços
- bloqueio de datas

Tecnologias Utilizadas
======================

- Python 3
- Git
- GitHub
- Sphinx
- Pytest

Instalação
==========

Clonar repositório
------------------

.. code-block:: bash

   git clone <url-do-repositorio>

Entrar no projeto
-----------------

.. code-block:: bash

   cd SistemaDoceria

Execução do Sistema
===================

.. code-block:: bash

   python main.py

ou

.. code-block:: bash

   py main.py

Execução de Testes
==================

Instalar pytest
---------------

.. code-block:: bash

   py -m pip install pytest

Executar testes
---------------

.. code-block:: bash

   py -m pytest testes.py

Documentação Técnica com Sphinx
===============================

Instalar Sphinx
---------------

.. code-block:: bash

   py -m pip install sphinx

Gerar documentação
------------------

.. code-block:: bash

   py -m sphinx -b html docs/source docs/build

Abrir documentação
------------------

.. code-block:: text

   docs/build/index.html

Regras de Negócio
=================

Produtos
--------

- Produto sem stock fica indisponível
- Preço deve ser superior a zero

Encomendas
----------

- Devem respeitar datas disponíveis
- Devem respeitar limite mensal de produção
- Quantidade deve ser superior a zero

Cancelamento
------------

- Encomendas entregues não podem ser canceladas
- Encomendas canceladas devolvem stock

Promoções
---------

- Desconto deve estar entre 1% e 99%

Avaliações
----------

- Nota mínima: 1
- Nota máxima: 5

Fluxo do Cliente
================

Entrar no sistema

↓

Escolher modo cliente

↓

Consultar catálogo

↓

Selecionar produto

↓

Criar encomenda

↓

Selecionar envio

↓

Selecionar pagamento

↓

Confirmar pedido

↓

Consultar estado

↓

Avaliar produto

Fluxo do Administrador
======================

Entrar no sistema

↓

Escolher modo administrador

↓

Gerir produtos

↓

Gerir stock

↓

Gerir promoções

↓

Gerir encomendas

↓

Consultar histórico

↓

Controlar operação

Testes Implementados
====================

- Testes unitários
- Testes funcionais
- Validação de regras de negócio
- Validação de estados
- Validação de stock
- Validação de datas bloqueadas

Autores
=======

**Grupo D**