-- 1. Análise de Ingredientes por Fornecedor
SELECT 
    fornecedor,
    COUNT(*) AS total_ingredientes,
    AVG(DATEDIFF(validade, CURDATE())) AS dias_validade_media
FROM ingredientes
GROUP BY fornecedor
ORDER BY total_ingredientes DESC;

-- 2. Capacidade Total de Armazenamento por Tipo de Tanque
SELECT 
    tipo,
    SUM(capacidade) AS capacidade_total,
    COUNT(*) AS quantidade_tanques,
    AVG(capacidade) AS capacidade_media
FROM tanques
GROUP BY tipo
ORDER BY capacidade_total DESC;

-- 3. Histórico de Processos de Produção
SELECT 
    m.id AS mosturacao_id,
    f.id AS fermentacao_id,
    d.id AS destilacao_id,
    ma.id AS maturacao_id,
    m.inicio_processo AS inicio_mostura,
    ma.fim_processo AS fim_maturacao,
    DATEDIFF(ma.fim_processo, m.inicio_processo) AS duracao_total_dias
FROM mosturacoes m
JOIN fermentacoes f ON m.id = f.mosturacao_id
JOIN destilacoes d ON f.id = d.fermentacao_id
JOIN maturacoes ma ON d.id = ma.destilacao_id
ORDER BY m.inicio_processo;

-- 4. Qualidade da Destilação (Teor Alcoólico)
SELECT 
    d.id AS destilacao_id,
    t.valor AS teor_alcoolico,
    v.valor AS vazao,
    CASE 
        WHEN t.valor >= 50 THEN 'Alta Qualidade'
        WHEN t.valor BETWEEN 45 AND 49.9 THEN 'Média Qualidade'
        ELSE 'Baixa Qualidade' 
    END AS classificacao
FROM destilacoes d
JOIN teor_alcoolicos t ON d.teor_alcoolico_id = t.id
JOIN vazoes v ON d.vazao_id = v.id
ORDER BY t.valor DESC;

-- 5. Análise de Envase
SELECT 
    tipo_garrafa,
    COUNT(*) AS total_garrafas,
    SUM(litros_garrafa) AS total_litros,
    AVG(litros_garrafa) AS litros_medio_por_garrafa
FROM empacotamentos
GROUP BY tipo_garrafa
ORDER BY total_garrafas DESC;

-- 6. Monitoramento de Fermentação
SELECT 
    f.id AS fermentacao_id,
    ph.valor AS ph,
    temp.valor AS temperatura,
    dens.valor AS densidade,
    DATEDIFF(f.fim_processo, f.inicio_processo) AS duracao_dias,
    CASE
        WHEN ph.valor BETWEEN 5.2 AND 5.8 AND temp.valor BETWEEN 18 AND 22 THEN 'Condições Ideais'
        ELSE 'Condições Não-Ideais'
    END AS status_fermentacao
FROM fermentacoes f
JOIN phs ph ON f.ph_id = ph.id
JOIN temperaturas temp ON f.temperatura_id = temp.id
JOIN densidades dens ON f.densidade_id = dens.id;

-- 7. Estoque de Ingredientes
SELECT 
    i.nome,
    i.tipo,
    SUM(l.quantidade) AS quantidade_total,
    l.unidade AS unidade_medida,
    MAX(l.data_recebimento) AS ultimo_recebimento
FROM ingredientes i
JOIN lotes_ingredientes l ON i.id = l.ingrediente_id
GROUP BY i.nome, i.tipo, l.unidade
ORDER BY quantidade_total desc;

-- 8. Eficiência de Produção
SELECT
    WEEK(inicio_processo) AS semana,
    COUNT(*) AS total_processos,
    AVG(DATEDIFF(fim_processo, inicio_processo)) AS duracao_media_dias
FROM (
    SELECT inicio_processo, fim_processo FROM mosturacoes
    UNION ALL
    SELECT inicio_processo, fim_processo FROM fermentacoes
    UNION ALL
    SELECT inicio_processo, fim_processo FROM destilacoes
) AS processos
GROUP BY semana
ORDER BY semana;

-- 9. Análise de Qualidade ao Longo do Tempo
SELECT 
    DATE_FORMAT(momento_leitura, '%Y-%m') AS mes,
    'pH' AS tipo_medicao,
    AVG(valor) AS valor_medio
FROM phs
GROUP BY mes

UNION ALL

SELECT 
    DATE_FORMAT(momento_leitura, '%Y-%m') AS mes,
    'Temperatura' AS tipo_medicao,
    AVG(valor) AS valor_medio
FROM temperaturas
GROUP BY mes

UNION ALL

SELECT 
    DATE_FORMAT(momento_leitura, '%Y-%m') AS mes,
    'Teor Alcoólico' AS tipo_medicao,
    AVG(valor) AS valor_medio
FROM teor_alcoolicos
GROUP BY mes

ORDER BY mes, tipo_medicao;

-- 10. Cadeia Completa de Produção (Batch 1001)
SELECT 
    e.lote,
    i.nome AS ingrediente_principal,
    m.inicio_processo AS inicio_mostura,
    ma.fim_processo AS fim_maturacao,
    e.data_empacotamento,
    DATEDIFF(e.data_empacotamento, m.inicio_processo) AS duracao_total_dias
FROM empacotamentos e
JOIN maturacoes ma ON e.maturacao_id = ma.id
JOIN destilacoes d ON ma.destilacao_id = d.id
JOIN fermentacoes f ON d.fermentacao_id = f.id
JOIN mosturacoes m ON f.mosturacao_id = m.id
JOIN lotes_ingredientes l ON m.lote_ingrediente_id = l.id
JOIN ingredientes i ON l.ingrediente_id = i.id
WHERE e.lote = 1001;

-- 11. Tanques em Operação Agora
SELECT 
    t.nome,
    t.tipo,
    t.capacidade,
    t.status_tanque,
    CASE 
        WHEN m.id IS NOT NULL THEN 'Mosturação'
        WHEN f.id IS NOT NULL THEN 'Fermentação'
        WHEN d.id IS NOT NULL THEN 'Destilação'
        WHEN ma.id IS NOT NULL THEN 'Maturação'
        ELSE 'Ocioso'
    END AS operacao_atual
FROM tanques t
LEFT JOIN mosturacoes m ON t.id = m.tanque_id AND NOW() BETWEEN m.inicio_processo AND m.fim_processo
LEFT JOIN fermentacoes f ON t.id = f.tanque_id AND NOW() BETWEEN f.inicio_processo AND f.fim_processo
LEFT JOIN destilacoes d ON t.id = d.tanque_id AND NOW() BETWEEN d.inicio_processo AND d.fim_processo
LEFT JOIN maturacoes ma ON t.id = ma.id AND NOW() BETWEEN ma.inicio_processo AND ma.fim_processo
WHERE t.status_tanque = 'Ocupado';