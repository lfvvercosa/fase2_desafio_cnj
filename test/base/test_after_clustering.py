import pandas as pd
import matplotlib.pyplot as plt

from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.statistics.traces.log import case_statistics
from pm4py.algo.discovery.dfg import parameters
from pm4py.visualization.dfg import visualizer as dfg_visualization

from log.Log import Log
from log.Log import INTENSE_FILTERING
from discovery.DFG import DFG
import visualization.Visualizer as Visualizer
from log.PreProcess import PreProcess

file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'log_vara_2.csv'


p = PreProcess(file_location=file_path)
p.select_desired_columns()
p.filter_outlier_timestamp()
p.filter_outlier_movements(lower=0.01, upper=0.99)
p.filter_outlier_trace_time(lower=0.01, upper=0.99)

l = Log(df_log=p.df_log.sort_values('time:timestamp'))
# l.filter_variants(1.1)

dfg = DFG(l.log,
          parameters={parameters.Parameters.AGGREGATION_MEASURE:'mean'},
          variant=dfg_discovery.Variants.FREQUENCY)

dfg.filter_activities(number_act=10)
dfg.filter_edges(percentage=0.3)

print(dfg.dfg)

Visualizer.\
    dfg_visualizer(dfg.dfg, 
                   l.log,
                   variant=dfg_visualization.Variants.FREQUENCY)


