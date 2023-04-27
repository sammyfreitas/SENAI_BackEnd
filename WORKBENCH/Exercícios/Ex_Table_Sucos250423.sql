create database sucos;
use sucos;
create table tbcliente -- Cria a tabela tbcliente
	(
	CPF varchar(11),
    nome varchar(100),
    endereço varchar(150),
    bairro varchar(50),
    cidade varchar(50),
    estado varchar(2),
    cep varchar (9),
    idade smallint,
    limite_credito float,
    volume_compra float,
    primeira_compra bit(1)
	);
create table tbproduto -- Cria a tabela tbproduto
	(
	codigo_produto varchar(20),
	nome_produto varchar(150),
	embalagem varchar(50),
	tamanho varchar (50),
	sabor varchar (50),
	preco_listas float
	);
    
insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1037797','Clean - 2 Litros - laranja', 'pet', '2 litros', 'laranja', 16.01); -- Insere dados na tabela tbproduto
insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1000889', 'Sabor da Montanha - 700ml - Uva', 'garrafa',  '700ml',  'uva',  6.31); -- Insere dados na tabela tbproduto
insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1004327', 'Videira do Campo - 1,5 Litros - Melancia', 'PET', '1,5 l', 'Melancia', 19.51); -- Insere dados na tabela tbproduto

select * from tbproduto where nome_produto like 'C%';
select embalagem, nome_produto from tbproduto where nome_produto like 'C%';
select embalagem, nome_produto from tbproduto where nome_produto like 'P_';
select embalagem, nome_produto from tbproduto where nome_produto like 'G_';
select embalagem, nome_produto from tbproduto where nome_produto like '_E_';
select embalagem, nome_produto from tbproduto where nome_produto like '_T';
select * from tbproduto;
select * from tbproduto where tamanha like '_l_';
--update tbproduto set tamanho = 1,5 litros where sabor like 'melancia';
update tbproduto set tamanho = 700ml where sabor like 'u_';
update tbproduto set embalagem = PET where sabor like 'l_';
select * from tbproduto;





select * from tbproduto;
delete from tbproduto where embalagem like 'pet';
select * from tbproduto;
update tbproduto set nome_produto = "Sabor da Montanha - 700ml - Uva" where codigo_produto like 1000889;
select * from tbproduto;






select * from tbproduto;
delete from tbproduto where embalagem like 'pet';
select * from tbproduto;
update tbproduto set nome_produto = "Sabor da Montanha - 700ml - Uva" where codigo_produto like 1000889;

insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1004327', 'Videira do Campo - 1,5 Litros - Melancia', 'PET', '1,5 l', 'Melancia', 19.51); -- Insere dados na tabela tbproduto
insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1037797','Clean - 2 Litros - Laranja', 'PET', '2 litros', 'Laranja', 16.01); -- Insere dados na tabela tbproduto
update tbproduto set sabor = "Uva" where codigo_produto like 1000889;
update tbproduto set tamanho = '1,5 litros' where codigo_produto like 1004327;
update tbproduto set tamanho = '2,0 litros' where codigo_produto like 1037797;

select * from tbproduto;



















