Exercícios:

1) Criar uma tabela para uma empresa com os dados: nome, rg, cpf, dpto, supervisor, salario, funcao
create table tbfuncionarios(
	cpf varchar (12) [NOT NULL],
	nome  varchar (150) [NOT NULL],
	rg varchar (10) [NOT NULL],
	dpto varchar (25) [NOT NULL],
	supervisor varchar (150) [NOT NULL],
	salario float (15) [NOT NULL],
	funcao varchar(100) [NOT NULL],	
	primary key cpf 
	);
	
	
2) Inserir as informações abaixo:
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values (Bruna Vianna,151515150,711111111-11,Administrativo,Renato,2000,Recepcionista);


NOME			RG			CPF				DPTO			SUPERVISOR	SALARIO 		FUNCAO
Bruna Vianna	151515150	711111111-11	Administrativo	Renato	 	R$ 2.000,00 	Recepcionista
Celio Martins	141414140	611111111-11	Administrativo	Renato	 	R$ 1.500,00 	Porteiro
Maria Aparecida	171717170	911111111-11	Administrativo	Renato	 	R$ 1.250,00 	Auxiliar Serviços Gerais
Mirian Leitao	161616160	811111111-11	Administrativo	Renato	 	R$ 2.000,00 	Recepcionista
Hoche Pulge		101010100	211111111-11	Diretoria		Fenton	 	R$ 12.000,00 	Diretor
Anthony Freitas	121212120	411111111-11	Engenharia		Fabiano	 	R$ 3.500,00 	Analista
Fabiano Junior	181818180	221111111-11	Engenharia		Hoche	 	R$ 7.500,00 	Gerente
Patricia Nedina	40404040	444444444-44	Engenharia		Fabiano	 	R$ 5.000,00 	Engenheiro
Joao Luiz		10101010	111111111-11	Financeiro		Renato	 	R$ 3.500,00 	Analista
Renato Silva	111111110	311111111-11	Financeiro		Hoche	 	R$ 7.500,00 	Gerente
Jose Varella	20202020	222222222-22	RH				Renato	 	R$ 3.500,00 	Analista
Ricardo Silva	30303030	333333333-33	RH				Renato	 	R$ 3.500,00 	Recutador
Anderson Sobral	131313130	511111111-11	Suporte			Hoche	 	R$ 7.500,00 	Gerente
Bruno Melo		50505050	555555555-55	Suporte			Anderson	R$ 1.600,00 	Atendente
Celia Regina	70707070	777777777-77	Suporte			Anderson	R$ 1.600,00 	Atendente
Glauce Monteiro	80808080	888888888-88	Suporte			Anderson	R$ 1.600,00 	Atendente
Glauco Costa	90909090	999999999-99	Suporte			Anderson	R$ 1.600,00 	Atendente
Jorge Henrique	60606060	666666666-66	Suporte			Anderson	R$ 1.600,00 	Atendente
Willian Militão	191919190	321111111-11	Suporte			Hoche	 	R$ 3.500,00 	Supervisor

insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Bruna Vianna','151515150','711111111-11','Administrativo','Renato',2000,'Recepcionista');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Celio Martins','141414140','611111111-11','Administrativo','Renato',1500,'Porteiro');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Maria Aparecida','171717170','911111111-11','Administrativo','Renato',1250,'Aux Servicos Gerais');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Mirian Leitao','161616160','811111111-11','Administrativo','Renato',2000,'Recepcionista');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Hoche Pulge','101010100','211111111-11','Diretoria','Fenton',12000,'Diretor');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Anthony Freitas','121212120','411111111-11','Engenharia','Fabiano',3500,'Analista');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Fabiano Junior','181818180','221111111-11','Engenharia','Hoche',7500,'Gerente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Patricia Nedina','40404040','444444444-44','Engenharia','Fabiano',5000,'Engenheiro');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Joao Luiz','10101010','111111111-11','Financeiro','Renato',3500,'Analista');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Renato Silva','141414140','311111111-11','Financeiro','Hoche',7500,'Gerente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Jose Varella','20202020','222222222-22','RH','Renato',3500,'Analista');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Ricardo Silva','30303030','333333333-33','RH','Renato',3500,'Recrutador');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Anderson Sobral','131313130','511111111-11','Suporte','Hoche',7500,'Gerente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Bruno Melo','50505050','555555555-55','Suporte','Anderson',1600,'Atendente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Celia Regina','70707070','777777777-77','Suporte','Anderson',1600,'Atendente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Glauce Monteiro','80808080','888888888-88','Suporte','Anderson',1600,'Atendente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Glauco Costa','90909090','999999999-99','Suporte','Anderson',1600,'Atendente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Jorge Henrique','60606060','666666666-66','Suporte','Anderson',1600,'Atendente');
insert into tbfuncionarios (nome,rg,cpf,dpto,supervisor, salario, funcao) values ('Willian Militão','191919190','321111111-11','Suporte','Hoche',3500,'Supervisor');

3) Selecionar quantas pessoas existem cadastradas:
	select count(*) from tbfuncionarios;

4) Selecionar quantos funcionarios pertencem ao departamento "Suporte":
	select count(*) from tbfuncionarios where depto="Suporte";

5) Selecionar o nome e o cpf dos funcionarios que possuem salario maior que 3000 reais.
	select (nome, rg) FROM tbfuncionarios where salario > 3000;
	
6) Remover registros da tabelas funcionarios que possuam a funcao "porteiro":
	delete from tbfuncionarios where funcao='porteiro'

7) Aumentar o salario em 12% dos funcionarios que possuam a funcao "analista":
	update tbfuncionarios set salario=salario+salario*0.12 where funcao='analista';

8) Aumentar o salario em 15% dos funcionarios que possuam o salario entre R$ 1000,00 e R$ 2000,00:
	update tbfuncionarios set salario=salario+salario*0.15 where salario between 1000 and 2000;


9) Crie uma instrução SQL para que o funcionário Hoche Pulge tenha um aumento de 50% em seu salário.

10) Crie uma instrução SQL que mostre quantos funcionários
ganham mais que R$ 2500.

11) Crie uma instrução SQL que mostra o nome e o salário dos
funcionários que trabalham no depto 'Engenharia'

12) Atualize o banco de dados para funcionarios que ganham
mais que R$ 4999, descontando 15% de IR seus salários

13) Dado o comando abaixo faça o desenho de como ficará
essa tabela no banco de dados.
CREATE TABLE armazem (
	item INT(6) DEFAULT NOT NULL AUTO_INCREMENT,
	vendedor CHAR(20) NOT NULL,
	preco DOUBLE(16,2) NOT NULL,
	fornecedor INT(6) NOT NULL,
	PRIMARY KEY(artigo));
	
14) Dada a tabela funcionarios e o comando abaixo diga qual
será o resultado da operação.
	mysql>DELETE FROM funcionarios WHERE depto='rh';
	Todos os funcionários do departamento RH serão deletados

15) Apague a tabela funcionarios.
	drop table tbfuncionarios;