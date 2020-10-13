-------------------------------------------------------------------------------
-- /varas -- lista de varas ---------------------------------------------------
-------------------------------------------------------------------------------
-- Lista os IDs e nomes de vara da tabela "varas"
SELECT distinct
	[identificador],
	[nome] as [vara]
FROM [varas]
ORDER BY [nome]

-------------------------------------------------------------------------------
-- /varas/{identificador} -- informacoes detalhadas da vara especificada ------
-------------------------------------------------------------------------------
-- Dado um ID, informa os detalhes da vara
-- @identificador bigint NOT NULL
SELECT
	[varas].[nome] as [vara],
	[varas].[colocacao],
	[varas].[processos_julgados],
	[varas].[dias_baixa_processo],
	[varas].[movimentacoes],

    [varas].[identificador_grupo],
    [grupos].[justica] as [justica_grupo],
    [grupos].[grau] as [grau_grupo],
    [grupos].[tribunal] as [tribunal_grupo],
    [grupos].[classe_judicial] as [classe_judicial_grupo],
    [grupos].[assunto] as [assunto_grupo],
    [grupos].[orgao_julgador] as [orgao_julgador_grupo],
    [grupos].[quantidade_de_varas] as [quantidade_de_varas_grupo]
FROM [varas]
LEFT JOIN [grupos] ON [varas].[identificador_grupo] = [grupos].[identificador]
WHERE [varas].[identificador] = @identificador


-------------------------------------------------------------------------------
-- /varas/melhoresVarasNaEtapa -- melhores varas do grupo na etapa ------------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
-- /etapas/melhoresEtapas -- melhores etapas da vara --------------------------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
-- /etapas/pioresEtapas -- piores etapas da vara ------------------------------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
-- /processos/melhoresVaras -- informacoes das melhores varas -----------------
-------------------------------------------------------------------------------
