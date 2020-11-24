import pandas as pd
import json
import random
import math
import matplotlib.pyplot as plt
import numpy as np

from log.Log import Log
from log.PreProcess import PreProcess
from process.MacroSteps import MacroSteps


# link 'grupos' and 'varas'


path_clusters = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
                'fase2_git/repositorio_fase_2/fase2_desafio_cnj/'+\
                'data/interim/clusterizacao.csv'

# file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
#             'versao5/version_5.csv'

# file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
#             'versao6/resultado_1_classe_0_null.csv'

file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
             'versao7/movimento_estadual_G1_filtered.csv'


movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
                'fase2_git/repositorio_fase_2/fase2_desafio_cnj/'+\
                'data/interim/df_movimentos.csv'

lat_long_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/' + \
                'municipios_lat_long.csv'

comments_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
                'fase2_git/repositorio_fase_2/fase2_desafio_cnj/'+\
                'data/interim/praticas.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

classes_map_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao7/classes_mapping.csv'

assuntos_map_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao7/assuntos_mapping.csv'

assuntos_aux = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
                'fase2_git/repositorio_fase_2/fase2_desafio_cnj/'+\
                'data/interim/df_assuntos.csv'

classes_aux = '/home/vercosa/Insync/doutorado/hackaton_cnj/'+\
                'fase2_git/repositorio_fase_2/fase2_desafio_cnj/'+\
                'data/interim/df_classes.csv'

# df_log = pd.read_csv(file_path,
#                      dtype=datatypes,
#                      sep=';', 
#                      engine='python')

pp = PreProcess(file_location=file_path)
pp.select_desired_columns()
pp.filter_outlier_timestamp()
pp.map_movements(movement_path)

df_log = pp.df_log

# filter last movement to "Baixa/Arquivamento"

df_last = df_log.groupby('case:concept:name', as_index=False).\
    agg({'time:timestamp':'max', 'concept:name':'last'})

df_last = df_last[df_last['concept:name'] == 'Baixa/Arquivamento']\
    [['case:concept:name']]

keys = ['case:concept:name']

i1 = df_log.set_index(keys).index
i2 = df_last.set_index(keys).index

df_log = df_log[i1.isin(i2)]

# calc df_proc (used for filtering out "Varas" with few process instance)

df_proc = df_log[['case: orgao_mun', 'case:concept:name']].drop_duplicates()
df_proc = df_proc.groupby('case: orgao_mun').count().\
    sort_values(by='case:concept:name')
df_proc = df_proc.rename(columns={'case:concept:name':'process_count'})
df_proc.reset_index(level=0, inplace=True)
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].str.upper()
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].str.replace('"','')
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].\
    str.replace(' - ','-')
df_proc['case: orgao_mun'] = df_proc['case: orgao_mun'].\
    str.replace('-',' - ')
df_proc = df_proc[df_proc['process_count'] >= 25]


# check how many encoding errors
# l1 = [x for x in df_proc['case: orgao_mun'].unique().tolist()] 
# l2 = [x for x in df_proc['case: orgao_mun'].unique().tolist()] 
# l2 = [x.encode('latin-1', errors='ignore').decode('latin-1') for x in l2]

# count = 0 

# for i in range(len(l1)): 
#     if l1[i] == l2[i]: 
#         count += 1 

# count

# clustering

df_clusters = pd.read_csv(path_clusters,
                        sep=';',
                        engine='python')

# df_clusters['Orgao Julgador'] = df_clusters['Orgao Julgador'].str.upper()
# df_clusters = df_clusters.rename(columns={'Orgao Julgador':'case: orgao_mun'})

df_clusters['case: orgao_mun'] = df_clusters['case: orgao_mun'].str.upper()
df_clusters['case: orgao_mun'] = df_clusters['case: orgao_mun'].\
    str.replace(' - ','-')
df_clusters['case: orgao_mun'] = df_clusters['case: orgao_mun'].\
    str.replace('-',' - ')

