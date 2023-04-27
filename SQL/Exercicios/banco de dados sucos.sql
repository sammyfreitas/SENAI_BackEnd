create database sucos; -- Cria o banco de dados sucos
use sucos; -- Informa ao BD que os comandos a seguir serão para o banco de dados escolhido

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

drop table tbcliente; --Exclui a tabela e todos os dados

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

insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1000889', 'Sabor da Montanha - 700ml - uva', 'garrafa',  '700ml',  'uva',  6.31); -- Insere dados na tabela tbproduto
	
insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1004327', 'Videira do Campo - 1,5 Litros - Melancia', 'PET', '1,5 l', 'melancia', 19.51); -- Insere dados na tabela tbproduto

insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1037797', 'Clean - 2 Litros - Melancia', 'PET', '1,5 l', 'uva', 6.31); -- Insere dados na tabela tbproduto

insert into tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_listas) values ('1000889', 'Sabor da Montanha - 700ml - uva', 'garrafa',  '700ml',  'uva',  6.31); -- Insere dados na tabela tbproduto

select * from tbproduto; -- Seleciona todos os dados da tabela tbproduto e exibe