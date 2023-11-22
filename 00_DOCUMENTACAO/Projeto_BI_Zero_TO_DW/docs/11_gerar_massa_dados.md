# Projeto BI Zero TO DW

### 10 - Notebook Externo

### SEQ-11.1 - Definindo as Bibliotecas

Selecionado quais bibliotecas serão usadas.

``` {.py3 title="Bibliotecas Usadas" linenums=1}
import pandas as pd
import numpy as np
```

### SEQ-11.2 - Massa de Dados de Produtos

```{.py3 title="Criação Dataframe de Produtos" linenums=1}
dadosProdutos = [('ABÓBORA', 'Verduras e Legumes', 'Verduras e Legumes')
,('ACELGA', 'Verduras e Legumes', 'Verduras e Legumes')
,('AGRIÃO', 'Verduras e Legumes', 'Verduras e Legumes')
,('ALCACHOFRA', 'Verduras e Legumes', 'Verduras e Legumes')
,('ALFACE', 'Verduras e Legumes', 'Verduras e Legumes')
,('ALHO-PORÓ', 'Verduras e Legumes', 'Verduras e Legumes')
,('ALMEIRÃO', 'Verduras e Legumes', 'Verduras e Legumes')
,('ASPARGO', 'Verduras e Legumes', 'Verduras e Legumes')
,('BATATA', 'Verduras e Legumes', 'Verduras e Legumes')
,('BERINJELA', 'Verduras e Legumes', 'Verduras e Legumes')
,('BERTALHA', 'Verduras e Legumes', 'Verduras e Legumes')
,('BETERRABA', 'Verduras e Legumes', 'Verduras e Legumes')
,('BRÓCOLIS', 'Verduras e Legumes', 'Verduras e Legumes')
,('CEBOLA', 'Verduras e Legumes', 'Verduras e Legumes')
,('CENOURA', 'Verduras e Legumes', 'Verduras e Legumes')
,('CHICÓRIA', 'Verduras e Legumes', 'Verduras e Legumes')
,('CHUCHU', 'Verduras e Legumes', 'Verduras e Legumes')
,('COUVE', 'Verduras e Legumes', 'Verduras e Legumes')
,('COUVE–FLOR', 'Verduras e Legumes', 'Verduras e Legumes')
,('JILÓ', 'Verduras e Legumes', 'Verduras e Legumes')
,('LENTILHA', 'Verduras e Legumes', 'Verduras e Legumes')
,('MANDIOCA', 'Verduras e Legumes', 'Verduras e Legumes')
,('MAXIXE', 'Verduras e Legumes', 'Verduras e Legumes')
,('MILHO VERDE', 'Verduras e Legumes', 'Verduras e Legumes')
,('MOSTARDA', 'Verduras e Legumes', 'Verduras e Legumes')
,('NABO', 'Verduras e Legumes', 'Verduras e Legumes')
,('PALMITO', 'Verduras e Legumes', 'Verduras e Legumes')
,('PEPINO', 'Verduras e Legumes', 'Verduras e Legumes')
,('PIMENTÃO', 'Verduras e Legumes', 'Verduras e Legumes')
,('QUIABO', 'Verduras e Legumes', 'Verduras e Legumes')
,('RABANETE', 'Verduras e Legumes', 'Verduras e Legumes')
,('TOMATE', 'Verduras e Legumes', 'Verduras e Legumes')
,('VAGEM', 'Verduras e Legumes', 'Verduras e Legumes')
,('Filé Mignon', 'Carne Boi', 'Carnes')
,('Maminha', 'Carne Boi', 'Carnes')
,('Picanha', 'Carne Boi', 'Carnes')
,('Coxão mole', 'Carne Boi', 'Carnes')
,('Patinho', 'Carne Boi', 'Carnes')
,('Lagarto', 'Carne Boi', 'Carnes')
,('Contrafilé', 'Carne Boi', 'Carnes')
,('Alcatra', 'Carne Boi', 'Carnes')
,('Costela', 'Carne Boi', 'Carnes')
,('Paleta', 'Carne Boi', 'Carnes')
,('Chuleta', 'Carne Boi', 'Carnes')
,('Coxão Duro', 'Carne Boi', 'Carnes')
,('Fraldinha', 'Carne Boi', 'Carnes')
,('Acém', 'Carne Boi', 'Carnes')
,('Músculo dianteiro', 'Carne Boi', 'Carnes')
,('Coxa', 'Carne Frango', 'Carnes')
,('Coxinha da asa', 'Carne Frango', 'Carnes')
,('Coxa com sobrecoxa', 'Carne Frango', 'Carnes')
,('Coração', 'Carne Frango', 'Carnes')
,('Sobrecoxa', 'Carne Frango', 'Carnes')
,('Sassami', 'Carne Frango', 'Carnes')
,('Filé de sobrecoxa', 'Carne Frango', 'Carnes')
,('Filé de peito', 'Carne Frango', 'Carnes')
,('Salmão', 'Carne Peixe', 'Carnes')
,('Bacalhau', 'Carne Peixe', 'Carnes')
,('Atum', 'Carne Peixe', 'Carnes')
,('Sardinha', 'Carne Peixe', 'Carnes')
,('Merluza', 'Carne Peixe', 'Carnes')
,('Corvina', 'Carne Peixe', 'Carnes')
,('Camarão', 'Carne Peixe', 'Carnes')
,('Pescadinha', 'Carne Peixe', 'Carnes')
,('Johnnie Walker', 'Whisky','Bebidas')
,('Smirnoff', 'Vodka','Bebidas')
,('Bacardi', 'Rum','Bebidas')
,('Jack Daniels', 'Whisky','Bebidas')
,('Absolut', 'Vodka','Bebidas')
,('Martini', 'Rum','Bebidas')
,('Chivas Regal', 'Whisky','Bebidas')
,('Ballantines', 'Whisky','Bebidas')
,('Moët & Chandon', 'Champagne','Bebidas')
,('Gordons', 'Gin','Bebidas')
,('Grants', 'Whisky','Bebidas')
,('Skyy', 'Vodka','Bebidas')
,('Cîroc', 'Vodka','Bebidas')
,('Malibu', 'Rum','Bebidas')
,('Tanqueray', 'Gin','Bebidas')
,('Coca-Cola', 'Refrigerante','Bebidas')
,('Coca-Cola Zero', 'Refrigerante','Bebidas')
,('Guaraná Antarctica', 'Refrigerante','Bebidas')
,('Mineirinho', 'Refrigerante','Bebidas')
,('Pepsi', 'Refrigerante','Bebidas')
,('Pepsi Zero', 'Refrigerante','Bebidas')
,('Pepsi Twister', 'Refrigerante','Bebidas')
,('Fanta Laranja', 'Refrigerante','Bebidas')
,('Fanta Uva', 'Refrigerante','Bebidas')
,('Sprite', 'Refrigerante','Bebidas')
,('Sprite Zero', 'Refrigerante','Bebidas')
,('Kuat', 'Refrigerante','Bebidas')]

dfProdutos = pd.DataFrame(dadosProdutos, columns=['DESCRICAO_PRODUTO', 'TIPO_PRODUTO', 'CODIGO_CATEGORIA'])

dfProdutos = dfProdutos.sort_values(by=['CODIGO_CATEGORIA','TIPO_PRODUTO','DESCRICAO_PRODUTO'])

dfProdutos = dfProdutos.reset_index()

dfProdutos['CODIGO_PRODUTO'] = np.arange(1, len(dfProdutos) + 1)

dfProdutos = dfProdutos[['CODIGO_PRODUTO','DESCRICAO_PRODUTO', 'TIPO_PRODUTO', 'CODIGO_CATEGORIA']]

dfProdutos.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\produtos.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)
```