alg = 'cluster'

df_clusters_alg = df_clusters[['case: orgao_mun', alg]]

df_proc = df_proc.merge(df_clusters_alg, on='case: orgao_mun', how='left')

df_temp = df_proc.groupby(alg).count().sort_values(by='case: orgao_mun')

df_temp

df_temp.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao7/grupos_cluster.csv', sep=';')


# Obtain most frequent classes of processes

df_selected = df_clusters[['case: orgao_mun', alg]]
df_selected = df_selected[(df_selected[alg] == 0) |
                          (df_selected[alg] == 1) |
                          (df_selected[alg] == 2) |
                          (df_selected[alg] == 3) |
                          (df_selected[alg] == 4) \
                          ]

df_class_map = pd.read_csv(classes_map_path,
                           dtype=datatypes,
                           sep=';',
                           engine='python')

df_selected = df_selected.\
                merge(df_class_map, on='case: orgao_mun', how='left')

df_selected = df_selected[df_selected['case: classe_root'].notna()]
df_selected['case: classe_root'] = \
    df_selected['case: classe_root'].astype(int)

# filter 'varas' with less than 25 processes
df_filter = df_selected.groupby('case: orgao_mun', as_index=False).count()
df_filter = df_filter[df_filter[alg] >= 25][['case: orgao_mun']]

key = ['case: orgao_mun']
i1 = df_selected.set_index(key).index
i2 = df_filter.set_index(key).index

df_selected = df_selected[i1.isin(i2)]

# get most frequent

df_selected = df_selected.\
    groupby(['case: orgao_mun', 'case: classe_root'], as_index=False).\
    agg({'case:concept:name':'count', alg:'first'})
df_selected = df_selected.rename(columns={'case:concept:name': 'count'})

df_aux = df_selected.groupby('case: orgao_mun', as_index=False).\
    agg({'count':'sum'})
df_aux = df_aux.rename(columns={'count': 'total'})

df_selected = df_selected.merge(df_aux, on='case: orgao_mun', how='left')
df_selected['classe_percent'] = \
    (df_selected['count'] / df_selected['total']) * 100
df_selected['classe_percent'] = df_selected['classe_percent'].round(2)

df_aux = df_selected.drop_duplicates('case: orgao_mun').\
    groupby(alg, as_index=False).count()
df_aux = df_aux[[alg, 'total']]

df_selected = df_selected.groupby([alg,'case: classe_root'], \
    as_index=False).agg({'classe_percent':'sum'})

df_selected = df_selected.merge(df_aux, on=alg, how='left')
df_selected['classe_percent'] = df_selected['classe_percent'] \
    / df_selected['total']
df_selected['classe_percent'] = df_selected['classe_percent'].round(2)


# mapping of classe code to name

df_temp = pd.read_csv(classes_aux,
                      sep=',',
                      engine='python')
df_temp = df_temp[['breadscrum', 'nome']]
df_temp = df_temp.rename(columns={'breadscrum':'case: classe_root'})

df_selected['case: classe_root'] = \
    df_selected['case: classe_root'].astype(str)

df_selected = \
    df_selected.merge(df_temp, on='case: classe_root', how='left')

df_selected = \
    df_selected.drop(['case: classe_root', 'total'], axis=1)

# create json

json_classe_grupos = {}

for index, row in df_selected.iterrows():
    if row[alg] not in json_classe_grupos:
        json_classe_grupos[row[alg]] = {}
    json_classe_grupos[row[alg]][row['nome']] = \
        row['classe_percent']


# Obtain most frequent assuntos of processes

df_selected2 = df_clusters[['case: orgao_mun', alg]]
df_selected2 = df_selected2[(df_selected2[alg] == 0) |
                            (df_selected2[alg] == 1) |
                            (df_selected2[alg] == 2) |
                            (df_selected2[alg] == 3) |
                            (df_selected2[alg] == 4) \
                          ]

