# Projeto BI Zero TO DW

## 8 - Ingestão dos Dados na Camada Gold

|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6|Ingestão dos Dados da Camada Silver para Gold|Carga realizada baseada nos dados existentes nas tabelas da camada Silver.|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6|Identificar a data de alteração ou cadastro|Regra: Caso o registro não exista (caindo na condição INSERT do MERGE), a data de cadastro e data de alteração devem ser a mesma, caso o registro exista, a data de alteração deverá ser alterada.|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6|Criação da PK usando o Algoritmo HASH(256)|Regra: Usar a PK da tabela na camada Silver e encriptar usando HASH(256).|
|SEQ-8.1 / SEQ-8.2 / SEQ-8.3 / SEQ-8.4 / SEQ-8.5 / SEQ-8.6|SCD Tipos|Não estaremos aplicando nenhuma forma de versionamento dos dados na camada dimensional.|

O arquivo do Notebook é encontrado aqui. [Notebook Ingestão Dados Para Camada Gold](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/02_NOTEBOOK/04_ingestao_camada_gold.ipynb)


### SEQ-8.1 - Carga Tabela Camada Gold - dim_cliente

``` {.sql title="Carga Gold gold.dim_cliente" linenums=1}
%sql
MERGE INTO gold.DIM_CLIENTE a
USING (
SELECT 
hash(CODIGO_CLIENTE, 256) ID_CLIENTE
,CODIGO_CLIENTE
,acentuacao(NOME_CLIENTE) NOME_CLIENTE
,DATA_NASCIMENTO
,IDADE_CLIENTE
,acentuacao(DESCRICAO_ENDERECO) DESCRICAO_ENDERECO
,NUMERO_ENDERECO
,acentuacao(NOME_CIDADE) NOME_CIDADE
,NUMERO_TELEFONE
,EMAIL_CLIENTE
,acentuacao(OCUPACAO_CLIENTE) OCUPACAO_CLIENTE
FROM silver.tb_cliente
) b

ON a.ID_CLIENTE= b.ID_CLIENTE

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_CLIENTE = b.CODIGO_CLIENTE
,a.NOME_CLIENTE = b.NOME_CLIENTE
,a.DATA_NASCIMENTO = b.DATA_NASCIMENTO
,a.IDADE_CLIENTE = b.IDADE_CLIENTE
,a.DESCRICAO_ENDERECO = b.DESCRICAO_ENDERECO
,a.NUMERO_ENDERECO = b.NUMERO_ENDERECO
,a.NOME_CIDADE = b.NOME_CIDADE
,a.NUMERO_TELEFONE = b.NUMERO_TELEFONE
,a.EMAIL_CLIENTE = b.EMAIL_CLIENTE
,a.OCUPACAO_CLIENTE = b.OCUPACAO_CLIENTE
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_CLIENTE
,CODIGO_CLIENTE
,NOME_CLIENTE
,DATA_NASCIMENTO
,IDADE_CLIENTE
,DESCRICAO_ENDERECO
,NUMERO_ENDERECO
,NOME_CIDADE
,NUMERO_TELEFONE
,EMAIL_CLIENTE
,OCUPACAO_CLIENTE
,DATA_CADASTRO
,DATA_ALTERACAO
)
VALUES 
(
b.ID_CLIENTE
,b.CODIGO_CLIENTE
,b.NOME_CLIENTE
,b.DATA_NASCIMENTO
,b.IDADE_CLIENTE
,b.DESCRICAO_ENDERECO
,b.NUMERO_ENDERECO
,b.NOME_CIDADE
,b.NUMERO_TELEFONE
,b.EMAIL_CLIENTE
,b.OCUPACAO_CLIENTE
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-8.2 - Carga Tabela Camada Gold - dim_forma_pagamento

```  {.sql title="Carga Gold gold.dim_forma_pagamento" linenums=1}
%sql
MERGE INTO gold.DIM_FORMA_PAGAMENTO a
USING (
SELECT 
hash(CODIGO_FORMA_PAGAMENTO, 256) ID_FORMA_PAGAMENTO
,CODIGO_FORMA_PAGAMENTO
,acentuacao(DESCRICAO_FORMA_PAGAMENTO) DESCRICAO_FORMA_PAGAMENTO
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

### SEQ-8.3 - Carga Tabela Camada Gold - dim_loja

```  {.sql title="Carga Gold gold.dim_loja" linenums=1}
%sql
MERGE INTO gold.DIM_LOJA a
USING (
SELECT 
hash(LOJA.CODIGO_LOJA_VENDEDOR, 256) ID_LOJA
,LOJA.CODIGO_LOJA
,acentuacao(LOJA.NOME_LOJA) NOME_LOJA
,acentuacao(VENDEDOR.NOME_VENDEDOR) NOME_VENDEDOR
,acentuacao(LOJA.LOCALIDADE_LOJA) LOCALIDADE_LOJA
,LOJA.TIPO_LOJA
FROM silver.tb_loja LOJA

INNER JOIN silver.tb_vendedor VENDEDOR

ON LOJA.CODIGO_VENDEDOR = VENDEDOR.CODIGO_VENDEDOR


) b

ON a.ID_LOJA= b.ID_LOJA

WHEN MATCHED THEN
UPDATE SET 
a.CODIGO_LOJA = b.CODIGO_LOJA
,a.NOME_LOJA = b.NOME_LOJA
,a.NOME_VENDEDOR  = b.NOME_VENDEDOR
,a.LOCALIDADE_LOJA = b.LOCALIDADE_LOJA
,a.TIPO_LOJA = b.TIPO_LOJA
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT (
ID_LOJA
,CODIGO_LOJA
,NOME_LOJA
,NOME_VENDEDOR
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
,b.NOME_VENDEDOR
,b.LOCALIDADE_LOJA
,b.TIPO_LOJA
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-8.4 - Carga Tabela Camada Gold - dim_produto

```  {.sql title="Carga Gold gold.dim_produto" linenums=1}
%sql

MERGE INTO gold.DIM_PRODUTO a
USING (SELECT 
hash(PROD.CODIGO_PRODUTO, 256) ID_PRODUTO
,PROD.CODIGO_PRODUTO
,PROD.DESCRICAO_PRODUTO
,CAT_PROD.CATEGORIA_PRODUTO
,CAT_PROD.SUB_CATEGORIA_PRODUTO

FROM silver.tb_produto PROD 

INNER JOIN silver.tb_categoria_produto CAT_PROD

ON PROD.CODIGO_CATEGORIA = CAT_PROD.CODIGO_CATEGORIA
) b

ON a.ID_PRODUTO= b.ID_PRODUTO

WHEN MATCHED 
THEN
UPDATE SET 
a.CODIGO_PRODUTO = b.CODIGO_PRODUTO
,a.DESCRICAO_PRODUTO = b.DESCRICAO_PRODUTO
,a.CATEGORIA_PRODUTO = b.CATEGORIA_PRODUTO
,a.SUB_CATEGORIA_PRODUTO = b.SUB_CATEGORIA_PRODUTO
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
ID_PRODUTO
,CODIGO_PRODUTO
,DESCRICAO_PRODUTO
,CATEGORIA_PRODUTO
,SUB_CATEGORIA_PRODUTO
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.ID_PRODUTO
,b.CODIGO_PRODUTO
,b.DESCRICAO_PRODUTO
,b.CATEGORIA_PRODUTO
,b.SUB_CATEGORIA_PRODUTO
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```

### SEQ-8.5 - Carga Tabela Camada Gold - dim_tempo

A dimensão tempo é carregado no notebook "00_configuracao_ambiente" etapa "SEQ-08 - Insert Tabela GOLD - DIM_TEMPO".


```  {.sql title="Carga Gold gold.dim_tempo" linenums=1}
%sql
diretorio = 'dbfs:/FileStore/tables/landing_zone/tempo/'
tabela = 'tempo'

parDF1=spark.read.parquet(diretorio)

parDF1.createOrReplaceTempView('tmp_dim_tempo')

colunas = parDF1.columns
lista1 = ''
listaInsert = ''
listaCondicao = ''

for coluna in colunas:
    if lista1 == '':
        lista1 = coluna
    else:
        lista1 = lista1 + ',' + coluna

for coluna in colunas:
    if listaInsert == '':
        listaInsert = 'b.'+coluna
    else:
        listaInsert = listaInsert + ',' + 'b.'+ coluna

for coluna in colunas:
    if listaCondicao == '':
        listaCondicao =  'a.'+coluna + '= b.'+coluna

tabela_dl = tabela.replace('dbo.','')

comando_truncate = f"""TRUNCATE TABLE gold.dim_tempo"""

print(comando_truncate)

spark.sql(comando_truncate)

comando_insert = f"""MERGE INTO gold.dim_tempo a
        USING tmp_dim_tempo b
        ON a.ID_TEMPO= b.ID_TEMPO
        WHEN NOT MATCHED
        THEN INSERT (ID_TEMPO
                    ,DATA
                    ,ANO
                    ,MES
                    ,DIA
                    ,DATA_CADASTRO
                    ,DATA_ALTERACAO) 
                    VALUES (
                        hash(b.ID_TEMPO, 256)
                        ,b.DATA
                        ,b.ANO
                        ,b.MES
                        ,b.DIA
                        ,b.DATA_CADASTRO
                        ,b.DATA_ALTERACAO)
        """

print(comando_insert)

spark.sql(comando_insert)


```

### SEQ-8.6 - Carga Tabela Camada Gold - fato_venda

```  {.sql title="Carga Gold gold.fato_venda" linenums=1}
%sql

MERGE INTO gold.fato_venda a
USING (
SELECT  

VENDA.CODIGO_VENDA
,DCLIENTE.ID_CLIENTE
,DLOJA.ID_LOJA
,DPRODUTO.ID_PRODUTO
,DFORMAPAGAMENTO.ID_FORMA_PAGAMENTO
,DTEMPO.ID_TEMPO
,HOUR(VENDA.DATA_VENDA) HORA_VENDA
,IVENDA.QUANTIDADE
,IVENDA.VALOR_UNITARIO
,(IVENDA.QUANTIDADE * IVENDA.VALOR_UNITARIO) VALOR_FINAL
,VENDA.TIPO_PAGAMENTO

FROM silver.tb_venda VENDA

INNER JOIN silver.tb_item_venda IVENDA

ON VENDA.CODIGO_VENDA = IVENDA.CODIGO_VENDA

INNER JOIN silver.tb_loja LOJA

ON VENDA.CODIGO_LOJA_VENDEDOR = LOJA.CODIGO_LOJA_VENDEDOR

INNER JOIN silver.tb_vendedor VENDEDOR

ON LOJA.CODIGO_VENDEDOR = VENDEDOR.CODIGO_VENDEDOR

INNER JOIN gold.dim_tempo DTEMPO

ON REPLACE(TO_DATE(VENDA.DATA_VENDA) ,'-','') = DTEMPO.DATA

INNER JOIN gold.dim_cliente DCLIENTE

ON VENDA.CODIGO_CLIENTE = DCLIENTE.CODIGO_CLIENTE

INNER JOIN gold.dim_loja DLOJA

ON LOJA.CODIGO_LOJA = DLOJA.CODIGO_LOJA

AND VENDEDOR.NOME_VENDEDOR = DLOJA.NOME_VENDEDOR

INNER JOIN gold.dim_produto DPRODUTO

ON IVENDA.CODIGO_PRODUTO = DPRODUTO.CODIGO_PRODUTO

INNER JOIN gold.dim_forma_pagamento DFORMAPAGAMENTO

ON VENDA.CODIGO_FORMA_PAGAMENTO = DFORMAPAGAMENTO.CODIGO_FORMA_PAGAMENTO
) b

ON 

a.CODIGO_VENDA = b.CODIGO_VENDA
AND a.ID_CLIENTE = b.ID_CLIENTE
AND a.ID_LOJA = b.ID_LOJA
AND a.ID_PRODUTO = b.ID_PRODUTO
AND a.ID_FORMA_PAGAMENTO = b.ID_FORMA_PAGAMENTO
AND a.ID_TEMPO = b.ID_TEMPO

WHEN MATCHED 
THEN
UPDATE SET 
a.HORA_VENDA = b.HORA_VENDA
,a.QUANTIDADE = b.QUANTIDADE
,a.VALOR_UNITARIO = b.VALOR_UNITARIO
,a.VALOR_FINAL = b.VALOR_FINAL
,a.TIPO_PAGAMENTO = b.TIPO_PAGAMENTO
,a.DATA_ALTERACAO = from_utc_timestamp(now(),'GMT-3')

WHEN NOT MATCHED
THEN 
INSERT 
(
CODIGO_VENDA
,ID_CLIENTE
,ID_LOJA
,ID_PRODUTO
,ID_FORMA_PAGAMENTO
,ID_TEMPO
,HORA_VENDA
,QUANTIDADE
,VALOR_UNITARIO
,VALOR_FINAL
,TIPO_PAGAMENTO
,DATA_CADASTRO
,DATA_ALTERACAO
) 
VALUES 
(
b.CODIGO_VENDA
,b.ID_CLIENTE
,b.ID_LOJA
,b.ID_PRODUTO
,b.ID_FORMA_PAGAMENTO
,b.ID_TEMPO
,b.HORA_VENDA
,b.QUANTIDADE
,b.VALOR_UNITARIO
,b.VALOR_FINAL
,b.TIPO_PAGAMENTO
,from_utc_timestamp(now(),'GMT-3')
,from_utc_timestamp(now(),'GMT-3')
)
```
