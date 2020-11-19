import pandas as pd
import json
import random
import math

from log.Log import Log
from log.PreProcess import PreProcess
from process.MacroSteps import MacroSteps


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
             'versao6/resultado_1_0_null.csv'

# file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
#             'versao5/version_5.csv'

movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/df_movimentos.csv'

pp = PreProcess(file_location=file_path)
# pp.select_desired_columns()
pp.filter_outlier_timestamp()
pp.map_movements(movement_path)

# filter first movement to "Distribuição"

df_log = pp.df_log

df_log

df_first = df_log.groupby('case:concept:name', as_index=False).\
    agg({'time:timestamp':'min', 'concept:name':'first'})

# df_first.groupby('concept:name', as_index=False).count().\
#     sort_values(by='case:concept:name', ascending=False)

df_first = df_first[df_first['concept:name'] == 'Distribuição']\
    [['case:concept:name']]

keys = ['case:concept:name']

i1 = df_log.set_index(keys).index
i2 = df_first.set_index(keys).index

df_log = df_log[i1.isin(i2)]


# filter last movement to "Baixa/Arquivamento"


df_last = df_log.groupby('case:concept:name', as_index=False).\
    agg({'time:timestamp':'max', 'concept:name':'last'})

df_last.groupby('concept:name', as_index=False).count().\
    sort_values(by='case:concept:name', ascending=False)

df_last = df_last[df_last['concept:name'] == 'Baixa/Arquivamento']\
    [['case:concept:name']]

keys = ['case:concept:name']

i1 = df_log.set_index(keys).index
i2 = df_last.set_index(keys).index

df_log = df_log[i1.isin(i2)]

df_log

# make some tests

df_log.drop_duplicates(['case:concept:name']).\
    groupby(['case: orgao_mun']).count().sort_values('case:concept:name')


