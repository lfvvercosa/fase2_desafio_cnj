# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 08:59:53 2020

@author: diego
"""
# Carga das bibliotecas necessárias
import pandas as pd
import sqlite3
from sqlite3 import Error

# Definição das variáveis globais
# %(competencia)s
sSql_classes    = """
    SELECT COALESCE(cod_item_pai || ':' || cod_item, cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao,
           c.just_es_2grau, c.just_es_juizado_es, c.just_es_turmas, c.just_es_1grau_mil, c.just_es_2grau_mil,
    	   c.just_es_juizado_es_fp, c.just_tu_es_un, c.just_fed_1grau, c.just_fed_2grau, c.just_fed_juizado_es,
           c.just_fed_turmas, c.just_fed_nacional, c.just_fed_regional, c.just_trab_1grau, c.just_trab_2grau,
    	   c.just_trab_tst, c.just_trab_csjt, c.stf, c.stj, c.cjf, c.cnj, c.just_mil_uniao_1grau, c.just_mil_uniao_stm,
    	   c.just_mil_est_1grau, c.just_mil_est_tjm, c.just_elei_1grau, c.just_elei_2grau, c.just_elei_tse
      FROM classes c inner join itens i on i.cod_item = c.cod_classe AND i.tipo_item = 'C' 
    UNION ALL
    SELECT COALESCE(i.cod_item_pai || ':' || i.cod_item, i.cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao,
               '' as just_es_2grau, '' as just_es_juizado_es, '' as just_es_turmas, '' as just_es_1grau_mil, '' as just_es_2grau_mil,
        	   '' as just_es_juizado_es_fp, '' as just_tu_es_un, '' as just_fed_1grau, '' as just_fed_2grau, '' as just_fed_juizado_es,
               '' as just_fed_turmas, '' as just_fed_nacional, '' as just_fed_regional, '' as just_trab_1grau, '' as just_trab_2grau,
        	   '' as just_trab_tst, '' as just_trab_csjt, '' as stf, '' as stj, '' as cjf, '' as cnj, '' as just_mil_uniao_1grau, '' as just_mil_uniao_stm,
        	   '' as just_mil_est_1grau, '' as just_mil_est_tjm, '' as just_elei_1grau, '' as just_elei_2grau, '' as just_elei_tse
          FROM itens i 
    WHERE i.tipo_item = 'C' 
      AND i.cod_item NOT IN (SELECT cod_classe FROM classes)	  
"""
sSql_assuntos   = """
    SELECT COALESCE(cod_item_pai || ':' || cod_item, cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao, a.sigiloso, a.assunto_secundario, a.crime_antecedente,
           a.just_es_2grau, a.just_es_juizado_es, a.just_es_turmas, a.just_es_1grau_mil, a.just_es_2grau_mil,
    	   a.just_es_juizado_es_fp, a.just_tu_es_un, a.just_fed_1grau, a.just_fed_2grau, a.just_fed_juizado_es,
           a.just_fed_turmas, a.just_fed_nacional, a.just_fed_regional, a.just_trab_1grau, a.just_trab_2grau,
    	   a.just_trab_tst, a.just_trab_csjt, a.stf, a.stj, a.cjf, a.cnj, a.just_mil_uniao_1grau, a.just_mil_uniao_stm,
    	   a.just_mil_est_1grau, a.just_mil_est_tjm, a.just_elei_1grau, a.just_elei_2grau, a.just_elei_tse
      FROM assuntos a INNER JOIN itens i ON i.cod_item = a.cod_assunto AND i.tipo_item = 'A'
    UNION ALL
    SELECT COALESCE(i.cod_item_pai || ':' || i.cod_item, i.cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao, '' as sigiloso, '' as assunto_secundario, '' as crime_antecedente,
               '' as just_es_2grau, '' as just_es_juizado_es, '' as just_es_turmas, '' as just_es_1grau_mil, '' as just_es_2grau_mil,
        	   '' as just_es_juizado_es_fp, '' as just_tu_es_un, '' as just_fed_1grau, '' as just_fed_2grau, '' as just_fed_juizado_es,
               '' as just_fed_turmas, '' as just_fed_nacional, '' as just_fed_regional, '' as just_trab_1grau, '' as just_trab_2grau,
        	   '' as just_trab_tst, '' as just_trab_csjt, '' as stf, '' as stj, '' as cjf, '' as cnj, '' as just_mil_uniao_1grau, '' as just_mil_uniao_stm,
        	   '' as just_mil_est_1grau, '' as just_mil_est_tjm, '' as just_elei_1grau, '' as just_elei_2grau, '' as just_elei_tse
          FROM itens i 
    WHERE i.tipo_item = 'A' 
      AND i.cod_item NOT IN (SELECT cod_assunto FROM assuntos)	
"""
sSql_movimentos = """
    SELECT COALESCE(i.cod_item_pai || ':' || i.cod_item, i.cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao, 
    	   m.visibilidade_externa, m.monocratico, m.colegiado, m.presidente_vice, m.flg_papel, m.flg_eletronico,
           m.just_es_2grau, m.just_es_juizado_es, m.just_es_turmas, m.just_es_1grau_mil, m.just_es_2grau_mil,
    	   m.just_es_juizado_es_fp, m.just_tu_es_un, m.just_fed_1grau, m.just_fed_2grau, m.just_fed_juizado_es,
           m.just_fed_turmas, m.just_fed_nacional, m.just_fed_regional, m.just_trab_1grau, m.just_trab_2grau,
    	   m.just_trab_tst, m.just_trab_csjt, m.stf, m.stj, m.cjf, m.cnj, m.just_mil_uniao_1grau, m.just_mil_uniao_stm,
    	   m.just_mil_est_1grau, m.just_mil_est_tjm, m.just_elei_1grau, m.just_elei_2grau, m.just_elei_tse
      FROM movimentos m INNER JOIN itens i ON i.cod_item = m.cod_movimento AND i.tipo_item = 'M'
    UNION ALL
    SELECT COALESCE(i.cod_item_pai || ':' || i.cod_item, i.cod_item) as breadscrum, i.cod_item, i.cod_item_pai, i.nome, i.situacao, 
     	   '' as visibilidade_externa, '' as monocratico, '' as colegiado, '' as presidente_vice, '' as flg_papel, '' as flg_eletronico,
           '' as just_es_2grau, '' as just_es_juizado_es, '' as just_es_turmas, '' as just_es_1grau_mil, '' as just_es_2grau_mil,
    	   '' as just_es_juizado_es_fp, '' as just_tu_es_un, '' as just_fed_1grau, '' as just_fed_2grau, '' as just_fed_juizado_es,
           '' as just_fed_turmas, '' as just_fed_nacional, '' as just_fed_regional, '' as just_trab_1grau, '' as just_trab_2grau,
    	   '' as just_trab_tst, '' as just_trab_csjt, '' as stf, '' as stj, '' as cjf, '' as cnj, '' as just_mil_uniao_1grau, '' as just_mil_uniao_stm,
    	   '' as just_mil_est_1grau, '' as just_mil_est_tjm, '' as just_elei_1grau, '' as just_elei_2grau, '' as just_elei_tse          
	 FROM itens i 
    WHERE i.tipo_item = 'M' 
      AND i.cod_item NOT IN (SELECT cod_movimento FROM movimentos)	
"""

banco = r"../../dados/provisorios/TPU.db"

# Funcoes básicas
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("1. Conectado ao banco!")        
    except Error as e:
        print('1. Erro ao tentar conectar ao banco: ',e)

    return conn

def hierarquia(df, breadscrum, cod_item_pai):
    texto = str(breadscrum)
    if cod_item_pai > 0:
        pai = df.loc[df.cod_item == cod_item_pai]['cod_item_pai'].values[0]
        while pai >0 :
            texto = str(int(pai)) + ":" + str(texto)
            pai = df.loc[df.cod_item == pai]['cod_item_pai'].values[0]
    
    return texto

# Conectar ao banco de dados
print("1. Conectando ao banco de dados...")    
conn = create_connection(banco)

#par = {'tipo':'text/html', 'limite':3724, 'competencia':1}
with conn:
    # Criar data_frame para as classes processuais    
    print("2. Gerando dataframe das classes...")
    try:
        df_classes = pd.read_sql_query(sSql_classes, conn) # , params=par
        df_classes = df_classes.fillna(0)
        df_classes['cod_item_pai'] = df_classes['cod_item_pai'].astype('int')
        df_classes['breadscrum'] = df_classes.apply(lambda x: hierarquia(df_classes, x['breadscrum'], x['cod_item_pai']), axis=1)
        df_classes.to_csv('../../dados/provisorios/df_classes.csv')
        print("2. Dataframe das classes gerado com sucesso em: dados/provisorios/df_classes.csv")
    except Error as e:
        print('2. Erro ao tentar gerar as classes: ',e)
      
    # Criar data_frame para os assuntos 
    print("3. Gerando dataframe dos assuntos...")
    try:
        df_assuntos = pd.read_sql_query(sSql_assuntos, conn)
        df_assuntos = df_assuntos.fillna(0)
        df_assuntos['cod_item_pai'] = df_assuntos['cod_item_pai'].astype('int')
        df_assuntos['breadscrum'] = df_assuntos.apply(lambda x: hierarquia(df_assuntos, x['breadscrum'], x['cod_item_pai']), axis=1)
        df_assuntos.to_csv('../../dados/provisorios/df_assuntos.csv')

        print("2. Dataframe dos assuntos gerado com sucesso em: dados/provisorios/df_assuntos.csv")
    except Error as e:
        print('2. Erro ao tentar gerar os assuntos: ',e)
        
    # Criar data_frame para os movimentos
    print("4. Gerando dataframe dos movimentos...")
    try:
        df_movimentos = pd.read_sql_query(sSql_movimentos, conn)
        df_movimentos = df_movimentos.fillna(0)
        df_movimentos['cod_item_pai'] = df_movimentos['cod_item_pai'].astype('int')
        df_movimentos['breadscrum'] = df_movimentos.apply(lambda x: hierarquia(df_movimentos, x['breadscrum'], x['cod_item_pai']), axis=1)
        df_movimentos.to_csv('../../dados/provisorios/df_movimentos.csv')
        print("2. Dataframe dos movimentos gerado  com sucesso em: dados/provisorios/df_movimentos.csv")
    except Error as e:
        print('2. Erro ao tentar gerar os movimentos: ',e)        