### SEQ-11.3 - Massa de Dados de Cliente

```{.py3 title="Criação Dataframe de Clientes" linenums=1}
df = pd.read_csv(f'C:\Temp\Python_YT\Arquivo_Exemplo\exemplo_pessoas.csv' , sep='|')

dfPessoas = df.loc[1:1000,['Nome']]

dfPessoas = dfPessoas.rename(columns={'Nome':'NOME_CLIENTE'})

dfPessoas = dfPessoas.sort_values(by='NOME_CLIENTE')

dfPessoas['CODIGO_CLIENTE'] = np.arange(1, len(dfPessoas) + 1)

dfPessoas = dfPessoas[['CODIGO_CLIENTE','NOME_CLIENTE']]

dfPessoas.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\clientes.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)
```

### SEQ-11.4 - Massa de Dados de Vendedor

```{.py3 title="Criação Dataframe de Vendedores" linenums=1}
dfPessoasVendedor = df.loc[3333:3383,['Nome']] #.sort_values(by=['Nome'])
dfVendedor = pd.DataFrame(columns=['CODIGO_VENDEDOR','NOME_VENDEDOR'])

codigo_vendedor_inicial = 1
codigo_vendedor_final = len(dfVendedor)

for vendedor in dfPessoasVendedor['Nome']:

    dados = [{'CODIGO_VENDEDOR' : codigo_vendedor_inicial,'NOME_VENDEDOR': vendedor}]       

    df1 = pd.DataFrame(dados)   

    dfVendedor =  pd.concat([dfVendedor, df1])

    codigo_vendedor_inicial = codigo_vendedor_inicial + 1  

dfVendedor.set_index('CODIGO_VENDEDOR', inplace=True)

dfVendedor.reset_index(inplace=True)

dfVendedor.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\vendedores.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)
```


