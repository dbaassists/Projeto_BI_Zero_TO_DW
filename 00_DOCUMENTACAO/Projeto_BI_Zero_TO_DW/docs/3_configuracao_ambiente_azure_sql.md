# Projeto BI Zero TO DW

## 3 - Configurando o Ambiente Azure SQL Database

Essa etapa é responsável pela criação das tabelas no banco Azure SQL Database.

### SEQ-3.1 - Tabelas Azure SQL Database.

Pré-Requisito para criação da estrutura do Azure SQL Database.

|Sequência|Ação|Detalhamento
|---|---|---|
|SEQ-2.1|Provisionamento do Azure SQL|Provisionamento de um banco de dados no Azure|

| Banco de Dados | Schema | Tabela | Descrição |
| ------ |  ------ |  ------ |  ------ |
| srv-db-treinamentosql | dbo | TB_FORMA_PAGAMENTO | Armazena informações de forma de pagamento. |
| srv-db-treinamentosql | dbo | TB_CATEGORIA_PRODUTO | Armazena informações das categorias dos produtos |
| srv-db-treinamentosql | dbo | TB_PRODUTO | Armazena informações de produtos. |
| srv-db-treinamentosql | dbo | TB_CLIENTE | Armazena informações de clientes. |
| srv-db-treinamentosql | dbo | TB_VENDEDOR | Armazena informações de vendedores. |
| srv-db-treinamentosql | dbo | TB_LOJA | Armazena informações de lojas. |
| srv-db-treinamentosql | dbo | TB_VENDA | Armazenada informações de vendas. |
| srv-db-treinamentosql | dbo | TB_ITEM_VENDA | Armazena informações sobre os itens que foram vendidos. |

### SEQ-3.2 - Modelo de Dados

#### 3.2.1 - Diagrama de Dados Gerado no SSMS

![Image](./imagens/02_modelo_dados.png)


#### 3.2.2 - Modelo de Dados Gerado no Toad Data Modeler

![Image](./imagens/09_modelo_dados.png)

### SEQ-3.3 - Script CREATE TABLE

