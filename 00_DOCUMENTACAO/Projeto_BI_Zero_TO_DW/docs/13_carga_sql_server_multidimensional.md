# Projeto BI Zero TO DW

### 13 - Notebook Carga de Dados no Axure SQL Server

### SEQ-13.1 - Definindo as Bibliotecas

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Bibliotecas Usadas" linenums=1}
from pyspark.sql.functions import *
from datetime import date, timedelta
import pyodbc
```

### SEQ-13.2 - Instalação Biblioteca pyodbc

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Instalação Biblioteca pyodbc" linenums=1}
pip install pyodbc
```

### SEQ-13.3 - Importação Arquivo de Configuração no GitHub

Processo de busca das credenciais de acesso ao Azure SQL Database armazenadas no GitHub.

``` {.py3 title="Importação Arquivo de Configuração no GitHub" linenums=1}
dfjson =  pd.read_json("https://raw.githubusercontent.com/dbaassists/Projeto_BI_Zero_TO_DW/main/04_ARQUIVO_CONFIG/config_azure_sql.json")

server = dfjson['Config']['server']
database = dfjson['Config']['database']
username = dfjson['Config']['username']
password = dfjson['Config']['password']
```

### SEQ-13.4 - Instalação do Driver ODBC Driver on Azure Databricks cluster

Driver a ser instalado.

``` {.py3 title="Instalação do Driver ODBC Driver on Azure Databricks cluster" linenums=1}
%sh
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17
```

### SEQ-13.5 - Limpeza das Tabelas do Azure SQL Database

``` {.py3 title="Limpeza das Tabelas do Azure SQL Database" linenums=1}
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=srv-db-treinamentosql.database.windows.net;port=1433;DATABASE=srv-db-treinamentosql;UID='+username+';PWD='+ password)

lista_tabela = ['dw.Fato_Venda', 'dw.Dim_Cliente', 'dw.Dim_Produto', 'dw.Dim_Forma_Pagamento', 'dw.Dim_Tempo', 'dw.Dim_Loja']

for tabela in lista_tabela:

    print(tabela)

    cursor = cnxn.cursor()

    if tabela == 'dw.Fato_Venda':
        comando = 'TRUNCATE TABLE'
        print(comando)
        cursor.execute(f'TRUNCATE TABLE {tabela}')

    else:

        comando = 'DELETE FROM'
        print(comando)
        cursor.execute(f'DELETE FROM {tabela}')    

    cursor.commit()

cnxn.close()    
```

### SEQ-13.6 - Carga de Clientes (dw.Dim_Cliente)

``` {.py3 title="Carga de Clientes (dw.Dim_Cliente)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.dim_cliente
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Dim_Cliente") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()
```

### SEQ-13.7 - Carga de Produtos (dw.Dim_Produto)

``` {.py3 title="Carga de Produtos (dw.Dim_Produto)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.dim_produto
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Dim_Produto") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()
```

### SEQ-13.8 - Carga de Categoria de Forma de Pagamento (gold.dim_forma_pagamento)

``` {.py3 title="Carga de Categoria de Forma de Pagamento (gold.dim_forma_pagamento)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.dim_forma_pagamento
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Dim_Forma_Pagamento") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()
```


### SEQ-13.9 - Carga de Tempo (gold.dim_tempo)

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Carga de Tempo (gold.dim_tempo)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.dim_tempo
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Dim_Tempo") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()
```

### SEQ-13.10 - Carga de Formas de Loja (dw.Dim_loja)

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Carga de Formas de Loja (dw.Dim_loja)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.dim_loja
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Dim_Loja") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()   

```

### SEQ-13.8 - Carga de Vendas (dw.Fato_Venda)

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Carga de Vendas (dw.Fato_Venda)" linenums=1}

# Consulta SQL para selecionar os dados do Databricks SQL
query = """
SELECT * FROM gold.fato_venda
"""
# Carregando os dados do Databricks SQL
df = spark.sql(query)

# Escrevendo os dados no banco de dados Azure SQL
df.write \
    .format("jdbc") \
    .option("url",  f"jdbc:sqlserver://{server};database={database}") \
    .option("dbtable", "dw.Fato_Venda") \
    .option("user", username) \
    .option("password", password) \
    .mode("append") \
    .save()
```