### SEQ-11.5 - Massa de Dados de Forma de Pagamento

```{.py3 title="Criação Dataframe de Forma de Pagamento" linenums=1}
dadosFormaPagamento = ['CARTÃO DÉBITO'
,'PIX'
,'CARTÃO CRÉDITO'
,'BOLETO']

dfFormaPagamento = pd.DataFrame(dadosFormaPagamento, columns=['DESCRICAO_FORMA_PAGAMENTO'])

dfFormaPagamento['CODIGO_FORMA_PAGAMENTO'] = np.arange(1, len(dfFormaPagamento) + 1)

dfFormaPagamento.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\forma_pagamento.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)
```


### SEQ-11.6 - Massa de Dados de Loja

```{.py3 title="Criação Dataframe de Loja" linenums=1}
dadosloja = [
('E-COMMERCE','WWW','VIRTUAL'),
('LOJA A','MT','FÍSICA'),
('LOJA B','RJ','FÍSICA'),
('LOJA C','CE','FÍSICA')
]

dfLoja = pd.DataFrame(dadosloja, columns=['NOME_LOJA', 'LOCALIDADE_LOJA', 'TIPO_LOJA'])

dfLoja['CODIGO_LOJA'] = np.arange(1, len(dfLoja) + 1)

dfLoja.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\lojas.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)
```

### SEQ-11.7 - Massa de Dados de Venda