Esse script pode ser encontrado em: [Script de Criação de Tabelas](https://github.com/dbaassists/Projeto_BI_Zero_TO_DW/blob/main/01_SCRIPT_SQL/00_CREATE_TABLE.sql)

``` {.sql title="Script Para Criar Tabelas no SQL" linenums=1}
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDEDOR', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDEDOR', N'COLUMN',N'NOME_VENDEDOR'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR', @level2type=N'COLUMN',@level2name=N'NOME_VENDEDOR'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDEDOR', N'COLUMN',N'CODIGO_VENDEDOR'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDEDOR'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'TIPO_PAGAMENTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'TIPO_PAGAMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'VALOR_FINAL'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_FINAL'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'DATA_VENDA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'DATA_VENDA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'CODIGO_FORMA_PAGAMENTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_FORMA_PAGAMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'CODIGO_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_VENDA', N'COLUMN',N'CODIGO_VENDA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_PRODUTO', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_PRODUTO', N'COLUMN',N'CODIGO_CATEGORIA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_CATEGORIA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_PRODUTO', N'COLUMN',N'DESCRICAO_PRODUTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'DESCRICAO_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_PRODUTO', N'COLUMN',N'CODIGO_PRODUTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_LOJA', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_LOJA', N'COLUMN',N'TIPO_LOJA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'TIPO_LOJA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_LOJA', N'COLUMN',N'LOCALIDADE_LOJA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'LOCALIDADE_LOJA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_LOJA', N'COLUMN',N'NOME_LOJA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'NOME_LOJA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_LOJA', N'COLUMN',N'CODIGO_LOJA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'CODIGO_LOJA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', N'COLUMN',N'VALOR_FINAL'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_FINAL'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', N'COLUMN',N'QUANTIDADE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'QUANTIDADE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', N'COLUMN',N'VALOR_UNITARIO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_UNITARIO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', N'COLUMN',N'CODIGO_PRODUTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_ITEM_VENDA', N'COLUMN',N'CODIGO_VENDA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDA'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_FORMA_PAGAMENTO', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_FORMA_PAGAMENTO', N'COLUMN',N'DESCRICAO_FORMA_PAGAMENTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO', @level2type=N'COLUMN',@level2name=N'DESCRICAO_FORMA_PAGAMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_FORMA_PAGAMENTO', N'COLUMN',N'CODIGO_FORMA_PAGAMENTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO', @level2type=N'COLUMN',@level2name=N'CODIGO_FORMA_PAGAMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'OCUPACAO_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'OCUPACAO_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'EMAIL_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'EMAIL_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'NUMERO_TELEFONE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NUMERO_TELEFONE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'NOME_CIDADE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NOME_CIDADE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'NUMERO_ENDERECO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NUMERO_ENDERECO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'DESCRICAO_ENDERECO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'DESCRICAO_ENDERECO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'IDADE_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'IDADE_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'DATA_NASCIMENTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'DATA_NASCIMENTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'NOME_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NOME_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CLIENTE', N'COLUMN',N'CODIGO_CLIENTE'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'CODIGO_CLIENTE'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CATEGORIA_PRODUTO', NULL,NULL))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CATEGORIA_PRODUTO', N'COLUMN',N'SUB_CATEGORIA_PRODUTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'SUB_CATEGORIA_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CATEGORIA_PRODUTO', N'COLUMN',N'CATEGORIA_PRODUTO'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'CATEGORIA_PRODUTO'
GO
IF  EXISTS (SELECT * FROM sys.fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'TB_CATEGORIA_PRODUTO', N'COLUMN',N'CODIGO_CATEGORIA'))
EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_CATEGORIA'
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_VENDA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_VENDA] DROP CONSTRAINT IF EXISTS [FK_TB_VENDA_LOJA_VENDEDOR]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_VENDA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_VENDA] DROP CONSTRAINT IF EXISTS [FK_TB_VENDA_FORMA_PAGAMENTO]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_VENDA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_VENDA] DROP CONSTRAINT IF EXISTS [FK_TB_VENDA_CLIENTE]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_PRODUTO]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_PRODUTO] DROP CONSTRAINT IF EXISTS [FK_TB_PRODUTO_CATEGORIA_PRODUTO]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_LOJA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_LOJA] DROP CONSTRAINT IF EXISTS [FK_TB_VENDEDOR_LOJA]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_ITEM_VENDA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_ITEM_VENDA] DROP CONSTRAINT IF EXISTS [FK_TB_VENDA_ITEM_VENDA]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TB_ITEM_VENDA]') AND type in (N'U'))
ALTER TABLE [dbo].[TB_ITEM_VENDA] DROP CONSTRAINT IF EXISTS [FK_TB_ITEM_VENDA_PRODUTO]
GO
/****** Object:  Index [IX_02]    Script Date: 30/01/2024 16:00:29 ******/
DROP INDEX IF EXISTS [IX_02] ON [dbo].[TB_VENDA]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
DROP INDEX IF EXISTS [IX_01] ON [dbo].[TB_VENDA]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
DROP INDEX IF EXISTS [IX_01] ON [dbo].[TB_PRODUTO]
GO
/****** Object:  Index [IX_02]    Script Date: 30/01/2024 16:00:29 ******/
DROP INDEX IF EXISTS [IX_02] ON [dbo].[TB_ITEM_VENDA]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
DROP INDEX IF EXISTS [IX_01] ON [dbo].[TB_ITEM_VENDA]
GO
/****** Object:  Table [dbo].[TB_VENDEDOR]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_VENDEDOR]
GO
/****** Object:  Table [dbo].[TB_VENDA]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_VENDA]
GO
/****** Object:  Table [dbo].[TB_PRODUTO]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_PRODUTO]
GO
/****** Object:  Table [dbo].[TB_LOJA]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_LOJA]
GO
/****** Object:  Table [dbo].[TB_ITEM_VENDA]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_ITEM_VENDA]
GO
/****** Object:  Table [dbo].[TB_FORMA_PAGAMENTO]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_FORMA_PAGAMENTO]
GO
/****** Object:  Table [dbo].[TB_CLIENTE]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_CLIENTE]
GO
/****** Object:  Table [dbo].[TB_CATEGORIA_PRODUTO]    Script Date: 30/01/2024 16:00:29 ******/
DROP TABLE IF EXISTS [dbo].[TB_CATEGORIA_PRODUTO]
GO
/****** Object:  Table [dbo].[TB_CATEGORIA_PRODUTO]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_CATEGORIA_PRODUTO](
	[CODIGO_CATEGORIA] [smallint] IDENTITY(1,1) NOT NULL,
	[CATEGORIA_PRODUTO] [varchar](100) NOT NULL,
	[SUB_CATEGORIA_PRODUTO] [varchar](100) NOT NULL,
 CONSTRAINT [PK_TB_CATEGORIA_PRODUTO] PRIMARY KEY CLUSTERED 
(
	[CODIGO_CATEGORIA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_CLIENTE]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_CLIENTE](
	[CODIGO_CLIENTE] [int] IDENTITY(1,1) NOT NULL,
	[NOME_CLIENTE] [varchar](100) NOT NULL,
	[DATA_NASCIMENTO] [date] NOT NULL,
	[IDADE_CLIENTE] [tinyint] NOT NULL,
	[DESCRICAO_ENDERECO] [varchar](200) NOT NULL,
	[NUMERO_ENDERECO] [smallint] NOT NULL,
	[NOME_CIDADE] [varchar](100) NOT NULL,
	[NUMERO_TELEFONE] [varchar](30) NOT NULL,
	[EMAIL_CLIENTE] [varchar](100) NOT NULL,
	[OCUPACAO_CLIENTE] [varchar](100) NOT NULL,
 CONSTRAINT [PK_TB_CLIENTE] PRIMARY KEY CLUSTERED 
(
	[CODIGO_CLIENTE] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_FORMA_PAGAMENTO]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_FORMA_PAGAMENTO](
	[CODIGO_FORMA_PAGAMENTO] [smallint] IDENTITY(1,1) NOT NULL,
	[DESCRICAO_FORMA_PAGAMENTO] [varchar](100) NOT NULL,
 CONSTRAINT [PK_TB_FORMA_PAGAMENTO] PRIMARY KEY CLUSTERED 
(
	[CODIGO_FORMA_PAGAMENTO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_ITEM_VENDA]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_ITEM_VENDA](
	[CODIGO_VENDA] [int] NOT NULL,
	[CODIGO_PRODUTO] [smallint] NOT NULL,
	[VALOR_UNITARIO] [decimal](18, 2) NULL,
	[QUANTIDADE] [smallint] NULL,
	[VALOR_FINAL] [decimal](18, 2) NULL,
 CONSTRAINT [PK_TB_ITEM_VENDA] PRIMARY KEY CLUSTERED 
(
	[CODIGO_VENDA] ASC,
	[CODIGO_PRODUTO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_LOJA]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_LOJA](
	[CODIGO_LOJA_VENDEDOR] [smallint] IDENTITY(1,1) NOT NULL,
	[CODIGO_LOJA] [smallint] NOT NULL,
	[CODIGO_VENDEDOR] [smallint] NOT NULL,
	[NOME_LOJA] [varchar](100) NOT NULL,
	[LOCALIDADE_LOJA] [varchar](100) NOT NULL,
	[TIPO_LOJA] [varchar](100) NOT NULL,
 CONSTRAINT [PK_TB_LOJA] PRIMARY KEY CLUSTERED 
(
	[CODIGO_LOJA_VENDEDOR] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_PRODUTO]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_PRODUTO](
	[CODIGO_PRODUTO] [smallint] IDENTITY(1,1) NOT NULL,
	[DESCRICAO_PRODUTO] [varchar](100) NOT NULL,
	[CODIGO_CATEGORIA] [smallint] NOT NULL,
 CONSTRAINT [PK_TB_PRODUTO] PRIMARY KEY CLUSTERED 
(
	[CODIGO_PRODUTO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_VENDA]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_VENDA](
	[CODIGO_VENDA] [int] IDENTITY(1,1) NOT NULL,
	[CODIGO_CLIENTE] [int] NOT NULL,
	[CODIGO_FORMA_PAGAMENTO] [smallint] NOT NULL,
	[CODIGO_LOJA_VENDEDOR] [smallint] NOT NULL,
	[DATA_VENDA] [datetime] NOT NULL,
	[VALOR_FINAL] [decimal](18, 2) NOT NULL,
	[TIPO_PAGAMENTO] [varchar](100) NOT NULL,
 CONSTRAINT [PK_TB_VENDA] PRIMARY KEY CLUSTERED 
(
	[CODIGO_VENDA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TB_VENDEDOR]    Script Date: 30/01/2024 16:00:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TB_VENDEDOR](
	[CODIGO_VENDEDOR] [smallint] IDENTITY(1,1) NOT NULL,
	[NOME_VENDEDOR] [varchar](100) NOT NULL,
 CONSTRAINT [PK_CODIGO_VENDEDOR] PRIMARY KEY CLUSTERED 
(
	[CODIGO_VENDEDOR] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
CREATE NONCLUSTERED INDEX [IX_01] ON [dbo].[TB_ITEM_VENDA]
(
	[CODIGO_VENDA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_02]    Script Date: 30/01/2024 16:00:29 ******/
CREATE NONCLUSTERED INDEX [IX_02] ON [dbo].[TB_ITEM_VENDA]
(
	[CODIGO_PRODUTO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
CREATE NONCLUSTERED INDEX [IX_01] ON [dbo].[TB_PRODUTO]
(
	[CODIGO_CATEGORIA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_01]    Script Date: 30/01/2024 16:00:29 ******/
CREATE NONCLUSTERED INDEX [IX_01] ON [dbo].[TB_VENDA]
(
	[CODIGO_CLIENTE] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_02]    Script Date: 30/01/2024 16:00:29 ******/
CREATE NONCLUSTERED INDEX [IX_02] ON [dbo].[TB_VENDA]
(
	[CODIGO_FORMA_PAGAMENTO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[TB_ITEM_VENDA]  WITH CHECK ADD  CONSTRAINT [FK_TB_ITEM_VENDA_PRODUTO] FOREIGN KEY([CODIGO_PRODUTO])
REFERENCES [dbo].[TB_PRODUTO] ([CODIGO_PRODUTO])
GO
ALTER TABLE [dbo].[TB_ITEM_VENDA] CHECK CONSTRAINT [FK_TB_ITEM_VENDA_PRODUTO]
GO
ALTER TABLE [dbo].[TB_ITEM_VENDA]  WITH CHECK ADD  CONSTRAINT [FK_TB_VENDA_ITEM_VENDA] FOREIGN KEY([CODIGO_VENDA])
REFERENCES [dbo].[TB_VENDA] ([CODIGO_VENDA])
GO
ALTER TABLE [dbo].[TB_ITEM_VENDA] CHECK CONSTRAINT [FK_TB_VENDA_ITEM_VENDA]
GO
ALTER TABLE [dbo].[TB_LOJA]  WITH CHECK ADD  CONSTRAINT [FK_TB_VENDEDOR_LOJA] FOREIGN KEY([CODIGO_VENDEDOR])
REFERENCES [dbo].[TB_VENDEDOR] ([CODIGO_VENDEDOR])
GO
ALTER TABLE [dbo].[TB_LOJA] CHECK CONSTRAINT [FK_TB_VENDEDOR_LOJA]
GO
ALTER TABLE [dbo].[TB_PRODUTO]  WITH CHECK ADD  CONSTRAINT [FK_TB_PRODUTO_CATEGORIA_PRODUTO] FOREIGN KEY([CODIGO_CATEGORIA])
REFERENCES [dbo].[TB_CATEGORIA_PRODUTO] ([CODIGO_CATEGORIA])
GO
ALTER TABLE [dbo].[TB_PRODUTO] CHECK CONSTRAINT [FK_TB_PRODUTO_CATEGORIA_PRODUTO]
GO
ALTER TABLE [dbo].[TB_VENDA]  WITH CHECK ADD  CONSTRAINT [FK_TB_VENDA_CLIENTE] FOREIGN KEY([CODIGO_CLIENTE])
REFERENCES [dbo].[TB_CLIENTE] ([CODIGO_CLIENTE])
GO
ALTER TABLE [dbo].[TB_VENDA] CHECK CONSTRAINT [FK_TB_VENDA_CLIENTE]
GO
ALTER TABLE [dbo].[TB_VENDA]  WITH CHECK ADD  CONSTRAINT [FK_TB_VENDA_FORMA_PAGAMENTO] FOREIGN KEY([CODIGO_FORMA_PAGAMENTO])
REFERENCES [dbo].[TB_FORMA_PAGAMENTO] ([CODIGO_FORMA_PAGAMENTO])
GO
ALTER TABLE [dbo].[TB_VENDA] CHECK CONSTRAINT [FK_TB_VENDA_FORMA_PAGAMENTO]
GO
ALTER TABLE [dbo].[TB_VENDA]  WITH CHECK ADD  CONSTRAINT [FK_TB_VENDA_LOJA_VENDEDOR] FOREIGN KEY([CODIGO_LOJA_VENDEDOR])
REFERENCES [dbo].[TB_LOJA] ([CODIGO_LOJA_VENDEDOR])
GO
ALTER TABLE [dbo].[TB_VENDA] CHECK CONSTRAINT [FK_TB_VENDA_LOJA_VENDEDOR]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código da Categoria do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_CATEGORIA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Descrição da Categoria do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'CATEGORIA_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Descrição da Sub-Categoria do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO', @level2type=N'COLUMN',@level2name=N'SUB_CATEGORIA_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações das categorias dos produtos' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CATEGORIA_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código do Cliente.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'CODIGO_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Nome do Cliente.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NOME_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Data de Nascimento do Cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'DATA_NASCIMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Idade do Cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'IDADE_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Endereço do Cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'DESCRICAO_ENDERECO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Número do Endereço' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NUMERO_ENDERECO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Cidade' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NOME_CIDADE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Telefone' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'NUMERO_TELEFONE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'E-mail do cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'EMAIL_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Ocupação do Cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE', @level2type=N'COLUMN',@level2name=N'OCUPACAO_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações de clientes.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO', @level2type=N'COLUMN',@level2name=N'CODIGO_FORMA_PAGAMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Descrição da Forma de Pagamento na Tabela TB_FORMA_PAGAMENTO.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO', @level2type=N'COLUMN',@level2name=N'DESCRICAO_FORMA_PAGAMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações de forma de pagamento.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_FORMA_PAGAMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código da Venda' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código do Produto' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Valor Unitário do Produto' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_UNITARIO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Quantidade do Produto Vendido' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'QUANTIDADE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Valor Final do Produto Vendido' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_FINAL'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações sobre os itens que foram vendidos.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_ITEM_VENDA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código da Loja.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'CODIGO_LOJA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Nome da Loja.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'NOME_LOJA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Localidade da Loja.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'LOCALIDADE_LOJA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Tipo da Loja.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA', @level2type=N'COLUMN',@level2name=N'TIPO_LOJA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações de lojas.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_LOJA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Descrição do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'DESCRICAO_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Categoria do Produto.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO', @level2type=N'COLUMN',@level2name=N'CODIGO_CATEGORIA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações de produtos.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_PRODUTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código da Venda.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código do Cliente' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_CLIENTE'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Forma de Pagamento' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'CODIGO_FORMA_PAGAMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Data da Venda' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'DATA_VENDA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Valor Total da Venda' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'VALOR_FINAL'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Tipo de Pagamento' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA', @level2type=N'COLUMN',@level2name=N'TIPO_PAGAMENTO'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazenada informações de vendas.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDA'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Código do Vendedor.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR', @level2type=N'COLUMN',@level2name=N'CODIGO_VENDEDOR'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Nome do Vendedor.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR', @level2type=N'COLUMN',@level2name=N'NOME_VENDEDOR'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Armazena informações de vendedores' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'TB_VENDEDOR'
GO
```