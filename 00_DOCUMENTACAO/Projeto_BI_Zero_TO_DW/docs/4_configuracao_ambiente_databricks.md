# Projeto BI Zero TO DW

## 4 - Configurando o Ambiente Databricks

É nessa etapa que é realizada a configuração do ambiente Databricks para ingestão dos dados.

São elas:

|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-4.0|Importação de Bibliotecas|Definição de quais bibliotecas estarão sendo usada|
|SEQ-4.0.1|Importação de Notebook Externo|Será usado para criar a tabela Dimensão Tempo|
|SEQ-4.1|Configuração do ambiente no Databricks|Criação do storage "dbfs:/FileStore/tables/landing_zone"|
|SEQ-4.2 / SEQ-4.3 / SEQ-4.4|Criação de Schemas (Bancos de Dados)|Criação das Camadas Bronze, Silver e Gold |
|SEQ-4.5 / SEQ-4.6 / SEQ-4.7|Criação das Tabelas|Criação das Tabelas das Camadas Bronze, Silver e Gold|
|SEQ-4.8|Criação Script Dimensão Tempo|Geração de Scripts de Insert para a Dimensão Tempo para o mês de Jul/2023|
|SEQ-4.9|Visualizando a Estrutura de uma tabela|Identificando informações de nome da coluna, datatype, nulabilidade, descrição das colunas|
|SEQ-4.10|Visualizando informçoes de armazenamento de uma tabela|Idenficação de quando a tabela foi criada, onde ela é armazenada etc.|
|SEQ-4.11|Visualizando a Estrutura de uma schema|Informações do Schema|

O arquivo do Notebook é encontrado aqui. [Notebook Configuração Ambiente Databricks](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/02_NOTEBOOK/00_configuracao_ambiente.ipynb)

### SEQ-4.0 - Importação de Bibliotecas

``` {.py3 title="Bibliotecas Usadas" linenums=1}
from pyspark.sql.functions import *
from datetime import date, timedelta
```

### SEQ-4.0.1 - Importando Notebook Externo

``` {.py3 title="Notebook Externo" linenums=1}
%run /estudos/libs/bibliotecas
```

### SEQ-4.1 - Criação Camada Landing Zone

Nessa etapa que é realizada a criação de uma área no HDFS do Databricks para salvar em formato parquet os dados exportados do Azure SQL Database.

Nome do Diretório: dbfs:/FileStore/tables/landing_zone

``` {.py3 title="Criação do Diretório no HDFS do Databricks" linenums=1}
diretorio_landing_zone = "dbfs:/FileStore/tables/landing_zone"

try:
    dbutils.fs.ls(diretorio_landing_zone)
    dbutils.fs.rm(diretorio_landing_zone, True)
        
except:

    print(f"O diretório {diretorio_landing_zone} não existe.")

```


``` {.py3 title="Criação do Diretório no HDFS do Databricks" linenums=1}
try:

    dbutils.fs.ls(diretorio_landing_zone)
        
except:

    print(f"O diretório {diretorio_landing_zone} não existe e será criado.")
    dbutils.fs.mkdirs(diretorio_landing_zone)
```
### SEQ-4.2 - Criação Schema de Dados "bronze"

Criação do Schema de Dados "bronze" para armazenamento dos dados ingeridos a partir da leituda dos arquivos de dados exportados do Azure SQL Database.

Trata-se de uma camada transiente, ou seja, é o momento em que os dados são carregados em sua totalidade sem a aplicação de tratamentos. 

Gosto de definir essa etapa como a transposição dos arquivos em tabelas, usando o mesmo nome para criar as tabelas e colunas. 

Nenhum tratamento é aplicado sobre os dados.

As tabelas são TRUNCADAS (limpas) sempre a cada ciclo de carga.

A sintaxe do script de criação de um Schema.

![Image](./imagens/04_create_schema.png)


``` {.sql title="Exclusão do Schema caso exista" linenums=1}
%sql
DROP SCHEMA IF EXISTS bronze CASCADE;
```

``` {.sql title="Criação do Schema" linenums=1}
%sql
CREATE SCHEMA IF NOT EXISTS bronze COMMENT 'SCHEMA (Banco de Dados) referente a Camada BRONZE.';
```

