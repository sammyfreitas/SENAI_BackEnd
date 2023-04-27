select * from tbfuncionarios;
select * from tbfuncionarios where dpto = 'Suporte';
update tbfuncionarios set salario=salario+salario*0.15 where salario between 1000 and 2000;
select * from tbfuncionarios;
update tbfuncionarios set salario=salario+salario*0.12 where funcao='Analista';
select * from tbfuncionarios;
update tbfuncionarios set funcao='Programador' where nome='Bruna_';
select * from tbfuncionarios;