df_assunto_map = pd.read_csv(assuntos_map_path,
                           dtype=datatypes,
                           sep=';',
                           engine='python')

df_assunto_map = \
    df_assunto_map[~df_assunto_map['case: orgao_mun'].isna()]

df_selected2 = df_selected2.\
                merge(df_assunto_map, on='case: orgao_mun', how='left')

df_selected2 = df_selected2[df_selected2['case: assunto_root'].notna()]
df_selected2['case: assunto_root'] = \
    df_selected2['case: assunto_root'].astype(int)

# filter 'varas' with less than 25 processes
df_filter = df_selected2.groupby('case: orgao_mun', as_index=False).count()
df_filter = df_filter[df_filter[alg] >= 25][['case: orgao_mun']]

key = ['case: orgao_mun']
i1 = df_selected2.set_index(key).index
i2 = df_filter.set_index(key).index

df_selected2 = df_selected2[i1.isin(i2)]

# get most frequent

# count assunto by vara

df_selected2 = df_selected2.\
    groupby(['case: orgao_mun', 'case: assunto_root'], as_index=False).\
    agg({'case:concept:name':'count', alg:'first'})
df_selected2 = df_selected2.rename(columns={'case:concept:name': 'count'})

# get total processses

df_aux = df_selected2.groupby('case: orgao_mun', as_index=False).\
    agg({'count':'sum'})
df_aux = df_aux.rename(columns={'count': 'total'})

# merge total in df_selected2

df_selected2 = df_selected2.merge(df_aux, on='case: orgao_mun', how='left')
df_selected2['classe_percent'] = \
    (df_selected2['count'] / df_selected2['total']) * 100
df_selected2['classe_percent'] = df_selected2['classe_percent'].round(2)

# get total varas by group

df_aux = df_selected2.drop_duplicates('case: orgao_mun').\
    groupby(alg, as_index=False).count()
df_aux = df_aux[[alg, 'total']]

# get mean of each assunto among varas

df_selected2 = df_selected2.groupby([alg,'case: assunto_root'], \
    as_index=False).agg({'classe_percent':'sum'})

df_selected2 = df_selected2.merge(df_aux, on=alg, how='left')
df_selected2['classe_percent'] = df_selected2['classe_percent'] \
    / df_selected2['total']
df_selected2['classe_percent'] = df_selected2['classe_percent'].round(2)

# mapping of assunto code to name

df_temp = pd.read_csv(assuntos_aux,
                      sep=',',
                      engine='python')
df_temp = df_temp[['breadscrum', 'nome']]
df_temp = df_temp.rename(columns={'breadscrum':'case: assunto_root'})

df_selected2['case: assunto_root'] = \
    df_selected2['case: assunto_root'].astype(str)

df_selected2 = \
    df_selected2.merge(df_temp, on='case: assunto_root', how='left')

df_selected2 = \
    df_selected2.drop(['case: assunto_root', 'total'], axis=1)

# create json

json_assuntos_grupos = {}

for index, row in df_selected2.iterrows():
    if row[alg] not in json_assuntos_grupos:
        json_assuntos_grupos[row[alg]] = {}
    json_assuntos_grupos[row[alg]][row['nome']] = \
        row['classe_percent']



# create 'grupos' json
    # group_id: <cluster_id>
    # justice: 'states'
    # grade: 'G1'
    # competences: 1116
    # subject: 'Execução Fiscal'
    # method: 'TSNE + DBSCAN'
    # amount_of_varas: <#cluster_members>

# selected groups
    # id: 111, varas: 57
    # id: 98, varas: 17
    # id: 256, varas: 16

json_group = []

group0 = {
    'pk':0,
    'model':'performance.Group',
    'fields':{
        'group_id': 0,
        'justice': 'states',
        'grade': 'G1',
        'competences': None,
        'subject': None,
        'method': 'DBSCAN',
        'frequent_subjects': json_assuntos_grupos[0],
        'frequent_classes': json_classe_grupos[0]
    }
}

