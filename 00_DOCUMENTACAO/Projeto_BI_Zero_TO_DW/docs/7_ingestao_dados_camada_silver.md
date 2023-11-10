# Projeto BI Zero TO DW

## 7 - Ingestão dos Dados na Camada Silver

|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-7.1 |Função acentuacao|Usada para remover a acentuação de campos do tipo STRING.|
|SEQ-7.2 / SEQ-7.3 / SEQ-7.4 / SEQ-7.5 / SEQ-7.6 / SEQ-7.7 / SEQ-7.8 / SEQ-7.9|Ingestão dos Dados da Camada Bronze para Silver|Carga realizada baseada nos dados existentes nas tabelas da camada Bronze.|
|SEQ-7.2 / SEQ-7.3 / SEQ-7.4 / SEQ-7.5 / SEQ-7.6 / SEQ-7.7 / SEQ-7.8 / SEQ-7.9|Tratamento de dados antes de inserir/atualizar|Remover acentuação e caracteres especiais, valores nulos onde o datatype foi STRING, informar 'N/A', datatype NUMÉRICO, informar 0 (zero) e datatype DATE/TIMESTAMP, informar '1900-01-01'. Todo os dados do tipo STRING devem estar dados em caixa alta.|
|SEQ-7.2 / SEQ-7.3 / SEQ-7.4 / SEQ-7.5 / SEQ-7.6 / SEQ-7.7 / SEQ-7.8 / SEQ-7.9|Identificar a data de alteração ou cadastro|Regra: Caso o registro não exista (caindo na condição INSERT do MERGE), a data de cadastro e data de alteração devem ser a mesma, caso o registro exista, a data de alteração deverá ser alterada.|

O arquivo do Notebook é encontrado aqui. [Notebook Ingestão Dados Para Camada Silver](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/02_NOTEBOOK/03_ingestao_camada_silver.ipynb)

### SEQ-7.1 - Notebook Externo<br>

Nessa etapa é realizada a importação de um notebook externo que contém a função que será usada para realizar o tratamento (remoção da acentuação) dos dados.

``` {.py3 title="Notebook Externo" linenums=1}
%run /estudos/libs/bibliotecas
```

### Atividades de Ingestão


### SEQ-7.2 - Ingestão de Dados na camada "silver" de tb_categoria_produto<br>

``` {.sql title="Carga Silver tb_categoria_produto" linenums=1}
%sql
MERGE INTO silver.tb_categoria_produto a
USING (
SELECT 
CODIGO_CATEGORIA
,IFNULL(TRIM(acentuacao(DECRICAO_CATEGORIA)),'N/A') DECRICAO_CATEGORIA
FROM bronze.tb_categoria_produto
) b

ON a.CODIGO_CATEGORIA= b.CODIGO_CATEGORIA

WHEN MATCHED THEN
UPDATE SET 
a.DECRICAO_CATEGORIA = b.DECRICAO_CATEGORIA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_CATEGORIA
,DECRICAO_CATEGORIA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.CODIGO_CATEGORIA
,b.DECRICAO_CATEGORIA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.3 - Ingestão de Dados na camada "silver" de tb_cliente <br>

``` {.sql title="Carga Silver tb_cliente" linenums=1}
%sql
MERGE INTO silver.tb_cliente a
USING (
SELECT 
CODIGO_CLIENTE
,IFNULL(TRIM(acentuacao(NOME_CLIENTE)),'N/A') NOME_CLIENTE
FROM bronze.tb_cliente
) b

ON a.CODIGO_CLIENTE= b.CODIGO_CLIENTE

WHEN MATCHED THEN
UPDATE SET 
a.NOME_CLIENTE = b.NOME_CLIENTE
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_CLIENTE
,NOME_CLIENTE
,DATA_CADASTRO
,DATA_ALTERACAO
)
VALUES 
(
b.CODIGO_CLIENTE
,b.NOME_CLIENTE
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.4 - Ingestão de Dados na camada "silver" de tb_forma_pagamento<br>

``` {.sql title="Carga Silver tb_forma_pagamento" linenums=1}
%sql
MERGE INTO silver.tb_forma_pagamento a
USING (
SELECT 
CODIGO_FORMA_PAGAMENTO
,IFNULL(TRIM(acentuacao(DESCRICAO_FORMA_PAGAMENTO)),'N/A') DESCRICAO_FORMA_PAGAMENTO
FROM bronze.tb_forma_pagamento
) b

ON a.CODIGO_FORMA_PAGAMENTO= b.CODIGO_FORMA_PAGAMENTO

WHEN MATCHED THEN
UPDATE SET 
a.DESCRICAO_FORMA_PAGAMENTO = b.DESCRICAO_FORMA_PAGAMENTO
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(CODIGO_FORMA_PAGAMENTO
,DESCRICAO_FORMA_PAGAMENTO
,DATA_CADASTRO
,DATA_ALTERACAO) 
VALUES 
(b.CODIGO_FORMA_PAGAMENTO
,b.DESCRICAO_FORMA_PAGAMENTO
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.5 - Ingestão de Dados na camada "silver" de tb_item_venda<br>

``` {.sql title="Carga Silver tb_item_venda" linenums=1}
%sql
MERGE INTO silver.tb_item_venda a
USING (
SELECT 
CODIGO_VENDA
,CODIGO_PRODUTO
,VALOR_UNITARIO
,QUANTIDADE
,VALOR_FINAL
FROM bronze.tb_item_venda
) b

ON a.CODIGO_VENDA= b.CODIGO_VENDA
AND a.CODIGO_PRODUTO= b.CODIGO_PRODUTO

WHEN MATCHED THEN
UPDATE SET 
a.VALOR_UNITARIO = b.VALOR_UNITARIO
,a.QUANTIDADE = b.QUANTIDADE
,a.VALOR_FINAL = b.VALOR_FINAL
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_VENDA
,CODIGO_PRODUTO
,VALOR_UNITARIO
,QUANTIDADE
,VALOR_FINAL
,DATA_CADASTRO
,DATA_ALTERACAO
)
VALUES 
(
b.CODIGO_VENDA
,b.CODIGO_PRODUTO
,b.VALOR_UNITARIO
,b.QUANTIDADE
,b.VALOR_FINAL
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)

