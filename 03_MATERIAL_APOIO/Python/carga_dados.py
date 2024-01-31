# %%

import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import os

server = 'localhost\DBAASSISTS'
database = 'TREINAMENTO' 
username = 'usr_treinamento' 
password = 'Tr&in@M&nT0SQL2024!' 
driver = 'SQL Server'

# %% 

print('00 (INICIO) - TERMINO PROCESSO DE CARGA DADOS')
# %% 

print('01 (INICIO) - CARGA DE DADOS DE CLIENTES')

diretorio = fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\01_clientes.csv'

dfcliente = pd.read_csv(diretorio
                    ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""
                        TRUNCATE TABLE dbo.TB_ITEM_VENDA;
                        DELETE FROM dbo.TB_VENDA;
                        DELETE FROM dbo.TB_CLIENTE;
                        """)

        for i, coluna in dfcliente.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_CLIENTE ON;  
                        INSERT INTO dbo.TB_CLIENTE (CODIGO_CLIENTE
                                                    ,NOME_CLIENTE
                                                    ,DATA_NASCIMENTO
                                                    ,IDADE_CLIENTE
                                                    ,DESCRICAO_ENDERECO
                                                    ,NUMERO_ENDERECO
                                                    ,NOME_CIDADE
                                                    ,NUMERO_TELEFONE
                                                    ,EMAIL_CLIENTE
                                                    ,OCUPACAO_CLIENTE) 
                                                    VALUES 
                                                    ({coluna['CODIGO_CLIENTE']} 
                                                    ,'{coluna['NOME_CLIENTE']}'
                                                    ,'{coluna['DATA_NASCIMENTO']}'
                                                    ,'{coluna['IDADE_CLIENTE']}'
                                                    ,'{coluna['DESCRICAO_ENDERECO']}'
                                                    ,'{coluna['NUMERO_ENDERECO']}'
                                                    ,'{coluna['NOME_CIDADE']}'
                                                    ,'{coluna['NUMERO_TELEFONE']}'
                                                    ,'{coluna['EMAIL_CLIENTE']}'
                                                    ,'{coluna['OCUPACAO_CLIENTE']}'
                                                    )
                        SET IDENTITY_INSERT dbo.TB_CLIENTE OFF;
                        """)
            
print('01 (FIM) - CARGA DE DADOS DE CLIENTES')


                       
# %%

print('02 (INICIO) - CARGA DE DADOS DE VENDEDORES')

dfvendedor = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\03_vendedores.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""DELETE FROM dbo.TB_LOJA;
                       DELETE FROM dbo.TB_VENDEDOR;
                       """)

        for i, coluna in dfvendedor.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_VENDEDOR ON;  
                        INSERT INTO dbo.TB_VENDEDOR 
                        (CODIGO_VENDEDOR
                        ,NOME_VENDEDOR) 
                        VALUES (
                           {coluna['CODIGO_VENDEDOR']} 
                        , '{coluna['NOME_VENDEDOR']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_VENDEDOR OFF;  
                        """)
            
print('02 (FIM) - CARGA DE DADOS DE VENDEDORES')            

       
# %%

print('03 (INICIO) - CARGA DE DADOS DE LOJAS')

