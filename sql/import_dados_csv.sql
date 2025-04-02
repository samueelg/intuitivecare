CREATE TEMP TABLE cd_conta_contabil_temp AS
SELECT * FROM cd_conta_contabil LIMIT 0;

COPY cd_conta_contabil_temp FROM 'caminho\\do\\seu\\arquivo.csv'
DELIMITER ';' CSV HEADER;

INSERT INTO cd_conta_contabil (data,reg_ans,cd_conta_contabil,descricao,vl_saldo_inicial,vl_saldo_final)
SELECT data,reg_ans,cd_conta_contabil,descricao,vl_saldo_inicial,vl_saldo_final
FROM cd_conta_contabil_temp
WHERE reg_ans IN (SELECT reg_ans FROM operadoras_ativas);