``` {.py3 title="Removendo o location das tabelas no HDFS" linenums=1}
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_forma_pagamento', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_categoria_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_cliente', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_vendedor', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_loja', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_venda', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/bronze.db/tb_item_venda', True);
```

### SEQ-4.3 - Criação Schema de Dados "silver"

Criação do Schema de Dados "silver" para armazenamento dos dados ingeridos da camada bronze.

Nessa camada os dados sofreram transformações (aplicações de regras de negócio) e estarão disponíveis para que seja criada a camada dimensional.

``` {.sql title="Exclusão do Schema caso exista" linenums=1}
%sql
DROP SCHEMA IF EXISTS silver CASCADE;
```
``` {.sql title="Criação do Schema" linenums=1}
%sql
CREATE SCHEMA IF NOT EXISTS silver COMMENT 'SCHEMA (Banco de Dados) referente a Camada SILVER.';
```

``` {.py3 title="Removendo o location das tabelas no HDFS" linenums=1}
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_forma_pagamento', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_categoria_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_cliente', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_vendedor', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_loja', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_venda', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/silver.db/tb_item_venda', True);
```

### SEQ-4.4 - Criação Schema de Dados "gold"

Criação do Schema de Dados "gold" para armazenamento dos dados após a ingestão dos dados na camada silver.

Nessa camada os objetos serão modelados como dimensões e fatos.

``` {.sql title="Exclusão do Schema caso exista" linenums=1}
%sql
DROP SCHEMA IF EXISTS gold CASCADE;
```
``` {.sql title="Criação do Schema" linenums=1}
%sql
CREATE SCHEMA IF NOT EXISTS gold COMMENT 'SCHEMA (Banco de Dados) referente a Camada GOLD.';
```

``` {.py3 title="Removendo o location das tabelas no HDFS" linenums=1}
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_forma_pagamento', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_categoria_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_produto', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_cliente', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_vendedor', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_loja', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/fato_venda', True);
dbutils.fs.rm('dbfs:/user/hive/warehouse/gold.db/dim_tempo', True);
```

[Documentação Create Schema Databricks](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-create-schema)

### SEQ-4.5 - CREATE TABLE schema "bronze" 

Criação das tabelas no Schema de Dados "bronze" com a mesma estrutura dos arquivos.

Nessa etapa, as tabelas serão criadas as tabelas no Schema bronze.

A sintaxe do script é muito parecida com que possuímos em bancos de dados.

![Image](./imagens/03_create_table.png)

