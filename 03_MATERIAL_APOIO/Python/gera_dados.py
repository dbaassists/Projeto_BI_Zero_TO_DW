# %%

import numpy as np
from faker import Faker
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from datetime import date
import random


# %%

print('00 (INICIO) - PROCESSO DE GERAÇÃO DOS DADOS')

# %%

print('01 (DEFINICAO) - CRIAÇÃO DA FUNÇÃO QUE GERA MASSA DE DADOS FAKE')

def geracao_dados_fake(qtd_rows: int = 100, locale: str = "pt_BR") -> DataFrame:

    data_atual = datetime.now()
    local_faker = Faker(locale)
    list_result = []
    for _ in range(qtd_rows):
        data_nascimento = local_faker.date()
        dict_result = {
            "Nome": local_faker.name(),
            "DataNascimento": str(data_nascimento),
            'NumIdade': (data_atual.date() - datetime.strptime(data_nascimento, "%Y-%m-%d").date()).days //365,
            "NomEndereco": local_faker.street_name(),
            "NumEndereco": local_faker.building_number(),
            "NomCidade": local_faker.city(),
            "NumTelefone": local_faker.phone_number(),
            "NomEmail": local_faker.ascii_email(),
            "NomOcupacao": local_faker.job()
        }
        list_result.append(dict_result)

    return pd.DataFrame(list_result)

# %% 

print('02 (INICIO) - PROCESSO DE GERAÇÃO DE DADOS DE PESSOAS FAKE')

dfDadosFake = geracao_dados_fake(1500)

arquivo = fr'C:\Temp\Python_YT\Arquivo_Exemplo\exemplo_pessoas.csv'

dfDadosFake.to_csv(arquivo
                 , sep=';'
                 , header=True
                 , index=False)

print('02 (FIM) - PROCESSO DE GERAÇÃO DE DADOS DE PESSOAS FAKE')

# %%

print('03 (INICIO) - PROCESSO DE GERAÇÃO DE DADOS DE PRODUTOS E CATEGORIAS')

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

dfProdutos = pd.DataFrame(dadosProdutos, columns=['DESCRICAO_PRODUTO' ,'TIPO_PRODUTO',  'CATEGORIA_PRODUTO'])

dfProdutos = dfProdutos.sort_values(by=['CATEGORIA_PRODUTO','DESCRICAO_PRODUTO'])

dfProdutos = dfProdutos.reset_index()

dfProdutos['CODIGO_PRODUTO'] = np.arange(1, len(dfProdutos) + 1)

print('03.1 (INICIO) - GERAÇÃO DE DADOS DE CATEGORIA DE PRODUTOS')

dfCategoriaProduto =  pd.DataFrame(columns=['CODIGO_CATEGORIA','CATEGORIA_PRODUTO','SUB_CATEGORIA_PRODUTO'])

dfCategoriaProduto_temp = pd.DataFrame()

listaCategoriaProduto = dfProdutos[['CATEGORIA_PRODUTO','TIPO_PRODUTO']].drop_duplicates()

codigo_categoria = 1

type(listaCategoriaProduto)

#for coluna in listaCategoriaProduto.columns:

for index, row in listaCategoriaProduto.iterrows():

    print(row['CATEGORIA_PRODUTO'])
    print(row['TIPO_PRODUTO'])

    dfCategoriaProduto_temp = pd.DataFrame({'CODIGO_CATEGORIA': [int(codigo_categoria)]
                                                ,'CATEGORIA_PRODUTO': [str(row['CATEGORIA_PRODUTO'])]
                                                ,'SUB_CATEGORIA_PRODUTO': [str(row['TIPO_PRODUTO'])]}
                                                )

    dfCategoriaProduto = dfCategoriaProduto.append(dfCategoriaProduto_temp)

    codigo_categoria += 1

dfCategoriaProduto.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\08_categoria_produtos.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('03.1 (FIM) - GERAÇÃO DE DADOS DE CATEGORIA DE PRODUTOS')

print('03.2 (INICIO) - GERAÇÃO DE DADOS DE PRODUTOS')

dfProdutos = pd.merge(dfProdutos
                      , dfCategoriaProduto
                              ,how='inner'
                              ,left_on=['CATEGORIA_PRODUTO','TIPO_PRODUTO']
                              ,right_on=['CATEGORIA_PRODUTO','SUB_CATEGORIA_PRODUTO']
                      )[['CODIGO_PRODUTO'
                        ,'DESCRICAO_PRODUTO'
                        ,'CODIGO_CATEGORIA']]

dfProdutos.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\02_produtos.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('03.2 (FIM) - GERAÇÃO DE DADOS DE PRODUTOS')

print('03 (INICIO) - PROCESSO DE GERAÇÃO DE DADOS DE PRODUTOS E CATEGORIAS')

# %%

print('04 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE CLIENTES')

df = pd.read_csv(f'C:\Temp\Python_YT\Arquivo_Exemplo\exemplo_pessoas.csv' , sep=';')

dfPessoas = df.loc[1:1398,['Nome','DataNascimento','NumIdade','NomEndereco','NumEndereco','NomCidade','NumTelefone','NomEmail','NomOcupacao']]