group1 = {
    'pk':1,
    'model':'performance.Group',
    'fields':{
        'group_id': 1,
        'justice': 'states',
        'grade': 'G1',
        'competences': None,
        'subject': None,
        'method': 'DBSCAN',
        'frequent_subjects': json_assuntos_grupos[1],
        'frequent_classes': json_classe_grupos[1]
    }
}

group2 = {
    'pk':2,
    'model':'performance.Group',
    'fields':{
        'group_id': 2,
        'justice': 'states',
        'grade': 'G1',
        'competences': None,
        'subject': None,
        'method': 'DBSCAN',
        'frequent_subjects': json_assuntos_grupos[2],
        'frequent_classes': json_classe_grupos[2]
    }
}

group3 = {
    'pk':3,
    'model':'performance.Group',
    'fields':{
        'group_id': 3,
        'justice': 'states',
        'grade': 'G1',
        'competences': None,
        'subject': None,
        'method': 'DBSCAN',
        'frequent_subjects': json_assuntos_grupos[3],
        'frequent_classes': json_classe_grupos[3]
    }
}

group4 = {
    'pk':4,
    'model':'performance.Group',
    'fields':{
        'group_id': 4,
        'justice': 'states',
        'grade': 'G1',
        'competences': None,
        'subject': None,
        'method': 'DBSCAN',
        'frequent_subjects': json_assuntos_grupos[4],
        'frequent_classes': json_classe_grupos[4]
    }
}

# group5 = {
#     'pk':5,
#     'model':'performance.Group',
#     'fields':{
#         'group_id': 5,
#         'justice': 'states',
#         'grade': 'G1',
#         'competences': None,
#         'subject': None,
#         'method': 'DBSCAN',
#         'frequent_subjects': json_assuntos_grupos[5],
#         'frequent_classes': json_classe_grupos[5]
#     }
# }

# group6 = {
#     'pk':6,
#     'model':'performance.Group',
#     'fields':{
#         'group_id': 6,
#         'justice': 'states',
#         'grade': 'G1',
#         'competences': None,
#         'subject': None,
#         'method': 'DBSCAN',
#         'frequent_subjects': json_assuntos_grupos[6],
#         'frequent_classes': json_classe_grupos[6]
#     }
# }

# create cadastro_etapas objects
    # step_id
    # origin
    # destination

macrosteps = [
              'Audiência',
              'Citação',
              'Conclusão',
              'Despacho',
              'Decisão',
              'Distribuição', 
              'Julgamento',
              'Trânsito em julgado', 
              'Baixa/Arquivamento',
              'Outros',
             ]

json_step_config = []
json_step_config_map = {}

step_config_id = 20

for m in macrosteps:
    for m2 in macrosteps:
        json_aux = {'model':'performance.StepConfiguration'}
        json_aux['pk'] = step_config_id
        json_aux['fields'] = {}
        json_aux['fields']['step_id'] = step_config_id
        json_aux['fields']['origin'] = m
        json_aux['fields']['destination'] = m2
        json_step_config.append(json_aux)

        json_step_config_map[m + ' -> ' + m2] = step_config_id

        step_config_id += 1


# create comments


df_comments = pd.read_csv(comments_path,
                          sep=',', 
                          engine='python')

comments_list = df_comments['Pratica'].tolist()
len_comments = len(comments_list)
json_comments = []
count_comments = 20

for c in comments_list:
    json_comments_aux = {"model": "performance.Comments",
                         "pk": str(count_comments)}
    json_comments_aux["fields"] = {"comment_id": count_comments,
                                   "comment": c}
    json_comments.append(json_comments_aux)
    count_comments += 1

# create vara objects
    # vara_id
    # nome
    # processos_julgados
    # movimentacoes
    # identificador_grupo
    # dias_baixa_processo
    
    # tempo_macroetapa1 (Distribuição)
    # tempo_macroetapa2 (Conclusão)
    # tempo_macroetapa3 (Despacho) 
    # tempo_macroetapa4 (Decisão)
    # tempo_macroetapa5 (Julgamento)
    # tempo_macroetapa6 (Trânsito em julgado)
    # tempo_macroetapa7 (Baixa/Arquivamento)


