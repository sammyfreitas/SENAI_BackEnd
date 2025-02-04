--0 - crie um outro banco de dados para fazer a prova.
create database teste_backend;

--1- criar duas tabelas cliente e produto
--Atributos:
--tabela cliente(nome , cpf , idcliente PK e autoIncremente, email , endereco , ativo_SN char(1)).
--produto(idPorduto PK e autoIncremente, nomeProduto,preco_produto ,  validade DATE, tamanho).
  
 create table cliente (
    idcliente int auto_increment primary key,
    nome varchar(150) not null,
    cpf varchar(14) not null,
    email varchar(150) not null,
    endereco varchar(250) not null,
	bairro varchar(100) not null, 
	cidade varchar(150) not null, 
	estado varchar(2) not null, 
	cep varchar(9) not null,
	ativo_SN char(1) not null
);
 
 CREATE TABLE produto (
    idProduto int auto_increment primary key,
    nomeProduto varchar(150) not null,
    preco_produto decimal (10,2) not null,
    validade date not null,
    tamanho varchar(50) not null
);
 
--2 - prencher com 7 clientes e com 7 produtos (ativo sn : (0 / 1) ,  idcliente: (50 / 100))

alter table cliente auto_increment = 50;

insert into cliente (nome, cpf, email, endereco, bairro, cidade, estado, cep, ativo_SN) values
  ('Anthony Freitas', '123.456.789-00', 'anthony.freitas@gmail.com', 'Rua Des Izidro, 100','Tijuca', 'Rio de Janeiro', 'RJ', 20000-000, '1'),
  ('Guilherme Neves', '987.654.321-00', 'guilherme.freitas@gmail.com', 'Rua Lins de Vasconcelos, 200','Engenho Novo', 'Rio de Janeiro', 'RJ', 20000-001, '0'),
  ('Willian Peng', '111.222.333-00', 'willian.peng@gmail.com', 'Rua Henry Ford, 300','Tijuca', 'Rio de Janeiro', 'RJ', 20000-002, '1'),
  ('Patricia Nedina', '444.555.666-00', 'patricia.nedina@gmail.com', 'Rua Gastão Baiana, 400','Copacabana', 'Rio de Janeiro', 'RJ', 20000-003, '0'),
  ('Fabiano Xavier', '777.888.999-00', 'fabiano.xavier@gmail.com', 'Rua Ary Parreiras, 500','Icaraí', 'Niteroi', 'RJ', 20000-004, '1'),
  ('Glauco Carvalho', '222.333.444-00', 'glauco.carvalho@gmail.com', 'Rua Catete, 600','Catete', 'Rio de Janeiro', 'RJ', 20000-005, '0'),
  ('Luis Augusto', '555.666.777-00', 'luis.augusto@gmail.com', 'Rua Miguel Lemos, 700','Copacabana', 'Rio de Janeiro', 'RJ', 20000-000, '1'),

insert into produto (nomeProduto, preco_produto, validade, tamanho) values
  ('Bolo de Chocolate', 39.99, '2023-12-31', '800g'),
  ('Bala Juquinha', 17.99, '2024-06-30', '1kg'),
  ('H2O Limoneto', 6.99, '2025-01-31', '600ml'),
  ('Paçoca', 1.99, '2023-12-31', '15g'),
  ('Chocolate Talento', 8.99, '2026-12-31', '90g'),
  ('Chocolate Caribe', 3.49, '2025-06-30', '28g'),
  ('Pacote Bombom Ouro Branco', 54.99, '2024-12-31', '1Kg');

--3- selecione quantos idcliente esta entre 50 e 75 
--select * from cliente where idcliente >= 50 and idcliente <= 75
select count(*) as qtd_clientes from cliente where idcliente >= 50 and idcliente <= 75;

--4 - conta quantos clientes estao com o ativo 0 
select count(*) as qtd_clientes_inativos from cliente where ativo_SN = '0';

---5- quantos produtos custam mais que a media 
select count (*) as qtd_produtos_acima_media from produto where (preco_produto > (avg(preco_produto));

-- 7- quantos produtos custam menos que a media 
select count (*) as qtd_produtos_abaixo_media from produto where (preco_produto < (avg(preco_produto));

--8- a soma dos preços de todos os produtos 
select sum(preco_produto) as soma_precos_produtos from produto;

--9 - adicione na tabela cliente o registo telefone e ao produto o registro embalagem e preenche. 
alter table cliente add column telefone varchar(14);
alter table produto add column embalagem varchar(50);

update cliente set telefone = '(21) 2345-6789' where idcliente = 50;
update cliente set telefone = '(21) 2345-6790' where idcliente = 51;
update cliente set telefone = '(21) 2345-6791' where idcliente = 52;
update cliente set telefone = '(21) 2345-6792' where idcliente = 53;
update cliente set telefone = '(21) 2345-6793' where idcliente = 54;
update cliente set telefone = '(21) 2345-6794' where idcliente = 55;
update cliente set telefone = '(21) 2345-6795' where idcliente = 56;

update produto set embalagem = 'Caixa de papelão' where idProduto = 1;
update produto set embalagem = 'Pacote' where idProduto = 2;
update produto set embalagem = 'Garrafa' where idProduto = 3;
update produto set embalagem = 'Papel Metalizado' where idProduto = 4;
update produto set embalagem = 'Papel Metalizado' where idProduto = 5;
update produto set embalagem = 'Papel Metalizado' where idProduto = 6;
update produto set embalagem = 'Pacote' where idProduto = 7;

--10 - mostre na tela o nome e o preço do produto mais caro e outro do mais barato 
select nomeProduto, preco_produto from produto where preco_produto = max(preco_produto) from produto;
select nomeProduto, preco_produto from produto where preco_produto = min(preco_produto) from produto;

--11 - ordene a tabela cliente por ordem decrescente no campo nome
select * from cliente order by nome desc;

--12 -  busque na tabela o nome dos clientes que estao ativo 
select * from cliente where ativo_SN = '1';

--13-  busque os nomes dos clientes que comecem com a letra A e termine com a letra O
select nome from cliente where nome like 'A%O';