```{.py3 title="Criação Dataframe de Venda" linenums=1}
dfFinal = pd.DataFrame(columns=['CODIGO_VENDA'
                    ,'DATA_VENDA'
                    ,'CODIGO_CLIENTE'
                    ,'NOME_CLIENTE'
                    ,'CODIGO_PRODUTO'
                    ,'DESCRICAO_PRODUTO'
                    ,'CODIGO_CATEGORIA'
                    ,'TIPO_PRODUTO'
                    ,'CODIGO_VENDEDOR'
                    ,'NOME_VENDEDOR'
                    ,'CODIGO_LOJA'
                    ,'NOME_LOJA'
                    ,'LOCALIDADE_LOJA'
                    ,'TIPO_LOJA'
                    ,'VALOR_UNITARIO'
                    ,'QUANTIDADE'
                    ,'VALOR_FINAL'
                    ,'TIPO_PAGAMENTO'])

codigo_venda_inicial = 1
codigo_venda_final = len(dfPessoas)

for pessoa in dfPessoas.index:

    data_inicio = pd.to_datetime('2023-01-02')
    data_fim = pd.to_datetime('2023-10-31')

    indice_randomico = np.random.choice(dfProdutos.index, size = 3 , replace=False)
    indice_randomico_vendedor = int(np.random.choice(dfVendedor.index, size = 1 , replace=False))
    indice_randomico_forma_pagamento = int(np.random.choice(dfFormaPagamento.index, size = 1 , replace=False))    
    indice_randomico_loja = int(np.random.choice(dfLoja.index, size = 1 , replace=False))    

    v_vendedor = dfVendedor['NOME_VENDEDOR'][indice_randomico_vendedor]
    v_codigo_vendedor = dfVendedor['CODIGO_VENDEDOR'][indice_randomico_vendedor]
    
    p_data_venda = pd.to_datetime(np.random.uniform(data_inicio.value, data_fim.value, size=365))
    v_data_venda = p_data_venda[0].strftime('%Y-%m-%d')

    v_codigo_loja = dfLoja['CODIGO_LOJA'][indice_randomico_loja]
    v_loja = dfLoja['NOME_LOJA'][indice_randomico_loja]
    v_lojalocalidade = dfLoja['LOCALIDADE_LOJA'][indice_randomico_loja]   
    v_lojatipo = dfLoja['TIPO_LOJA'][indice_randomico_loja]       
    v_formaPagamento = dfFormaPagamento['DESCRICAO_FORMA_PAGAMENTO'][indice_randomico_forma_pagamento]
    v_codigo_formaPagamento = dfFormaPagamento['CODIGO_FORMA_PAGAMENTO'][indice_randomico_forma_pagamento]

    v_pessoa = dfPessoas['NOME_CLIENTE'][pessoa]
    v_codigo_cliente = dfPessoas['CODIGO_CLIENTE'][pessoa]

    for i in indice_randomico:

        if dfProdutos['TIPO_PRODUTO'][i] == 'Whisky':

            valor_min = 89.98
            valor_max = 179.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Vodka':

            valor_min = 35.99
            valor_max = 99.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Refrigerante':

            valor_min = 6.00
            valor_max = 9.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Rum':

            valor_min = 69.00
            valor_max = 99.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Champagne':

            valor_min = 115.00
            valor_max = 159.99

            valor = np.random.uniform(valor_min, valor_max, size=1)            

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Gin':

            valor_min = 99.00
            valor_max = 119.99

            valor = np.random.uniform(valor_min, valor_max, size=1)    

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 'Verduras e Legumes':

            valor_min = 0.99
            valor_max = 5.99

            valor = np.random.uniform(valor_min, valor_max, size=1)    

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Carne Boi':

            valor_min = 29.99
            valor_max = 75.99

            valor = np.random.uniform(valor_min, valor_max, size=1) 

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Carne Frango':

            valor_min = 14.99
            valor_max = 29.99

            valor = np.random.uniform(valor_min, valor_max, size=1) 

        elif dfProdutos['TIPO_PRODUTO'][i] == 'Carne Peixe':

            valor_min = 29.99
            valor_max = 85.99

            valor = np.random.uniform(valor_min, valor_max, size=1)             

        else:

            valor = 0.

        v_quantidade = int(np.random.randint(1, 10, size=1))

        v_produto = dfProdutos['DESCRICAO_PRODUTO'][i]
        v_codigo_produto = dfProdutos['CODIGO_PRODUTO'][i]
        v_categoria_produto = dfProdutos['TIPO_PRODUTO'][i]
        v_tipo_produto = dfProdutos['CODIGO_CATEGORIA'][i]

        v_tipo_pagamento = 'A VISTA'
        
        dados = [{ 'CODIGO_VENDA' : codigo_venda_inicial
                    ,'DATA_VENDA': str(v_data_venda)
                    ,'CODIGO_CLIENTE': v_codigo_cliente
                    ,'NOME_CLIENTE': v_pessoa
                    ,'CODIGO_PRODUTO' : v_codigo_produto
                    ,'DESCRICAO_PRODUTO' : v_produto
                    ,'CODIGO_CATEGORIA' : v_categoria_produto
                    ,'TIPO_PRODUTO' : v_tipo_produto
                    ,'CODIGO_VENDEDOR': v_codigo_vendedor
                    ,'NOME_VENDEDOR' : v_vendedor
                    ,'CODIGO_LOJA': v_codigo_loja
                    ,'NOME_LOJA': v_loja
                    ,'LOCALIDADE_LOJA': v_lojalocalidade
                    ,'TIPO_LOJA': v_lojatipo
                    ,'VALOR_UNITARIO': round(float(valor),2)
                    ,'QUANTIDADE': v_quantidade
                    ,'VALOR_FINAL': round((round(float(valor),2) * v_quantidade),2)
                    ,'FORMA_PAGAMENTO' : v_codigo_formaPagamento
                    ,'TIPO_PAGAMENTO' : v_tipo_pagamento}]       

        df = pd.DataFrame(dados)

        dfFinal =  pd.concat([dfFinal, df])

    codigo_venda_inicial = codigo_venda_inicial + 1


dfVenda = (dfFinal.groupby(['CODIGO_VENDA'
                            ,'DATA_VENDA'
                            ,'CODIGO_CLIENTE'
                            ,'CODIGO_VENDEDOR'
                            ,'CODIGO_LOJA'
                            ,'FORMA_PAGAMENTO'
                            ,'TIPO_PAGAMENTO'], as_index=False)
                .agg(VALOR_FINAL=('VALOR_FINAL','sum'))
                     .sort_values(by=['DATA_VENDA','CODIGO_VENDA'])
                     .reset_index(drop=True))

dfVenda.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\vendas.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

dfItemVenda = (dfFinal.groupby(['CODIGO_VENDA', 'CODIGO_PRODUTO'], as_index=False)
                .agg(VALOR_UNITARIO=('VALOR_UNITARIO','sum')
                     ,QUANTIDADE=('QUANTIDADE','sum')
                     ,VALOR_FINAL=('VALOR_FINAL','sum'))
                     .sort_values(by=['CODIGO_VENDA', 'CODIGO_PRODUTO'])
                     .reset_index(drop=True))

dfItemVenda.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\item_vendas.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)


```