``` {.sql title="Criação das Tabelas no Schema Bronze" linenums=1}
%sql

DROP  TABLE IF EXISTS bronze.tb_forma_pagamento;
CREATE TABLE bronze.tb_forma_pagamento
(
CODIGO_FORMA_PAGAMENTO	 INT COMMENT 'Código da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
,DESCRICAO_FORMA_PAGAMENTO VARCHAR(100) COMMENT 'Descrição da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
)
COMMENT 'Armazena informações de forma de pagamento.';

DROP  TABLE IF EXISTS bronze.tb_categoria_produto;
CREATE TABLE bronze.tb_categoria_produto
(
CODIGO_CATEGORIA INT COMMENT 'Código da Categoria do Produto.'
,DECRICAO_CATEGORIA VARCHAR(100) COMMENT 'Descrição da Categoria do Produto.'
)
COMMENT 'Armazena informações das categorias dos produtos';

DROP  TABLE IF EXISTS bronze.tb_produto;
CREATE TABLE bronze.tb_produto
(
CODIGO_PRODUTO	 INT  COMMENT 'Código do Produto.'
,DESCRICAO_PRODUTO	 VARCHAR(100) COMMENT 'Descrição do Produto.'
,CODIGO_CATEGORIA INT COMMENT 'Categoria do Produto.'
)
COMMENT '	Armazena informações de produtos.';

DROP  TABLE IF EXISTS bronze.tb_cliente;
CREATE TABLE bronze.tb_cliente
(
CODIGO_CLIENTE INT COMMENT 'Código do Cliente.'
,NOME_CLIENTE VARCHAR(100) COMMENT 'Nome do Cliente.'
)
COMMENT 'Armazena informações de clientes.';

DROP  TABLE IF EXISTS bronze.tb_vendedor;
CREATE TABLE bronze.tb_vendedor
(
CODIGO_VENDEDOR INT COMMENT 'Código do Vendedor.'
,NOME_VENDEDOR VARCHAR(100) COMMENT 'Nome do Vendedor.'
)
COMMENT 'Armazena informações de vendedores.';

DROP  TABLE IF EXISTS bronze.tb_loja;
CREATE TABLE bronze.tb_loja
(
CODIGO_LOJA	 INT COMMENT 'Código da Loja.'
,NOME_LOJA	 VARCHAR(100) COMMENT 'Nome da Loja.'
,LOCALIDADE_LOJA	 VARCHAR(100) COMMENT 'Localidade da Loja.'
,TIPO_LOJA VARCHAR(100) COMMENT 'Tipo da Loja.'
)
COMMENT 'Armazena informações de lojas.';

DROP  TABLE IF EXISTS bronze.tb_venda;
CREATE TABLE bronze.tb_venda
(
CODIGO_VENDA INT COMMENT 'Código da Venda.'
,DATA_VENDA	TIMESTAMP COMMENT 'Data da Venda'
,CODIGO_CLIENTE	INT COMMENT 'Código do Cliente.'
,CODIGO_VENDEDOR	INT COMMENT 'Código do Vendedor.'
,CODIGO_LOJA	INT COMMENT 'Código da Loja.'
,VALOR_FINAL DECIMAL(18,2)	 COMMENT 'Valor Total da Venda.'
,FORMA_PAGAMENTO	INT COMMENT 'Forma de Pagamento.'
,TIPO_PAGAMENTO VARCHAR(100) COMMENT 'Tipo de Pagamento.'
)
COMMENT 'Armazenada informações de vendas.';

DROP  TABLE IF EXISTS bronze.tb_item_venda;
CREATE TABLE bronze.tb_item_venda
(
CODIGO_VENDA INT COMMENT 'Código da Venda.'
,CODIGO_PRODUTO	INT COMMENT 'Código do Produto.'
,VALOR_UNITARIO DECIMAL(18,2)	 COMMENT 'Valor Unitário do Produto.'
,QUANTIDADE	INT COMMENT 'Quantidade do Produto Vendido.'
,VALOR_FINAL DECIMAL(18,2) COMMENT 'Valor Final do Produto Vendido.'
)
COMMENT 'Armazena informações sobre os itens que foram vendidos.';
```

### SEQ-4.6 - CREATE TABLE schema "silver"

Criação das tabelas no Schema de Dados "silver".

