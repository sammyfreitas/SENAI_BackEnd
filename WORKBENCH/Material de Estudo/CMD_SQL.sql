--SQL SCRIPTS

--CRIANDO BANCO DE DADOS
create database bd_teste;

--CRIANDO TABELAS
create table <nome_tabela>(
	cpf varchar (11),
	nome  varchar (100),
	endereco varchar (500),
	cidade varchar (150),
	pais varchar (150),
	cep varchar (9),
	salario float (
	...
	);
	
--DELETANDO TABELAS
drop table tbClientes;

--INSERINDO DADOS NA TABELA
insert into tbClientes(cpf,nome) values ('125789463','Joao');

--Sintaxe básica Delete
delete *
from tbClientes
where critério

--Sintaxe básica Consulta
select [distinct] expressao [as nome-atributo]
[from lista]
[where condicao]
[order by attr_name1 [ASC | DESC ]]
--onde: DISTINCT: Elimina linhas duplicadas na seleção

--Sintaxe básica Consulta
select count(*) from funcionarios;
select * from cidadao order by nome DESC;

--25/04/23
--Ordenação de dados Crescente
select * from tbproduto order by NOME_PRODUTO asc;

--Ordenação de dados Decrescente
select * from tbproduto order by NOME_PRODUTO desc;

--Criando campo novo na tabela
alter table tbproduto add Email varchar(100);

--Excluindo campo da tabela
alter table tbproduto drop column Email;

--Alterando dados
update tbproduto set embalagem = 'Vidro' where codigo_produto = '10000889';

--Exercicio
--Tabela cliente - inserir 7 registros e mais a coluna email


insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('111111111-11','Anthony Freitas','Rua Des Izidro 114','Tijuca','Rio de Janeiro','RJ','20000-000',40,50000,12000,'N');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('222222222-22','Bruna Vianna','Rua Henry Ford 10','Tijuca','Rio de Janeiro','RJ','20000-000',28,30000,10000,'S');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('333333333-33','Willian Peng','Rua General Roca 20','Tijuca','Rio de Janeiro','RJ','20000-000',17,2000,200,'S');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('444444444-44','Guilherme Neves','Rua Lins de Vasconcelos, 30','Lins','Rio de Janeiro','RJ','20000-000',21,500,120,'N');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('555555555-55','Bruno Melo','Rua Sao Francisco Xavier 200','Tijuca','Rio de Janeiro','RJ','20000-000',30,52000,1800,'S');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('666666666-66','Alan','Rua Barao do Bom Retiro 100','Engenho Novo','Rio de Janeiro','RJ','20000-000',33,20000,16000,'N');
insert into tbcliente (CPF,nome,endereco,bairro,cidade,estado,cep,idade,limite_credito,volume_compra,primeira_compra) values ('777777777-77','Victor','Rua Des Izidro 114','Jacarepagua','Rio de Janeiro','RJ','20000-000',25,120000,1000,'S');
alter table tbcliente add Email varchar(100);