# selected groups
    # 0
    # 1
    # 2
    # 3
    # 4

varas_dict = {}

varas_dict[0] = df_proc[(df_proc[alg] == 0)]\
                    ['case: orgao_mun'].tolist()
                    
varas_dict[1] = df_proc[(df_proc[alg] == 1)]\
                    ['case: orgao_mun'].tolist()

varas_dict[2] = df_proc[(df_proc[alg] == 2)]\
                    ['case: orgao_mun'].tolist()

varas_dict[3] = df_proc[(df_proc[alg] == 3)]\
                    ['case: orgao_mun'].tolist()

varas_dict[4] = df_proc[(df_proc[alg] == 4)]\
                    ['case: orgao_mun'].tolist()                    
# pp = PreProcess(file_location=file_path)
# pp.select_desired_columns()
# pp.filter_outlier_timestamp()
# pp.map_movements(movement_path)


# df_log = pp.df_log


# filter first movement to "Distribuição"


# df_first = df_log.groupby('case:concept:name', as_index=False).\
#     agg({'time:timestamp':'min', 'concept:name':'first'})

# df_first.groupby('concept:name', as_index=False).count().\
#     sort_values(by='case:concept:name', ascending=False)

# df_first = df_first[df_first['concept:name'] == 'Distribuição']\
#     [['case:concept:name']]

# keys = ['case:concept:name']

# i1 = df_log.set_index(keys).index
# i2 = df_first.set_index(keys).index

# df_log = df_log[i1.isin(i2)]


# filter out non-macrosteps movements

# df_macrosteps = pd.DataFrame(macrosteps, columns=['concept:name'])

# keys = ['concept:name']

# i1 = df_log.set_index(keys).index
# i2 = df_macrosteps.set_index(keys).index

# df_log = df_log[i1.isin(i2)]


# df_log = pp.df_log

#### get latitude and longitude

df_log['case: orgao_mun'] = df_log['case: orgao_mun'].str.upper()
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].str.replace('"','')
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].\
    str.replace(' - ','-')
df_log['case: orgao_mun'] = df_log['case: orgao_mun'].\
    str.replace('-',' - ')

df_lat_long = pd.read_csv(lat_long_path)
df_lat_long = df_lat_long[['codigo_ibge', 'latitude', 'longitude']]

df_aux = df_log[['case: orgao_mun', 'case: municipio']].\
            drop_duplicates(subset=['case: orgao_mun'])
df_aux = df_aux.rename(columns={'case: municipio': 'codigo_ibge'})
df_aux = df_aux.merge(df_lat_long, on='codigo_ibge', how='left')
map_lat_long = df_aux.set_index('case: orgao_mun').to_dict()

json_vara = []
json_steps = []
vara_id_count = 20
step_id_count = 20
number_of_skips = {}
ranking_varas = {}
amount_of_varas = {}