``` {.sql title="Criação das Tabelas no Schema Silver" linenums=1}
%sql

DROP  TABLE IF EXISTS silver.tb_forma_pagamento;
CREATE TABLE silver.tb_forma_pagamento
(
CODIGO_FORMA_PAGAMENTO	 INT COMMENT 'Código da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
,DESCRICAO_FORMA_PAGAMENTO VARCHAR(100) COMMENT 'Descrição da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações de forma de pagamento.';

DROP  TABLE IF EXISTS silver.tb_categoria_produto;
CREATE TABLE silver.tb_categoria_produto
(
CODIGO_CATEGORIA INT COMMENT 'Código da Categoria do Produto.'
,DECRICAO_CATEGORIA VARCHAR(100) COMMENT 'Descrição da Categoria do Produto.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações das categorias dos produtos';

DROP  TABLE IF EXISTS silver.tb_produto;
CREATE TABLE silver.tb_produto
(
CODIGO_PRODUTO	 INT  COMMENT 'Código do Produto.'
,DESCRICAO_PRODUTO	 VARCHAR(100) COMMENT 'Descrição do Produto.'
,CODIGO_CATEGORIA INT COMMENT 'Categoria do Produto.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT '	Armazena informações de produtos.';

DROP  TABLE IF EXISTS silver.tb_cliente;
CREATE TABLE silver.tb_cliente
(
CODIGO_CLIENTE INT COMMENT 'Código do Cliente.'
,NOME_CLIENTE VARCHAR(100) COMMENT 'Nome do Cliente.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações de clientes.';

DROP  TABLE IF EXISTS silver.tb_vendedor;
CREATE TABLE silver.tb_vendedor
(
CODIGO_VENDEDOR INT COMMENT 'Código do Vendedor.'
,NOME_VENDEDOR VARCHAR(100) COMMENT 'Nome do Vendedor.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações de vendedores.';

DROP  TABLE IF EXISTS silver.tb_loja;
CREATE TABLE silver.tb_loja
(
CODIGO_LOJA	 INT COMMENT 'Código da Loja.'
,NOME_LOJA	 VARCHAR(100) COMMENT 'Nome da Loja.'
,LOCALIDADE_LOJA	 VARCHAR(100) COMMENT 'Localidade da Loja.'
,TIPO_LOJA VARCHAR(100) COMMENT 'Tipo da Loja.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações de lojas.';

DROP  TABLE IF EXISTS silver.tb_venda;
CREATE TABLE silver.tb_venda
(
CODIGO_VENDA INT COMMENT 'Código da Venda.'
,DATA_VENDA	TIMESTAMP COMMENT 'Data da Venda'
,CODIGO_CLIENTE	INT COMMENT 'Código do Cliente.'
,CODIGO_VENDEDOR	INT COMMENT 'Código do Vendedor.'
,CODIGO_LOJA	INT COMMENT 'Código da Loja.'
,VALOR_FINAL DECIMAL(18,2)	 COMMENT 'Valor Total da Venda.'
,FORMA_PAGAMENTO	INT COMMENT 'Forma de Pagamento.'
,TIPO_PAGAMENTO VARCHAR(100) COMMENT 'Tipo de Pagamento.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazenada informações de vendas.';

DROP  TABLE IF EXISTS silver.tb_item_venda;
CREATE TABLE silver.tb_item_venda
(
CODIGO_VENDA INT COMMENT 'Código da Venda.'
,CODIGO_PRODUTO	INT COMMENT 'Código do Produto.'
,VALOR_UNITARIO DECIMAL(18,2)	 COMMENT 'Valor Unitário do Produto.'
,QUANTIDADE	INT COMMENT 'Quantidade do Produto Vendido.'
,VALOR_FINAL DECIMAL(18,2) COMMENT 'Valor Final do Produto Vendido.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
)
COMMENT 'Armazena informações sobre os itens que foram vendidos.';
```

### SEQ-4.7 - CREATE TABLE schema "gold"

Criação das tabelas no Schema de Dados "gold".

