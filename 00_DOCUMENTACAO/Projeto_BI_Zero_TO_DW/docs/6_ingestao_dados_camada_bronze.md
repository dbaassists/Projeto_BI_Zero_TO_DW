# Projeto BI Zero TO DW

## 6 - Ingestão dos Dados na Camada Bronze


|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-6.1 / SEQ-6.2|Ingestão dos Dados|Identificar no storage "dbfs:/FileStore/tables/landing_zone" os dados a serem inseridos na camada BRONZE.|

O arquivo do Notebook é encontrado aqui. [Notebook Ingestão Dados Para Camada Bronze](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/02_NOTEBOOK/02_ingestao_camada_bronze.ipynb)

### SEQ-6.1 - Origem dos Dados no Databricks 

Nessa etapa definimos onde os nossos dados foram armazenados na etapa de extração de dados do Azure SQL Database.

```
diretorio_landing_zone = "dbfs:/FileStore/tables/landing_zone/"
arquivos_diretorio = dbutils.fs.ls(diretorio_landing_zone)
```

### SEQ-6.2 - Carga Dados Camada Bronze

Rotina de leitura dos arquivos e carga na camada bronze.

```
for arquivo in arquivos_diretorio:

    diretorio = arquivo.path
    tabela = arquivo.name.replace('/','').lower()

    parDF1=spark.read.parquet(diretorio)

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

    if tabela == 'tb_item_venda':
        listaCondicao = listaCondicao + ' AND a.CODIGO_PRODUTO = b.CODIGO_PRODUTO'


    tabela_dl = tabela.replace('dbo.','')

    parDF1.createOrReplaceTempView(tabela)

    comando_truncate = f"""TRUNCATE TABLE bronze.{tabela}"""

    print(comando_truncate)

    spark.sql(comando_truncate)

    comando_insert = f"""MERGE INTO bronze.{tabela} a
            USING {tabela} b
            ON {listaCondicao}
            WHEN NOT MATCHED
            THEN INSERT ({lista1}) VALUES ({listaInsert})
            """

    print(comando_insert)

    spark.sql(comando_insert)
```