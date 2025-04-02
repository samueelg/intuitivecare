SELECT 
    oa.REG_ANS,
    oa.Razao_Social,
    SUM(ccc.VL_SALDO_FINAL - ccc.VL_SALDO_INICIAL) AS total_despesas
FROM cd_conta_contabil ccc
JOIN operadoras_ativas oa ON ccc.REG_ANS = oa.REG_ANS
WHERE 
    ccc.DESCRICAO like 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND ccc.DATA >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY oa.REG_ANS, oa.Razao_Social
ORDER BY total_despesas DESC
LIMIT 10;
