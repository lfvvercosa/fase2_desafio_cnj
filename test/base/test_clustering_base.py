from log.Log import Log
from log.PreProcess import PreProcess
from discovery.DFG import DFG
import visualization.Visualizer as Visualizer

from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.algo.discovery.dfg import parameters

import pandas as pd
import pickle
import numpy as np
import json

file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

group_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'processos_grupo_all.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')

df_group = pd.read_csv(group_path,
                     sep=';', 
                     engine='python')

df_group = df_group[df_group['process_count'] > 50]
varas_group = df_group['case: orgao'].tolist()

dfg_dict = {}

act_dict = {}
act_dict_temp = {}
similar_group = {}
similar_group_ref = {}


for vara in varas_group:
    df_temp = df_log[df_log['case: orgao'] == vara]
    p = PreProcess(df=df_temp)
    p.select_desired_columns()
    p.filter_outlier_timestamp()
    p.filter_outlier_movements(lower=0.01, upper=0.99)
    p.filter_outlier_trace_time(lower=0.01, upper=0.99)
    l = Log(df_log=p.df_log.sort_values('time:timestamp'))
    # l.filter_variants(1)
    dfg = DFG(l.log)
    dfg.filter_activities(number_act=10)
    dfg.filter_edges(percentage=0.3)
    dfg_dict[vara] = list(dfg.dfg)


for vara in dfg_dict.keys():
    act_dict[vara] = (list(set([item for sublist in dfg_dict[vara] \
                                    for item in sublist])),
                      [item for item in dfg_dict[vara]])

for vara in act_dict.keys():
    if act_dict[vara][0] and act_dict[vara][1]:
        act_dict_temp[vara] = act_dict[vara]

act_dict = act_dict_temp


def is_similar(l1, l2, threshold=0.8, tol=0.3):
    similar_list = []
    if len(l2) > (1 + tol) * len(l1) or \
       len(l2) < (1 - tol) * len(l1):
       return False
    count = 0
    
    for act in l1:
        if act in l2:
            similar_list.append(act)
            count += 1
    
    is_sim = count >= threshold * len(l1)

    if is_sim:
        return similar_list
    else:
        return []


def run_similar_group(threshold_act=0.8,
                      tol_act=0.3,
                      threshold_edge=0.4,
                      tol_edge=0.5):
    global similar_group
    global similar_group_ref

    similar_group = {}
    similar_group_ref = {}

    for vara in act_dict.keys():
        similar_group[vara] = []
        similar_group_ref[vara] = []

        for vara2 in act_dict.keys():
            if vara != vara2:
                act_simil = is_similar(act_dict[vara][0], 
                                       act_dict[vara2][0],
                                       threshold=threshold_act,
                                       tol=tol_act)

                if act_simil:
                    edg_simil = is_similar(act_dict[vara][1], 
                                           act_dict[vara2][1],
                                           threshold=threshold_edge,
                                           tol=tol_edge)
                    if edg_simil:
                        similar_group[vara].append({vara2:(act_simil,
                                                           edg_simil)})
                        similar_group_ref[vara].append(vara2)

run_similar_group(threshold_act=0.8,
                  tol_act=0.3,
                  threshold_edge=0.8,
                  tol_edge=0.3)

# similar_group

json.dump(similar_group, 
          open('/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'similar_groups.json', 'w'))

json.dump(similar_group_ref, 
          open('/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'similar_groups_ref.json', 'w'))

print('done!')

#####################

varas = ["2ª VARA C�?VEL E DE FAZENDA PÚBLICA DE MACAP�?",
         "4ª VARA C�?VEL E DE FAZENDA PÚBLICA DE MACAP�?",
         "1ª VARA C�?VEL E DE FAZENDA PÚBLICA DE MACAP�?"]

count = 1
for vara in varas:
    df_temp = df_log[df_log['case: orgao'] == vara]
    df_temp.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                               'log_vara_'+str(count)+'.csv', 
                   sep=';', 
                   index=False)
    count += 1