dfPessoas = dfPessoas.rename(columns={'Nome':'NOME_CLIENTE'
                                      ,'DataNascimento':'DATA_NASCIMENTO'
                                      ,'NumIdade':'IDADE_CLIENTE'
                                      ,'NomEndereco':'DESCRICAO_ENDERECO'
                                      ,'NumEndereco':'NUMERO_ENDERECO'
                                      ,'NomCidade':'NOME_CIDADE'
                                      ,'NumTelefone':'NUMERO_TELEFONE'
                                      ,'NomEmail':'EMAIL_CLIENTE'
                                      ,'NomOcupacao':'OCUPACAO_CLIENTE'})

dfPessoas = dfPessoas.sort_values(by='NOME_CLIENTE')

dfPessoas['CODIGO_CLIENTE'] = np.arange(1, len(dfPessoas) + 1)

dfPessoas = dfPessoas[['CODIGO_CLIENTE'
                        ,'NOME_CLIENTE'
                        ,'DATA_NASCIMENTO'
                        ,'IDADE_CLIENTE'
                        ,'DESCRICAO_ENDERECO'
                        ,'NUMERO_ENDERECO'
                        ,'NOME_CIDADE'
                        ,'NUMERO_TELEFONE'
                        ,'EMAIL_CLIENTE'
                        ,'OCUPACAO_CLIENTE']]

dfPessoas.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\01_clientes.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('04 (FIM) - PROCESSO GERAÇÃO DE DADOS DE CLIENTES')

# %% 

print('05 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE VENDEDORES')

dfPessoasVendedor = df.loc[1400:1438,['Nome']] #.sort_values(by=['Nome'])
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

dfVendedor.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\03_vendedores.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('05 (FIM) - PROCESSO GERAÇÃO DE DADOS DE VENDEDORES')

# %%

print('06 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE FORMA DE PAGAMENTO')

dadosFormaPagamento = ['CARTÃO DÉBITO'
,'PIX'
,'CARTÃO CRÉDITO'
,'BOLETO']

dfFormaPagamento = pd.DataFrame(dadosFormaPagamento, columns=['DESCRICAO_FORMA_PAGAMENTO'])

dfFormaPagamento['CODIGO_FORMA_PAGAMENTO'] = np.arange(1, len(dfFormaPagamento) + 1)

dfFormaPagamento.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\05_forma_pagamento.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('06 (FIM) - PROCESSO GERAÇÃO DE DADOS DE FORMA DE PAGAMENTO')

# %%

print('07 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE LOJAS')

dadosloja = [
('E-COMMERCE','WWW','VIRTUAL'),
('LOJA A','MT','FÍSICA'),
('LOJA B','RJ','FÍSICA'),
('LOJA C','CE','FÍSICA')
]

dfLoja = pd.DataFrame(dadosloja, columns=['NOME_LOJA', 'LOCALIDADE_LOJA', 'TIPO_LOJA'])

dfLoja['CODIGO_LOJA'] = np.arange(1, len(dfLoja) + 1)

dfLoja.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\04_lojas.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('07 (FIM) - PROCESSO GERAÇÃO DE DADOS DE LOJAS')

# %% 

print('08 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE VENDAS')

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
codigo_venda_final = 100 #43209

#for pessoa in dfPessoas.index:

