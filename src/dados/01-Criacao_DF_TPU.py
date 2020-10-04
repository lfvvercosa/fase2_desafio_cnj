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
    SELECT i.cod_item, i.cod_item_pai, i.nome, i.situacao,
           c.just_es_2grau, c.just_es_juizado_es, c.just_es_turmas, c.just_es_1grau_mil, c.just_es_2grau_mil,
    	   c.just_es_juizado_es_fp, c.just_tu_es_un, c.just_fed_1grau, c.just_fed_2grau, c.just_fed_juizado_es,
           c.just_fed_turmas, c.just_fed_nacional, c.just_fed_regional, c.just_trab_1grau, c.just_trab_2grau,
    	   c.just_trab_tst, c.just_trab_csjt, c.stf, c.stj, c.cjf, c.cnj, c.just_mil_uniao_1grau, c.just_mil_uniao_stm,
    	   c.just_mil_est_1grau, c.just_mil_est_tjm, c.just_elei_1grau, c.just_elei_2grau, c.just_elei_tse
      FROM classes c inner join itens i on i.cod_item = c.cod_classe AND i.tipo_item = 'C'
"""
sSql_assuntos   = """
    SELECT i.cod_item, i.cod_item_pai, i.nome, i.situacao, a.sigiloso, a.assunto_secundario, a.crime_antecedente,
           a.just_es_2grau, a.just_es_juizado_es, a.just_es_turmas, a.just_es_1grau_mil, a.just_es_2grau_mil,
    	   a.just_es_juizado_es_fp, a.just_tu_es_un, a.just_fed_1grau, a.just_fed_2grau, a.just_fed_juizado_es,
           a.just_fed_turmas, a.just_fed_nacional, a.just_fed_regional, a.just_trab_1grau, a.just_trab_2grau,
    	   a.just_trab_tst, a.just_trab_csjt, a.stf, a.stj, a.cjf, a.cnj, a.just_mil_uniao_1grau, a.just_mil_uniao_stm,
    	   a.just_mil_est_1grau, a.just_mil_est_tjm, a.just_elei_1grau, a.just_elei_2grau, a.just_elei_tse
      FROM assuntos a INNER JOIN itens i ON i.cod_item = a.cod_assunto AND i.tipo_item = 'A'
"""
sSql_movimentos = """
    SELECT i.cod_item, i.cod_item_pai, i.nome, i.situacao, 
    	   m.visibilidade_externa, m.monocratico, m.colegiado, m.presidente_vice, m.flg_papel, m.flg_eletronico,
           m.just_es_2grau, m.just_es_juizado_es, m.just_es_turmas, m.just_es_1grau_mil, m.just_es_2grau_mil,
    	   m.just_es_juizado_es_fp, m.just_tu_es_un, m.just_fed_1grau, m.just_fed_2grau, m.just_fed_juizado_es,
           m.just_fed_turmas, m.just_fed_nacional, m.just_fed_regional, m.just_trab_1grau, m.just_trab_2grau,
    	   m.just_trab_tst, m.just_trab_csjt, m.stf, m.stj, m.cjf, m.cnj, m.just_mil_uniao_1grau, m.just_mil_uniao_stm,
    	   m.just_mil_est_1grau, m.just_mil_est_tjm, m.just_elei_1grau, m.just_elei_2grau, m.just_elei_tse
      FROM movimentos m INNER JOIN itens i ON i.cod_item = m.cod_movimento AND i.tipo_item = 'M'
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


# Conectar ao banco de dados
print("1. Conectando ao banco de dados...")    
conn = create_connection(banco)

#par = {'tipo':'text/html', 'limite':3724, 'competencia':1}
with conn:
    # Criar data_frame para as classes processuais    
    print("2. Gerando dataframe das classes...")
    try:
        df_classes = pd.read_sql_query(sSql_classes, conn, ) # , params=par
        df_classes.to_csv('../../dados/provisorios/df_classes.csv')
        print("2. Dataframe das classes gerado com sucesso em: dados/provisorios/df_classes.csv")
    except Error as e:
        print('2. Erro ao tentar gerar as classes: ',e)
      
    # Criar data_frame para os assuntos 
    print("3. Gerando dataframe dos assuntos...")
    try:
        df_assuntos = pd.read_sql_query(sSql_assuntos, conn)
        df_assuntos.to_csv('../../dados/provisorios/df_assuntos.csv')
        print("2. Dataframe dos assuntos gerado com sucesso em: dados/provisorios/df_assuntos.csv")
    except Error as e:
        print('2. Erro ao tentar gerar os assuntos: ',e)
        
    # Criar data_frame para os movimentos
    print("4. Gerando dataframe dos movimentos...")
    try:
        df_movimentos = pd.read_sql_query(sSql_movimentos, conn)
        df_movimentos.to_csv('../../dados/provisorios/df_movimentos.csv')
        print("2. Dataframe dos movimentos gerado  com sucesso em: dados/provisorios/df_movimentos.csv")
    except Error as e:
        print('2. Erro ao tentar gerar os movimentos: ',e)        