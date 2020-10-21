import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt
import statistics

from log.Log import Log
from log.PreProcess import PreProcess
from process.MacroSteps import MacroSteps
from discovery.DFG import DFG
import visualization.Visualizer as Visualizer

from pm4py.statistics.traces.log import case_statistics


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/df_movimentos.csv'

vara = '2ª VARA C�?VEL DE SANTANA'

macrosteps = [
              
              'Distribuição', 
              'Conclusão',
              'Despacho',
              'Decisão',
              'Julgamento',
              'Trânsito em julgado', 
              'Baixa/Arquivamento',  
             ]

pp = PreProcess(file_location=file_path)
pp.select_desired_columns()
pp.filter_outlier_timestamp()
pp.map_movements(movement_path)

df_log = pp.df_log
df_vara = df_log[df_log['case: orgao'] == vara]

pp_vara = PreProcess(df=df_vara)
pp_vara.filter_outlier_movements(lower=0.05, upper=0.95)
pp_vara.filter_outlier_trace_time(lower=0.05, upper=0.95)

log = Log(df_log=pp_vara.df_log.sort_values('time:timestamp'))

median_case_duration = case_statistics.\
  get_median_caseduration(log.log, parameters={
    case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"
})

print('median case duration: ', str(median_case_duration/ (24*60*60)))

ms = MacroSteps(log.log, macrosteps)

res = ms.calc_macrosteps()

print(res)


