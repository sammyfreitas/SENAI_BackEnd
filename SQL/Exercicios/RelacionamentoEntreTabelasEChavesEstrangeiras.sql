# criando os relacionamentos entre tabelas e as chaves estrangeiras. 
# referencia venderoes - vendas 
alter table VENDEDORES add constraint CE_VENDEDORES_VENDAS
foreign key (ID_VENDEDOR) references VENDAS (ID_VENDEDOR)
ON DELETE NO action
ON update NO ACTION;
