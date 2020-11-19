import pandas as pd
import json
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

from log.Log import Log
from log.PreProcess import PreProcess
from process.MacroSteps import MacroSteps


def get_time_percentage_activ(G_time, less_freq):
    time_percent_macrosteps = {}
    instant_transit = filter_instantaneous_transitions(G_time)

    print('less_freq: ', str(less_freq))
    print('')
    print('instant_transit: ', str(instant_transit))
    print('')

    edge_times = nx.get_edge_attributes(G_time,'weight')
    edge_times = remove_keys(edge_times, less_freq)
    edge_times = remove_keys(edge_times, instant_transit)

    # rebuild the Graph
    weighted_edges = []

    for key in edge_times:
        weighted_edges.append((key[0], key[1], edge_times[key]))

    G = nx.DiGraph()
    G.add_weighted_edges_from(weighted_edges)
    nodes = list(G.nodes)

    print('edge_times: ', str(edge_times))
    print('')

    print('nodes: ', str(nodes))
    print('')
    
    for n in nodes:
        node_edges = G.out_edges(n)
        total_edges = len(node_edges)

        if total_edges > 0:
            time_percent_macrosteps[n] = 0

            for e in node_edges:
                time_percent_macrosteps[n] += edge_times[e]
            time_percent_macrosteps[n] /= total_edges
    
    print('time_macrosteps: ', str(time_percent_macrosteps))

    total_time = sum(list(time_percent_macrosteps.values()))

    for key in time_percent_macrosteps:
        time_percent_macrosteps[key] = \
            round((time_percent_macrosteps[key] / total_time) * 100,2)
    
    print('')
    print('time_pecent_macrosteps: ', str(time_percent_macrosteps))

    return time_percent_macrosteps


def filter_less_frequent_activ(G_freq, percent=0.05):
    less_freq = []
    dict_freq = nx.get_edge_attributes(G_freq,'weight')
    total_freq = sum(list(dict_freq.values()))

    for key in dict_freq:
        if dict_freq[key]/total_freq < percent:
            less_freq.append(key)
    
    return less_freq


def filter_instantaneous_transitions(G_time):
    filt = []
    dict_time = nx.get_edge_attributes(G_time,'weight')

    for key in dict_time:
        if dict_time[key] == 0.0:
            filt.append(key)
    
    return filt    


def remove_keys(my_dict, l):
    for k in l:
        my_dict.pop(k, None)
    return my_dict


macrosteps = [
              'Audiência',
              'Citação',
              'Conclusão',
              'Despacho',
              'Decisão',
              'Distribuição', 
              'Julgamento',
              'Trânsito em Julgado', 
              'Baixa/Arquivamento',
              'Outros',  
             ]

vara = 'CIANORTE - 1ª VARA CÍVEL E DA FAZENDA PÚBLICA - TJPR'
# vara = 'VARA CÍVEL - TJAC'
# vara = '1ª VARA DE EXECUÇÃO FISCAL E TRIBUTÁRIA - TJRN'

df_vara = df_log[df_log['case: orgao_mun'] == vara]
pp_vara = PreProcess(df=df_vara)
pp_vara.filter_outlier_movements(lower=0.05, upper=0.95)
pp_vara.filter_outlier_trace_time(lower=0.05, upper=0.95)
df_vara = pp_vara.df_log
log = Log(df_log=pp_vara.df_log.sort_values('time:timestamp'))

ms = MacroSteps(log.log, macrosteps)

macro_trace_freq = ms.find_all_macro_trace(ms.log, 
                                           ms.macrosteps, 
                                           freq=True)

macro_trace_time = ms.find_all_macro_trace(ms.log, 
                                           ms.macrosteps, 
                                           freq=False)


G_freq = ms.create_macro_graph(macro_trace_freq)
G_time3 = ms.create_macro_graph(macro_trace_time)

less_freq = filter_less_frequent_activ(G_freq, percent=0.05)
time = get_time_percentage_activ(G_time3.copy(), less_freq)

# pos=nx.spring_layout(G)
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G, with_labels = True, pos=pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.show()