dfloja = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\04_lojas.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:

        cursor.execute(fr"""
                        DELETE FROM dbo.TB_LOJA;
                        """)

        for i, coluna in dfloja.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_LOJA ON;
                        INSERT INTO dbo.TB_LOJA 
                        (CODIGO_LOJA_VENDEDOR
                        ,CODIGO_LOJA
                        ,CODIGO_VENDEDOR
                        ,NOME_LOJA
                        ,LOCALIDADE_LOJA
                        ,TIPO_LOJA) 
                        VALUES (
                        {coluna['CODIGO_LOJA_VENDEDOR']}
                        , {coluna['CODIGO_LOJA']}
                        , {coluna['CODIGO_VENDEDOR']}
                        , '{coluna['NOME_LOJA']}' 
                        , '{coluna['LOCALIDADE_LOJA']}'
                        , '{coluna['TIPO_LOJA']}')
                        SET IDENTITY_INSERT dbo.TB_LOJA OFF;
                        """)
            
print('03 (FIM) - CARGA DE DADOS DE LOJAS')            

# %%

print('04 (INICIO) - CARGA DE DADOS DE CATEGORIA PRODUTOS')

dfCategoriaProduto = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\08_categoria_produtos.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""
                        DELETE FROM dbo.TB_PRODUTO;
                        DELETE FROM dbo.TB_CATEGORIA_PRODUTO;
                        """)
        
        for i, coluna in dfCategoriaProduto.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_CATEGORIA_PRODUTO ON;  
                        INSERT INTO dbo.TB_CATEGORIA_PRODUTO 
                           (CODIGO_CATEGORIA
                           ,CATEGORIA_PRODUTO
                           ,SUB_CATEGORIA_PRODUTO) 
                        VALUES (
                           {coluna['CODIGO_CATEGORIA']} 
                        , '{coluna['CATEGORIA_PRODUTO']}'
                        , '{coluna['SUB_CATEGORIA_PRODUTO']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_CATEGORIA_PRODUTO OFF;  
                        """)

print('04 (FIM) - CARGA DE DADOS DE CATEGORIA PRODUTOS')

# %%

print('05 (INICIO) - CARGA DE DADOS DE PRODUTOS')

dfproduto = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\02_produtos.csv'
                        ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""DELETE FROM dbo.TB_PRODUTO;""")
        
        for i, coluna in dfproduto.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_PRODUTO ON;  
                        INSERT INTO dbo.TB_PRODUTO 
                           (CODIGO_PRODUTO
                           , DESCRICAO_PRODUTO
                           , CODIGO_CATEGORIA) 
                        VALUES (
                           {coluna['CODIGO_PRODUTO']} 
                        , '{coluna['DESCRICAO_PRODUTO']}'
                        , '{coluna['CODIGO_CATEGORIA']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_PRODUTO OFF;  
                        """)
            
print('05 (FIM) - CARGA DE DADOS DE PRODUTOS')            

# %%

print('06 (INICIO) - CARGA DE DADOS DE FORMA PAGAMENTO')

dfforma_pagamento = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\05_forma_pagamento.csv'
                        ,sep=';')

#with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""DELETE FROM dbo.TB_FORMA_PAGAMENTO;""")        

        for i, coluna in dfforma_pagamento.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_FORMA_PAGAMENTO ON;  
                        INSERT INTO dbo.TB_FORMA_PAGAMENTO 
                        (CODIGO_FORMA_PAGAMENTO
                        ,DESCRICAO_FORMA_PAGAMENTO) 
                        VALUES (
                        {coluna['CODIGO_FORMA_PAGAMENTO']}
                        ,'{coluna['DESCRICAO_FORMA_PAGAMENTO']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_FORMA_PAGAMENTO OFF;
                        """)

print('06 (FIM) - CARGA DE DADOS DE FORMA PAGAMENTP')            

# %%

print('07 (INICIO) - CARGA DE DADOS DE VENDAS')

dfVenda = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\06_vendas.csv'
                      ,dtype={'CODIGO_VENDA': int
                            ,'DATA_VENDA': str
                            ,'CODIGO_CLIENTE': int
                            ,'CODIGO_LOJA_VENDEDOR': int
                            ,'VALOR_FINAL': float
                            ,'FORMA_PAGAMENTO': int
                            ,'TIPO_PAGAMENTO': str}
                        ,parse_dates=['DATA_VENDA']
                        ,sep=';')


dfVenda.sort_values(by='FORMA_PAGAMENTO')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""
                       DELETE FROM dbo.TB_ITEM_VENDA;
                       DELETE FROM dbo.TB_VENDA;""")        

        for i, coluna in dfVenda.iterrows():

            cursor.execute(fr"""
                        SET IDENTITY_INSERT dbo.TB_VENDA ON;  
                        INSERT INTO dbo.TB_VENDA 
                        (CODIGO_VENDA
                        ,DATA_VENDA
                        ,CODIGO_CLIENTE
                        ,CODIGO_LOJA_VENDEDOR
                        ,VALOR_FINAL
                        ,CODIGO_FORMA_PAGAMENTO
                        ,TIPO_PAGAMENTO) 
                        VALUES (
                        {coluna['CODIGO_VENDA']}
                        ,'{coluna['DATA_VENDA']}'
                        ,{coluna['CODIGO_CLIENTE']}
                        ,{coluna['CODIGO_LOJA_VENDEDOR']}
                        ,'{coluna['VALOR_FINAL']}'
                        ,{coluna['FORMA_PAGAMENTO']}
                        ,'{coluna['TIPO_PAGAMENTO']}'
                        )
                        SET IDENTITY_INSERT dbo.TB_VENDA OFF;
                        """)            
            
print('07 (FIM) - CARGA DE DADOS DE VENDAS')

# %%

print('08 (INICIO) - CARGA DE DADOS DE ITEM VENDA')

dfItemVenda = pd.read_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\07_item_vendas.csv'
                      ,dtype={'CODIGO_VENDA': int
                            ,'CODIGO_PRODUTO': str
                            ,'VALOR_UNITARIO': float
                            ,'QUANTIDADE': int
                            ,'VALOR_FINAL': float}
                        ,sep=';')

with pyodbc.connect('DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

    with conn.cursor() as cursor:

        cursor.execute(fr"""TRUNCATE TABLE dbo.TB_ITEM_VENDA;""")        

        for i, coluna in dfItemVenda.iterrows():

            cursor.execute(fr"""
                        INSERT INTO dbo.TB_ITEM_VENDA 
                        (CODIGO_VENDA
                        ,CODIGO_PRODUTO
                        ,VALOR_UNITARIO
                        ,QUANTIDADE
                        ,VALOR_FINAL) 
                        VALUES (
                        {coluna['CODIGO_VENDA']}
                        ,{coluna['CODIGO_PRODUTO']}
                        ,{coluna['VALOR_UNITARIO']}
                        ,{coluna['QUANTIDADE']}
                        ,{coluna['VALOR_FINAL']}
                        )
                        """)

print('08 (FIM) - CARGA DE DADOS DE ITEM VENDA')

# %%

print('00 (FIM) - TERMINO PROCESSO DE CARGA DADOS')
