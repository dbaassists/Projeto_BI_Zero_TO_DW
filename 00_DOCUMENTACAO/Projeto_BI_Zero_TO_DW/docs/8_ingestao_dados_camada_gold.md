# Projeto BI Zero TO DW

## 8 - Ingestão dos Dados na Camada Gold

|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6 |Ingestão dos Dados da Camada Silver para Gold|Carga realizada baseada nos dados existentes nas tabelas da camada Silver.|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6 |Identificar a data de alteração ou cadastro|Regra: Caso o registro não exista (caindo na condição INSERT do MERGE), a data de cadastro e data de alteração devem ser a mesma, caso o registro exista, a data de alteração deverá ser alterada.|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6 |Criação da PK usando o Algoritmo HASH(256)|Regra: Usar a PK da tabela na camada Silver e encriptar usando HASH(256).|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6 |SCD Tipos|Não estaremos aplicando nenhuma forma de versionamento dos dados na camada dimensional.|

O arquivo do Notebook é encontrado aqui. [Notebook Ingestão Dados Para Camada Gold](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/02_NOTEBOOK/04_ingestao_camada_gold.ipynb)


### SEQ-8.1 - Carga Tabela Camada Gold - dim_categoria_produto

```
%sql
MERGE INTO gold.DIM_CATEGORIA_PRODUTO a
USING (
SELECT 
hash(CODIGO_CATEGORIA, 256) ID_CATEGORIA_PRODUTO
,CODIGO_CATEGORIA
,acentuacao(DECRICAO_CATEGORIA) DECRICAO_CATEGORIA
FROM silver.tb_categoria_produto
) b

ON a.ID_CATEGORIA_PRODUTO= b.ID_CATEGORIA_PRODUTO

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_CATEGORIA = b.CODIGO_CATEGORIA
,a.DECRICAO_CATEGORIA = b.DECRICAO_CATEGORIA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_CATEGORIA_PRODUTO
,CODIGO_CATEGORIA
,DECRICAO_CATEGORIA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.ID_CATEGORIA_PRODUTO
,b.CODIGO_CATEGORIA
,b.DECRICAO_CATEGORIA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-8.2 - Carga Tabela Camada Gold - dim_cliente

```
%sql
MERGE INTO gold.DIM_CLIENTE a
USING (
SELECT 
hash(CODIGO_CLIENTE, 256) ID_CLIENTE
,CODIGO_CLIENTE
,acentuacao(NOME_CLIENTE) NOME_CLIENTE
FROM silver.tb_cliente
) b

ON a.ID_CLIENTE= b.ID_CLIENTE

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_CLIENTE = b.CODIGO_CLIENTE
,a.NOME_CLIENTE = b.NOME_CLIENTE
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_CLIENTE
,CODIGO_CLIENTE
,NOME_CLIENTE
,DATA_CADASTRO
,DATA_ALTERACAO
)
VALUES 
(
b.ID_CLIENTE
,b.CODIGO_CLIENTE
,b.NOME_CLIENTE
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)

```

### SEQ-8.3 - Carga Tabela Camada Gold - dim_forma_pagamento

```
%sql
MERGE INTO gold.DIM_FORMA_PAGAMENTO a
USING (
SELECT 
hash(CODIGO_FORMA_PAGAMENTO, 256) ID_FORMA_PAGAMENTO
,CODIGO_FORMA_PAGAMENTO
,DESCRICAO_FORMA_PAGAMENTO DESCRICAO_FORMA_PAGAMENTO
FROM silver.tb_forma_pagamento
) b

ON a.ID_FORMA_PAGAMENTO= b.ID_FORMA_PAGAMENTO

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_FORMA_PAGAMENTO = b.CODIGO_FORMA_PAGAMENTO
,a.DESCRICAO_FORMA_PAGAMENTO = b.DESCRICAO_FORMA_PAGAMENTO
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_FORMA_PAGAMENTO  
,CODIGO_FORMA_PAGAMENTO
,DESCRICAO_FORMA_PAGAMENTO
,DATA_CADASTRO
,DATA_ALTERACAO) 
VALUES 
(
b.ID_FORMA_PAGAMENTO
,b.CODIGO_FORMA_PAGAMENTO
,b.DESCRICAO_FORMA_PAGAMENTO
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)

```

### SEQ-8.4 - Carga Tabela Camada Gold - dim_loja

```
%sql
MERGE INTO gold.DIM_LOJA a
USING (
SELECT 
hash(CODIGO_LOJA, 256) ID_LOJA
,CODIGO_LOJA
,acentuacao(NOME_LOJA) NOME_LOJA
,acentuacao(LOCALIDADE_LOJA) LOCALIDADE_LOJA
,TIPO_LOJA
FROM silver.tb_loja
) b

ON a.ID_LOJA= b.ID_LOJA

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_LOJA = b.CODIGO_LOJA
,a.NOME_LOJA = b.NOME_LOJA
,a.LOCALIDADE_LOJA = b.LOCALIDADE_LOJA
,a.TIPO_LOJA = b.TIPO_LOJA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT (
ID_LOJA
,CODIGO_LOJA
,NOME_LOJA
,LOCALIDADE_LOJA
,TIPO_LOJA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.ID_LOJA
,b.CODIGO_LOJA
,b.NOME_LOJA
,b.LOCALIDADE_LOJA
,b.TIPO_LOJA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)

```

### SEQ-8.5 - Carga Tabela Camada Gold - dim_produto

```
%sql

MERGE INTO gold.DIM_PRODUTO a
USING (SELECT 
hash(CODIGO_PRODUTO, 256) ID_PRODUTO
,PROD.CODIGO_PRODUTO
,PROD.DESCRICAO_PRODUTO DESCRICAO_PRODUTO
,PROD.CODIGO_CATEGORIA
FROM silver.tb_produto PROD) b

ON a.ID_PRODUTO= b.ID_PRODUTO

WHEN MATCHED 
THEN
UPDATE SET 
a.CODIGO_PRODUTO = b.CODIGO_PRODUTO
,a.DESCRICAO_PRODUTO = b.DESCRICAO_PRODUTO
,a.CODIGO_CATEGORIA = b.CODIGO_CATEGORIA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_PRODUTO
,CODIGO_PRODUTO
,DESCRICAO_PRODUTO
,CODIGO_CATEGORIA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.ID_PRODUTO
,b.CODIGO_PRODUTO
,b.DESCRICAO_PRODUTO
,b.CODIGO_CATEGORIA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)

```

### SEQ-8.6 - Carga Tabela Camada Gold - dim_vendedor

```
%sql

MERGE INTO gold.DIM_VENDEDOR a
USING (
SELECT 
hash(CODIGO_VENDEDOR, 256) ID_VENDEDOR
,CODIGO_VENDEDOR
,NOME_VENDEDOR NOME_VENDEDOR
FROM silver.tb_vendedor
) b

ON a.ID_VENDEDOR= b.ID_VENDEDOR

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_VENDEDOR = b.CODIGO_VENDEDOR
,a.NOME_VENDEDOR = b.NOME_VENDEDOR
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_VENDEDOR
,CODIGO_VENDEDOR
,NOME_VENDEDOR
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.ID_VENDEDOR
,b.CODIGO_VENDEDOR
,b.NOME_VENDEDOR
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```
