import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt
import statistics

from log.Log import Log
from log.PreProcess import PreProcess
from discovery.DFG import DFG
import visualization.Visualizer as Visualizer


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')

df_log['case: orgao'] = df_log['case: orgao'].str.strip()
df_log['concept:name'] = df_log['concept:name'].str.strip()

df_log = df_log[['case:concept:name',
                 'concept:name_cod',
                 'concept:name',
                 'case: orgao',
                 'time:timestamp']]

# change movements code

# create movement df


movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/df_movimentos.csv'

df_mov = pd.read_csv(movement_path,
                     engine='python')

df_mov = df_mov[['breadscrum', 'cod_item', 'nome']]
df_mov = df_mov.rename(columns={'cod_item':'concept:name_cod'})


# change movements names

reg = '\:(.*?)\:'                
df_mov['father_mov_code']  = df_mov['breadscrum'].str.\
                                findall(reg, flags=re.I).str[0]
df_mov['father_mov_code'].fillna(df_mov['concept:name_cod'], 
                                 inplace=True)
df_mov['father_mov_code'] = df_mov['father_mov_code'].astype(int)
df_mov.loc[((df_mov['concept:name_cod'] == 22) |
            (df_mov['concept:name_cod'] == 246)),\
             'nome'] = 'Baixa/Arquivamento'
# change 'Magistrado' movimentos to uppest father
df_mov.loc[(df_mov['father_mov_code'] == 193),\
             'nome'] = 'Julgamento'
df_mov.loc[(df_mov['father_mov_code'] == 11009),\
             'nome'] = 'Despacho'
df_mov.loc[(df_mov['father_mov_code'] == 3),\
             'nome'] = 'Decisão'



len_before = len(df_log)

df_log = df_log.merge(df_mov[['concept:name_cod', 'nome']], 
                      on='concept:name_cod', 
                      how='left')

len_after = len(df_log)


print('number of lines diff: ', str(len_after - len_before))

df_log.drop('concept:name', inplace=True, axis=1)
df_log = df_log.rename(columns={'nome':'concept:name'})


######## create algorithm


### find most common trace among processes in same vara


def create_transition(orig, name, time, tran_dict):

    if orig:
        time_elapsed = (time - orig[1]).days
        key = orig[0] + ' -> ' + name

        # if key not in tran_dict:
        #     tran_dict[key] = []
        
        tran_dict[key] = time_elapsed



def find_macro_trace(trace, macrosteps):

    tran_dict = {}
    orig = None
    
    for (idx,activ) in enumerate(trace):

        # print('### activ')
        # print(activ)
        # print('')

        name = activ['concept:name']
        time = activ['time:timestamp']

        if idx == 0 and name not in macrosteps:
            orig = ('Distribuição', activ['time:timestamp'])

        if name in macrosteps:
            macrosteps.remove(name)
            create_transition(orig, name, time, tran_dict)

            orig = (name, time)

        elif idx == len(trace) - 1:
            name = 'Baixa/Arquivamento'
            create_transition(orig, name, time, tran_dict)


    return tran_dict


def find_all_macro_trace(log, macrosteps, freq=True):

    traces = {}
    all_macro_trace = {}

    for trace in log:

        # print('### trace')
        # print(trace)
        # print('')

        my_macrosteps = macrosteps.copy()
        tran_dict = find_macro_trace(trace, my_macrosteps)

        if freq:

            for tran in tran_dict:
                if tran not in all_macro_trace:
                    all_macro_trace[tran] = 0

                all_macro_trace[tran] += 1
        
        else:

            for tran in tran_dict:
                if tran not in all_macro_trace:
                    all_macro_trace[tran] = []

                all_macro_trace[tran].append(tran_dict[tran])

    if not freq:
        for key in all_macro_trace:
            all_macro_trace[key] = \
                statistics.median(all_macro_trace[key])


    return all_macro_trace


def find_all_process_most_frequent(varas_group):

    macro_trace_processes = {}

    for vara in varas_group:
        df_vara = df_log[df_log['case: orgao'] == vara]

        p = PreProcess(df=df_vara)
        p.select_desired_columns()
        p.filter_outlier_timestamp()
        p.filter_outlier_movements(lower=0.05, upper=0.95)
        p.filter_outlier_trace_time(lower=0.05, upper=0.95)

        l = Log(df_log=p.df_log.sort_values('time:timestamp'))
        all_macro_trace = find_all_macro_trace(l.log, macrosteps)

        for tran in all_macro_trace:
            if tran not in macro_trace_processes:
                macro_trace_processes[tran] = 0
            macro_trace_processes[tran] += 1

    macro_trace_processes = {k: v for k, v in \
        sorted(macro_trace_processes.items(), 
            key=lambda item: item[1])}

    macro_trace_processes


def create_macro_graph(trace):
    
    G = nx.DiGraph()

    for key in trace:
        (orig, dest) = key.split(' -> ')
        G.add_edge(orig, dest, weight=trace[key])

    return G


def graph_most_frequent_path(G, 
                             orig='Distribuição', 
                             dest='Baixa/Arquivamento',
                             ):
    most_frequent = 0
    most_frequent_path = -1
    simple_paths = list(nx.all_simple_paths(G, 
                                            source=orig,
                                            target=dest))

    for idx_path, path in enumerate(simple_paths):
        
        print(path)
        count = 0

        for idx_act,act in enumerate(path):
            if idx_act + 1 < len(path):
                orig = path[idx_act]
                dest = path[idx_act+1]
                count += G[orig][dest]['weight']     

        if count > most_frequent:
            most_frequent = count
            most_frequent_path = idx_path
    
        # print('most_frequent_path: ', str(most_frequent_path))

    return simple_paths[most_frequent_path]


def get_time_most_freq_path(path, macro_trace_time):
    
    G_time = create_macro_graph(macro_trace_time)

    time_most_freq = {}

    for idx_act, act in enumerate(path):
        if idx_act + 1 < len(path):
                orig = path[idx_act]
                dest = path[idx_act+1]
                time = G[orig][dest]['weight']
                time_most_freq[orig + ' -> ' + dest] = time 

    return time_most_freq

macrosteps = [
              
              'Distribuição', 
              'Conclusão',
              'Despacho',
              'Decisão',
              'Julgamento',
              'Remessa',
              'Baixa/Arquivamento',  
            #   'Trânsito em julgado', 
             ]

group_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'processos_grupo_all.csv'

df_group = pd.read_csv(group_path,
                       sep=';', 
                       engine='python')

df_group = df_group[df_group['process_count'] > 50]
varas_group = df_group['case: orgao'].tolist() 


vara = 'Porto Velho - 2ª Vara de Execuções Fiscais'

df_vara = df_log[df_log['case: orgao'] == vara]

p = PreProcess(df=df_vara)
p.select_desired_columns()
p.filter_outlier_timestamp()
p.filter_outlier_movements(lower=0.05, upper=0.95)
p.filter_outlier_trace_time(lower=0.05, upper=0.95)

l = Log(df_log=p.df_log.sort_values('time:timestamp'))

macro_trace_freq = find_all_macro_trace(l.log, macrosteps, freq=True)
macro_trace_time = find_all_macro_trace(l.log, macrosteps, freq=False) 
                                            

macro_trace_freq

G = create_macro_graph(macro_trace_freq)

nx.draw(G, with_labels = True)

plt.show()

path_number = graph_most_frequent_path(G)

get_time_most_freq_path(path_number, macro_trace_time)