for group in varas_dict:

    number_of_skips[group] = 0
    ranking_varas[group] = {}

    print('current group: ' + str(group))

    for vara in varas_dict[group]:

        json_vara_aux = {'model':'performance.Vara',
                        'pk':vara_id_count,
                        'fields':{
                            'time_distribuicao':-1,
                            'time_conclusao':-1,
                            'time_despacho':-1,
                            'time_decisao':-1,
                            'time_julgamento':-1,
                            'time_transito_em_julgado':-1,
                            'time_baixa_ou_arquivamento':-1,
                            'time_audiencia':-1,
                            'time_citacao':-1,
                            'time_outros':-1,
                        },

                        }

        vara_id = vara_id_count
        name = vara
        latitude = map_lat_long['latitude'][name]
        longitude = map_lat_long['longitude'][name]

        if math.isnan(latitude):
            latitude = None
        
        if math.isnan(longitude):
            longitude = None

        json_vara_aux['fields']['vara_id'] = vara_id
        json_vara_aux['fields']['name'] = name
        json_vara_aux['fields']['latitude'] = latitude
        json_vara_aux['fields']['longitude'] = longitude

        df_vara = df_log[df_log['case: orgao_mun'] == vara]
        pp_vara = PreProcess(df=df_vara)
        pp_vara.filter_outlier_movements(lower=0.05, upper=0.95)
        pp_vara.filter_outlier_trace_time(lower=0.05, upper=0.95)
        df_vara = pp_vara.df_log

        log = Log(df_log=pp_vara.df_log.sort_values('time:timestamp'))

        finished_processes = int(df_vara['case:concept:name'].\
            drop_duplicates().count())
        print('finished_processes: ', str(finished_processes))
        json_vara_aux['fields']['finished_processes'] = finished_processes

        total_movements = int(df_vara['case:concept:name'].count())

        movements = \
            int(total_movements / finished_processes)
        print('movements: ', str(movements))
        json_vara_aux['fields']['movements'] = movements

        group_id = group
        days_finish_process = int(log.median_time() / (24*60*60))
        print('days_finish_process: ', str(days_finish_process))
        json_vara_aux['fields']['group_id'] = group_id
        json_vara_aux['fields']['days_finish_process'] = days_finish_process
        ranking_varas[group][vara_id] = days_finish_process

        if movements > 3 and days_finish_process > 0:

            ms = MacroSteps(log.log, macrosteps)
            macrosteps_result = ms.calc_macrosteps()
            # print('')
            # print('macrosteps: ', str(macrosteps_result))
            # print('')

            # rescale macrosteps
            # total = sum(macrosteps_result.values())

            # for m in macrosteps_result:
            #     macrosteps_result[m] = int((macrosteps_result[m] / total)\
            #         * days_finish_process)

            # print('macrosteps: ', str(macrosteps_result))

            for m in macrosteps_result:
                if m == 'Distribuição':
                    json_vara_aux['fields']['time_distribuicao'] = \
                        macrosteps_result[m]

                if m == 'Conclusão':
                    json_vara_aux['fields']['time_conclusao'] = \
                        macrosteps_result[m]

                if m == 'Despacho':
                    json_vara_aux['fields']['time_despacho'] = \
                        macrosteps_result[m]

                if m == 'Decisão':
                    json_vara_aux['fields']['time_decisao'] = \
                        macrosteps_result[m]

                if m == 'Julgamento':
                    json_vara_aux['fields']['time_julgamento'] = \
                        macrosteps_result[m]
    
                if m == 'Trânsito em julgado':
                    json_vara_aux['fields']['time_transito_em_julgado'] = \
                        macrosteps_result[m]

                if m == 'Baixa/Arquivamento':
                    json_vara_aux['fields']['time_baixa_ou_arquivamento'] = \
                        macrosteps_result[m]
                
                if m == 'Audiência':
                    json_vara_aux['fields']['time_audiencia'] = \
                        macrosteps_result[m]

                if m == 'Citação':
                    json_vara_aux['fields']['time_citacao'] = \
                        macrosteps_result[m]

                if m == 'Outros':
                    json_vara_aux['fields']['time_outros'] = \
                        macrosteps_result[m]
        
            json_vara.append(json_vara_aux)

            if group not in amount_of_varas:
                amount_of_varas[group] = 0
            
            amount_of_varas[group] += 1

            # create json Steps

            macro_trace_freq = ms.get_macro_trace(freq=True)
            macro_trace_time = ms.get_macro_trace(freq=False)

            # rescale macrosteps
            total = sum(macro_trace_time.values())

            # for m in macrosteps_result:
            #     macrosteps_result[m] = int((macrosteps_result[m] / total)\
            #         * days_finish_process)

            # print('')
            # print('macro_trace_freq: ', str(macro_trace_freq))
            # print('macro_trace_time: ', str(macro_trace_time))
            # print('')


            for m in macro_trace_freq:
                if macro_trace_time[m] > 0:
                    json_steps_aux = {'model':'performance.Steps',
                                'pk':step_id_count,
                                'fields':{}
                                }
                    json_steps_aux['fields']['step_id'] = \
                        json_step_config_map[m]
                    json_steps_aux['fields']['vara_id'] = \
                        vara_id_count
                
                    json_steps_aux['fields']['frequency'] = \
                        macro_trace_freq[m]
                    json_steps_aux['fields']['med_time'] = \
                        macro_trace_time[m]
                    json_steps_aux['fields']['comment_id'] = \
                        20 + int(random.random()*len_comments)

                    json_steps.append(json_steps_aux)
                    
                    step_id_count += 1


            # print('current json_steps:')
            # print(json_steps)

            vara_id_count += 1 
        else:
            number_of_skips[group] += 1