``` {.sql title="Criação das Tabelas no Schema Gold" linenums=1}
%sql

DROP  TABLE IF EXISTS gold.dim_forma_pagamento;
CREATE TABLE gold.dim_forma_pagamento
(
ID_FORMA_PAGAMENTO VARCHAR(100) COMMENT 'Chave da Dimensão Forma de Pagamento.'
,CODIGO_FORMA_PAGAMENTO	 INT COMMENT 'Código da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
,DESCRICAO_FORMA_PAGAMENTO VARCHAR(100) COMMENT 'Descrição da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);

DROP  TABLE IF EXISTS gold.dim_produto;
CREATE TABLE gold.dim_produto
(
ID_PRODUTO VARCHAR(100) COMMENT 'Chave da Dimensão Produto.'
,CODIGO_PRODUTO	 INT  COMMENT 'Código do Produto.'
,DESCRICAO_PRODUTO VARCHAR(100) COMMENT 'Descrição do Produto.'
,CATEGORIA_PRODUTO VARCHAR(100) COMMENT 'Categoria do Produto.'
,SUB_CATEGORIA_PRODUTO VARCHAR(100) COMMENT 'Categoria do Produto.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);

DROP  TABLE IF EXISTS gold.dim_cliente;
CREATE TABLE gold.dim_cliente
(
ID_CLIENTE VARCHAR(100) COMMENT 'Chave da Dimensão Cliente.'
,CODIGO_CLIENTE INT COMMENT 'Código do Cliente.'
,NOME_CLIENTE VARCHAR(100) COMMENT 'Nome do Cliente.'
,DATA_NASCIMENTO DATE COMMENT 'Data de Nascimento do Cliente'
,IDADE_CLIENTE INT COMMENT 'Idade do Cliente'
,DESCRICAO_ENDERECO VARCHAR(200) COMMENT 'Endereço do Cliente'
,NUMERO_ENDERECO INT COMMENT 'Numero da Residencia do Cliente'
,NOME_CIDADE VARCHAR(100) COMMENT 'Cidade de Residência do Cliente'
,NUMERO_TELEFONE VARCHAR(30) COMMENT 'Telefone do Cliente'
,EMAIL_CLIENTE VARCHAR(100) COMMENT 'E-mail do Cliente'
,OCUPACAO_CLIENTE VARCHAR(100) COMMENT 'Ocupação do cliente'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);

DROP  TABLE IF EXISTS gold.dim_loja;
CREATE TABLE gold.dim_loja
(
ID_LOJA VARCHAR(100) COMMENT 'Chave da Dimensão Loja.'
,CODIGO_LOJA	 INT COMMENT 'Código da Loja.'
,NOME_LOJA	 VARCHAR(100) COMMENT 'Nome da Loja.'
,NOME_VENDEDOR VARCHAR(100)  COMMENT 'Nome do Vendedor.'
,LOCALIDADE_LOJA	 VARCHAR(100) COMMENT 'Localidade da Loja.'
,TIPO_LOJA VARCHAR(100) COMMENT 'Tipo da Loja.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);

DROP  TABLE IF EXISTS gold.dim_tempo;
CREATE TABLE gold.dim_tempo
(
ID_TEMPO VARCHAR(100) COMMENT 'Chave da Dimensão Tempo.'
,DATA VARCHAR(10) COMMENT 'Data.'
,ANO INT COMMENT 'Ano referente a coluna data.'
,MES	INT COMMENT 'Mês referente a coluna data.'
,DIA INT COMMENT 'Dia referente a coluna data.' 
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);

DROP  TABLE IF EXISTS gold.fato_venda;
CREATE TABLE gold.fato_venda
(
CODIGO_VENDA INT COMMENT 'Código da Venda.'
,ID_CLIENTE	VARCHAR(100)  COMMENT 'Chave da Dimensão Cliente.'
,ID_LOJA VARCHAR(100) COMMENT 'Chave da Dimensão Loja.'
,ID_PRODUTO	VARCHAR(100)  COMMENT 'Chave da Dimensão Produto.'
,ID_FORMA_PAGAMENTO	 VARCHAR(100) COMMENT 'Chave da Dimensão Forma de Pagamento.'
,ID_TEMPO VARCHAR(100)  COMMENT 'Chave da Dimensão Tempo.'
,HORA_VENDA	INT COMMENT 'Hora em que ocorreu a venda.'
,QUANTIDADE	INT COMMENT 'Quantidade vendida do produto.'
,VALOR_UNITARIO DECIMAL(18,2)	 COMMENT 'Valor unitário do produto.'
,VALOR_FINAL DECIMAL(18,2)	 COMMENT 'Valor vendido de um produto.'
,TIPO_PAGAMENTO VARCHAR(100) COMMENT 'Tipo de Pagamentto da Venda.'
,DATA_CADASTRO TIMESTAMP COMMENT 'Data de Cadastro do Registro.'
,DATA_ALTERACAO TIMESTAMP COMMENT 'Data de Atualização do Registro.'
);
```

### SEQ-4.8 - Inserção Dimensão Tempo

Script para inserção dos dados na Dimensão Tempo.

``` {.py3 title="Populando a Dimensão Tempo" linenums=1}
data_inicial = date(2023, 6, 1)
data_fim = date(2023, 8, 1)
dias_acrescimo = timedelta(days=1)

cria_dimensao_tempo(data_inicial, data_fim, dias_acrescimo)
```

### SEQ-4.9 - Listando as Tabelas do Schema

Script para visualizar todas as tabelas de um schema qualquer.

``` {.sql title="Listando as Tabelas do Schema" linenums=1}
%sql
SHOW TABLES FROM silver
```

### SEQ-4.10 - Visualizar Estrutura de Tabela

Script para visualizar a estrutura de uma tabela qualquer.

``` {.sql title="Listando a Estrutura de uma tabela" linenums=1}
%sql
DESC gold.DIM_LOJA
```

### SEQ-4.11 - Visualizar Armazenamento de uma Tabela

Script para visualizar informações de armazenamento de uma tabela qualquer.

``` {.sql title="Listando Informações da Tabela" linenums=1}
%sql
DESC DETAIL gold.DIM_LOJA
```

### SEQ-4.11 - Visualizar Estrutura de Schema

Script para visualizar a estrutura de um schema.

``` {.sql title="Listando a Estrutura do Schema" linenums=1}
%sql
DESC SCHEMA bronze
```