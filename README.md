# Sistema de Gestão de Doceria

## Descrição

O Sistema de Gestão de Doceria é uma aplicação desenvolvida em Python para gerir produtos, encomendas e operações administrativas de uma doceria.

O sistema permite a separação de funcionalidades entre clientes e administradores, facilitando o processo de compra, gestão de encomendas e controlo interno.

---

## Objetivos do Projeto

- Organizar catálogo de produtos
- Permitir encomendas normais e personalizadas
- Gerir stock de produtos
- Gerir promoções
- Permitir avaliações de clientes
- Controlar datas disponíveis para encomendas
- Melhorar organização administrativa

---

## Funcionalidades do Cliente

- Visualizar produtos disponíveis
- Procurar produtos por nome
- Filtrar produtos por categoria
- Filtrar produtos por sabor
- Filtrar produtos por tamanho
- Filtrar produtos por cor
- Fazer encomendas
- Cancelar encomendas
- Consultar estado da encomenda
- Consultar tempo estimado
- Avaliar produtos
- Consultar avaliações

---

## Funcionalidades do Administrador

- Visualizar produtos
- Verificar stock
- Alterar preços
- Remover produtos
- Adicionar produtos
- Gerir promoções
- Alterar estado de encomendas
- Consultar checkout
- Consultar histórico de compras
- Bloquear datas
- Gerir lista de compras
- Gerir redes sociais
- Definir stock máximo mensal

---

## Estrutura do Projeto

```text
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
```

---

## Estrutura dos Módulos

### admin.py

Módulo responsável pela gestão administrativa.

Funções principais:

- gerir produtos
- gerir stock
- gerir promoções
- gerir estados de encomendas
- gerir checkout

---

### dados.py

Módulo responsável pelo armazenamento dos dados do sistema.

Contém:

- produtos
- encomendas
- métodos de pagamento
- métodos de envio
- estados de encomenda
- datas bloqueadas
- stock máximo mensal

---

### encomendas.py

Módulo responsável pela gestão de encomendas.

Funções principais:

- criar encomendas
- cancelar encomendas
- alterar data de entrega
- calcular total

---

### produtos.py

Módulo responsável pela gestão de produtos.

Funções principais:

- listar produtos
- filtrar produtos
- promoções
- avaliações

---

### user.py

Módulo responsável pelas ações do utilizador.

Funções principais:

- fazer pedidos
- comentar encomendas
- consultar pedidos

---

### main.py

Módulo principal.

Responsável pelos menus e interação com o utilizador.

---

## Tecnologias Utilizadas

- Python 3
- Git
- GitHub
- Sphinx
- Pytest

---

## Instalação

### Clonar repositório

```bash
git clone <url-do-repositorio>
```

### Entrar no projeto

```bash
cd nome-do-projeto
```

---

## Execução do Sistema

```bash
python main.py
```

ou

```bash
py main.py
```

---

## Execução de Testes

### Instalar pytest

```bash
py -m pip install pytest
```

### Executar testes

```bash
py -m pytest testes.py
```

---

## Documentação Técnica com Sphinx

### Instalar Sphinx

```bash
py -m pip install sphinx
```

### Gerar documentação

```bash
py -m sphinx -b html source build
```

### Abrir documentação

```text
docs/build/index.html
```

---

## Regras de Negócio

### Produtos

- Produto sem stock fica indisponível
- Preço deve ser superior a zero

### Encomendas

- Devem respeitar datas disponíveis
- Devem respeitar limite mensal

### Cancelamento

- Encomendas entregues não podem ser canceladas
- Encomendas canceladas devolvem stock

### Promoções

- Desconto entre 1% e 99%

### Avaliações

- Nota mínima: 1
- Nota máxima: 5

---

## Fluxo do Cliente

Entrar no sistema

↓

Escolher modo cliente

↓

Visualizar catálogo

↓

Escolher produto

↓

Criar encomenda

↓

Escolher envio

↓

Escolher pagamento

↓

Confirmar pedido

↓

Consultar estado

↓

Avaliar produto

---

## Fluxo do Administrador

Entrar no sistema

↓

Escolher modo administrador

↓

Gerir produtos

↓

Gerir encomendas

↓

Gerir stock

↓

Gerir promoções

↓

Consultar histórico

---

## Testes Implementados

- Listagem de produtos
- Pesquisa de produtos
- Filtros
- Promoções
- Avaliações
- Criação de encomendas
- Cancelamento de encomendas
- Alteração de estado
- Alteração de preço
- Bloqueio de datas

---

## Autores

Grupo D