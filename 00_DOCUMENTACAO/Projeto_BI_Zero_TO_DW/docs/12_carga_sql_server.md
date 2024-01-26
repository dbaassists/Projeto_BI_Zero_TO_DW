# Projeto BI Zero TO DW

### 12 - Notebook Carga de Dados no Axure SQL Server

### SEQ-12.1 - Definindo as Bibliotecas

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Bibliotecas Usadas" linenums=1}
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import os

server = 'srv-db-treinamentosql.database.windows.net'
database = 'srv-db-treinamentosql' 
username = 'usr-srv-treinamentosql' 
password = 'Tr&in@M&nT0SQL2023!' 
driver = 'ODBC Driver 17 for SQL Server'
```

### SEQ-12.2 - Carga de Clientes

``` {.py3 title="Carga de Clientes" linenums=1}
dfcliente = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\clientes.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        for i, coluna in dfcliente.iterrows():

            print(coluna['Nome'])

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_CLIENTE ON;  
                        INSERT INTO dbo.TB_CLIENTE (CODIGO_CLIENTE, NOME_CLIENTE) VALUES ({coluna['CodigoCliente']} , '{coluna['Nome']}')
                        SET IDENTITY_INSERT dbo.TB_CLIENTE OFF;
                        """)
```


### SEQ-12.3 - Carga de Lojas

``` {.py3 title="Carga de Lojas" linenums=1}
dfloja = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\lojas.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        for i, coluna in dfloja.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_LOJA ON;
                        INSERT INTO dbo.TB_LOJA 
                        (
                        CODIGO_LOJA
                        ,NOME_LOJA
                        ,LOCALIDADE_LOJA
                        ,TIPO_LOJA) 
                        VALUES (
                        {coluna['CodigoLoja']}
                        , '{coluna['NomeLoja']}' 
                        , '{coluna['LocalidadeLoja']}'
                        , '{coluna['TipoLoja']}')
                        SET IDENTITY_INSERT dbo.TB_LOJA OFF;
                        """)

```

### SEQ-12.4 - Carga de Produto

``` {.py3 title="Carga de Produto" linenums=1}

dfproduto = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\produtos.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        for i, coluna in dfproduto.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_PRODUTO ON;  
                        INSERT INTO dbo.TB_PRODUTO 
                           (CODIGO_PRODUTO
                           , DESCRICAO_PRODUTO
                           , CODIGO_CATEGORIA
                           ,TIPO_PRODUTO) 
                        VALUES (
                           {coluna['CodigoProduto']} 
                        , '{coluna['Nome']}'
                        , '{coluna['Categoria']}'
                        , '{coluna['Tipo']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_PRODUTO OFF;  
                        """)

```

### SEQ-12.5 - Carga de Vendedores

``` {.py3 title="Carga de Vendedores" linenums=1}


dfvendedor = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\vendedores.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        for i, coluna in dfvendedor.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_VENDEDOR ON;  
                        INSERT INTO dbo.TB_VENDEDOR 
                        (CODIGO_VENDEDOR
                        , NOME_VENDEDOR) 
                        VALUES (
                           {coluna['CodigoVendedor']} 
                        , '{coluna['NomeVendedor']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_VENDEDOR OFF;  
                        """)

```


### SEQ-12.6 - Carga de Formas Pagamento

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Carga de Formas Pagamento" linenums=1}
dfforma_pagamento = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\forma_pagamento.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        for i, coluna in dfforma_pagamento.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_FORMA_PAGAMENTO ON;  
                        INSERT INTO dbo.TB_FORMA_PAGAMENTO 
                        (CODIGO_FORMA_PAGAMENTO
                        ,DESCRICAO_FORMA_PAGAMENTO) 
                        VALUES (
                        {coluna['CodigoFormaPagamento']}
                        ,'{coluna['FormaPagamento']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_FORMA_PAGAMENTO OFF;
                        """)
```