while codigo_venda_final > 0:

    print('codigo_venda_final: ' + str(codigo_venda_final))
    
    data_inicio = pd.to_datetime('2017-01-02')
    data_fim = pd.to_datetime(date.today().isoformat())

    pessoa = int(np.random.choice(dfPessoas.index, size = 1 , replace=False))
    indice_randomico_vendedor = int(np.random.choice(dfVendedor.index, size = 1 , replace=False))
    indice_randomico_forma_pagamento = int(np.random.choice(dfFormaPagamento.index, size = 1 , replace=False))    
    indice_randomico_loja = int(np.random.choice(dfLoja.index, size = 1 , replace=False))    

    v_vendedor = dfVendedor['NOME_VENDEDOR'][indice_randomico_vendedor]
    v_codigo_vendedor = dfVendedor['CODIGO_VENDEDOR'][indice_randomico_vendedor]

    v_codigo_loja = dfLoja['CODIGO_LOJA'][indice_randomico_loja]
    v_loja = dfLoja['NOME_LOJA'][indice_randomico_loja]
    v_lojalocalidade = dfLoja['LOCALIDADE_LOJA'][indice_randomico_loja]   
    v_lojatipo = dfLoja['TIPO_LOJA'][indice_randomico_loja]       
    v_formaPagamento = dfFormaPagamento['DESCRICAO_FORMA_PAGAMENTO'][indice_randomico_forma_pagamento]
    v_codigo_formaPagamento = dfFormaPagamento['CODIGO_FORMA_PAGAMENTO'][indice_randomico_forma_pagamento]

    v_pessoa = dfPessoas['NOME_CLIENTE'][pessoa]
    v_codigo_cliente = dfPessoas['CODIGO_CLIENTE'][pessoa]

    indice_randomico = np.random.choice(dfProdutos.index, size = random.randint(1, 10) , replace=False)    
    
    p_data_venda = pd.to_datetime(np.random.uniform(data_inicio.value, data_fim.value, size=365))


    if v_codigo_loja == 1:

        v_data_venda = p_data_venda[0].strftime("%Y-%m-%d %H:%M:%S")
    
    elif v_codigo_loja != 1:

        hora = int(random.uniform(9, 18))
        minuto = int(random.uniform(0, 59))
        segundo = int(random.uniform(0, 59))

        data = str(p_data_venda[0].year) + '-' + str(p_data_venda[0].month).zfill(2) + '-' + str(p_data_venda[0].day).zfill(2) + ' ' + str(hora).zfill(2) + ':' + str(minuto).zfill(2) + ':' + str(segundo).zfill(2)

        v_data_venda = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

    for i in indice_randomico:

        if dfProdutos['CODIGO_CATEGORIA'][i] == 3: #'Whisky':

            valor_min = 89.98
            valor_max = 179.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 1: #'Vodka':

            valor_min = 35.99
            valor_max = 99.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 4: #'Refrigerante':

            valor_min = 6.00
            valor_max = 9.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 2: #'Rum':

            valor_min = 69.00
            valor_max = 99.99

            valor = np.random.uniform(valor_min, valor_max, size=1)

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 6: #'Champagne':

            valor_min = 115.00
            valor_max = 159.99

            valor = np.random.uniform(valor_min, valor_max, size=1)            

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 5: #'Gin':

            valor_min = 99.00
            valor_max = 119.99

            valor = np.random.uniform(valor_min, valor_max, size=1)    

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 10: #'Verduras e Legumes':

            valor_min = 0.99
            valor_max = 5.99

            valor = np.random.uniform(valor_min, valor_max, size=1)    

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 7: #'Carne Boi':

            valor_min = 29.99
            valor_max = 75.99

            valor = np.random.uniform(valor_min, valor_max, size=1) 

        elif dfProdutos['CODIGO_CATEGORIA'][i] == 9: #'Carne Frango':

            valor_min = 14.99
            valor_max = 29.99

            valor = np.random.uniform(valor_min, valor_max, size=1) 

        elif dfProdutos['CODIGO_CATEGORIA'][i] ==  8: #'Carne Peixe':

            valor_min = 29.99
            valor_max = 85.99

            valor = np.random.uniform(valor_min, valor_max, size=1)             

        else:

            valor_min = 0.99
            valor_max = 7.99

            valor = np.random.uniform(valor_min, valor_max, size=1)            

        v_quantidade = int(np.random.randint(1, 10, size=1))

        v_produto = dfProdutos['DESCRICAO_PRODUTO'][i]
        v_codigo_produto = dfProdutos['CODIGO_PRODUTO'][i]
        v_tipo_produto = dfProdutos['CODIGO_CATEGORIA'][i]

        tipo_pagamento = int(np.random.randint(1, 4, size=1))

        if tipo_pagamento == 3:

            v_tipo_pagamento = 'PARCELADO'

        else:

            v_tipo_pagamento = 'A VISTA'
        
        dados = [{ 'CODIGO_VENDA' : codigo_venda_inicial
                    ,'DATA_VENDA': str(v_data_venda)
                    ,'CODIGO_CLIENTE': v_codigo_cliente
                    ,'NOME_CLIENTE': v_pessoa
                    ,'CODIGO_PRODUTO' : v_codigo_produto
                    ,'DESCRICAO_PRODUTO' : v_produto
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

    codigo_venda_final = codigo_venda_final - 1

print('08 (FIM) - PROCESSO GERAÇÃO DE DADOS DE VENDAS')

# %%

print('09 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE VENDAS')

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

dfVenda.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\06_vendas.csv'
                  ,sep=';'
                  ,header=True
                  ,index=False)

print('09 (FIM) - PROCESSO GERAÇÃO DE DADOS DE VENDAS')

# %%

print('10 (INICIO) - PROCESSO GERAÇÃO DE DADOS DE ITENS DE VENDAS')

dfItemVenda = (dfFinal.groupby(['CODIGO_VENDA', 'CODIGO_PRODUTO'], as_index=False)
                .agg(VALOR_UNITARIO=('VALOR_UNITARIO','sum')
                     ,QUANTIDADE=('QUANTIDADE','sum')
                     ,VALOR_FINAL=('VALOR_FINAL','sum'))
                     .sort_values(by=['CODIGO_VENDA', 'CODIGO_PRODUTO'])
                     .reset_index(drop=True))

dfItemVenda.to_csv(fr'C:\Temp\Python_YT\Git\Projeto_BI_Zero_TO_DW\01_SCRIPT_SQL\DADOS_BASE\07_item_vendas.csv'
                  ,sep=';'  
                  ,header=True
                  ,index=False)

print('10 (FIM) - PROCESSO GERAÇÃO DE DADOS DE ITENS DE VENDAS')

# %%

print('00 (FIM) - TERMINO PROCESSO DE CARGA DADOS')


# %%