```

### SEQ-7.6 - Ingestão de Dados na camada "silver" de tb_loja<br>

``` {.sql title="Carga Silver tb_loja" linenums=1}
%sql
MERGE INTO silver.tb_loja a
USING (
SELECT 
CODIGO_LOJA
,IFNULL(TRIM(acentuacao(NOME_LOJA)),'N/A') NOME_LOJA
,IFNULL(TRIM(acentuacao(LOCALIDADE_LOJA)),'N/A') LOCALIDADE_LOJA
,IFNULL(TRIM(TIPO_LOJA),'N/A') TIPO_LOJA
FROM bronze.tb_loja
) b

ON a.CODIGO_LOJA= b.CODIGO_LOJA

WHEN MATCHED THEN
UPDATE SET 
a.NOME_LOJA = b.NOME_LOJA
,a.LOCALIDADE_LOJA = b.LOCALIDADE_LOJA
,a.TIPO_LOJA = b.TIPO_LOJA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT (
CODIGO_LOJA
,NOME_LOJA
,LOCALIDADE_LOJA
,TIPO_LOJA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(b.CODIGO_LOJA
,b.NOME_LOJA
,b.LOCALIDADE_LOJA
,b.TIPO_LOJA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.7 - Ingestão de Dados na camada "silver" de tb_produto<br>

``` {.sql title="Carga Silver tb_produto" linenums=1}
%sql

MERGE INTO silver.tb_produto a
USING (SELECT 
PROD.CODIGO_PRODUTO
,IFNULL(TRIM(acentuacao(PROD.DESCRICAO_PRODUTO)),'N/A') DESCRICAO_PRODUTO
,IFNULL(TRIM(PROD.CODIGO_CATEGORIA),'N/A') CODIGO_CATEGORIA
FROM bronze.tb_produto PROD) b

ON a.CODIGO_PRODUTO= b.CODIGO_PRODUTO

WHEN MATCHED 
THEN
UPDATE SET 
a.DESCRICAO_PRODUTO = b.DESCRICAO_PRODUTO
,a.CODIGO_CATEGORIA = b.CODIGO_CATEGORIA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_PRODUTO
,DESCRICAO_PRODUTO
,CODIGO_CATEGORIA
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.CODIGO_PRODUTO
,b.DESCRICAO_PRODUTO
,b.CODIGO_CATEGORIA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.8 - Ingestão de Dados na camada "silver" de tb_venda<br>

``` {.sql title="Carga Silver tb_venda" linenums=1}
%sql

MERGE INTO silver.tb_venda a
USING (
SELECT 
CODIGO_VENDA
,DATA_VENDA
,CODIGO_CLIENTE
,CODIGO_VENDEDOR
,CODIGO_LOJA
,VALOR_FINAL
,IFNULL(TRIM(FORMA_PAGAMENTO),'N/A') FORMA_PAGAMENTO
,IFNULL(TRIM(TIPO_PAGAMENTO),'N/A') TIPO_PAGAMENTO
FROM bronze.tb_venda
) b

ON a.CODIGO_VENDA= b.CODIGO_VENDA

WHEN MATCHED THEN
UPDATE SET 
a.DATA_VENDA = b.DATA_VENDA
,a.CODIGO_CLIENTE = b.CODIGO_CLIENTE
,a.CODIGO_VENDEDOR = b.CODIGO_VENDEDOR
,a.CODIGO_LOJA = b.CODIGO_LOJA
,a.VALOR_FINAL = b.VALOR_FINAL
,a.FORMA_PAGAMENTO = b.FORMA_PAGAMENTO
,a.TIPO_PAGAMENTO = b.TIPO_PAGAMENTO
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_VENDA
,DATA_VENDA
,CODIGO_CLIENTE
,CODIGO_VENDEDOR
,CODIGO_LOJA
,VALOR_FINAL
,FORMA_PAGAMENTO
,TIPO_PAGAMENTO
,DATA_CADASTRO
,DATA_ALTERACAO
)
VALUES (
b.CODIGO_VENDA
,b.DATA_VENDA
,b.CODIGO_CLIENTE
,b.CODIGO_VENDEDOR
,b.CODIGO_LOJA
,b.VALOR_FINAL
,b.FORMA_PAGAMENTO
,b.TIPO_PAGAMENTO
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-7.9 - Ingestão de Dados na camada "silver" de tb_vendedor<br>

``` {.sql title="Carga Silver tb_vendedor" linenums=1}
%sql

MERGE INTO silver.tb_vendedor a
USING (
SELECT 
CODIGO_VENDEDOR
,IFNULL(TRIM(acentuacao(NOME_VENDEDOR)),'N/A') NOME_VENDEDOR
FROM bronze.tb_vendedor
) b

ON a.CODIGO_VENDEDOR= b.CODIGO_VENDEDOR

WHEN MATCHED THEN
UPDATE SET 
a.NOME_VENDEDOR = b.NOME_VENDEDOR
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_VENDEDOR
,NOME_VENDEDOR
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.CODIGO_VENDEDOR
,b.NOME_VENDEDOR
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```