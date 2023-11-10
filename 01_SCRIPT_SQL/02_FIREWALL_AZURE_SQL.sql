
-- Listando as Regras Criadas 

SELECT * 
FROM sys. firewall_rules

-- Adicionando um IP na Regra

exec sp_set_firewall_rule N'nome_regra', '0.0.0.0', '0.0.0.0'

-- Removendo um IP da Regra

exec sp_delete_firewall_rule N'nome_regra'