print('total skips: ' + str(number_of_skips))

# check times distribution

for k in ranking_varas:
    print('group is: ' + str(k))
    print('number of varas: ' +str(amount_of_varas[k]))

    times = np.array(list(ranking_varas[k].values()))
    print('times: ' + str(times))

    quantile1 = np.percentile(times, 25)
    quantile3 = np.percentile(times, 75)
    upper_bound = quantile3 + (0.5*quantile3)
    lower_bound = quantile1 - (-1.5*quantile1)
    std = np.std(times)
    mean = np.mean(times)

    print('quantile3: ' + str(quantile3))
    print('upper_bound: ' + str(upper_bound))
    print('quantile1: ' + str(quantile1))
    print('lower_bound: ' + str(lower_bound))
    print('upper std: ' + str(mean + 1.5 * std))
    print('lower std: ' + str(mean - 1.5 * std))
    print('std: ' +str(std))
    print('mean: ' +str(mean))


    outliers_up = [x for x in times if x > mean + 1.5 * std]
    outliers_down = [x for x in times if x < mean - 1.5 * std]

    print('outlier up times: ' + str(outliers_up))
    print('outlier down times: ' + str(outliers_down))


    plt.hist(times, bins=int(amount_of_varas[k]))
    plt.show()


# add ranking

for group in ranking_varas:
    ranking_varas[group] = \
        {k: v for k, v in sorted(ranking_varas[group].items(), 
                                 key=lambda item: item[1])}

print('ranking_varas: ', str(ranking_varas))

for vara in json_vara:
    vara['fields']['ranking'] = \
        list(ranking_varas[vara['fields']['group_id']]).\
            index(vara['pk']) + 1

group0['fields']['amount_of_varas'] = amount_of_varas[group0['pk']]
group1['fields']['amount_of_varas'] = amount_of_varas[group1['pk']]
group2['fields']['amount_of_varas'] = amount_of_varas[group2['pk']]
group3['fields']['amount_of_varas'] = amount_of_varas[group3['pk']]
group4['fields']['amount_of_varas'] = amount_of_varas[group4['pk']]
# group5['fields']['amount_of_varas'] = amount_of_varas[group5['pk']]
# group6['fields']['amount_of_varas'] = amount_of_varas[group6['pk']]

json_group.append(group0)
json_group.append(group1)
json_group.append(group2)
json_group.append(group3)
json_group.append(group4)
# json_group.append(group5)
# json_group.append(group6)


with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_groups.json', 'w') as f:
          json.dump(json_group, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_varas.json', 'w') as f:
          json.dump(json_vara, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps.json', 'w') as f:
          json.dump(json_steps, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps.json', 'w') as f:
          json.dump(json_steps, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_steps_config.json', 'w') as f:
          json.dump(json_step_config, f)

with open('/home/vercosa/Insync/doutorado/hackaton_cnj/backend_git/'+\
          'backend-desafio-cnj/Fixtures/base5_comments.json', 'w') as f:
          json.dump(json_comments, f)
          