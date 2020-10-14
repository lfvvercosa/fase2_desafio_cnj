# from log import Log
# from discovery.DFG import DFG
# import visualization.Visualizer as Visualizer

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



# file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
#             'sample/tjba_sample.csv'
file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'log_vara3.csv'


# datatypes = [('case:concept:name','S10'),
#              ('time:timestamp','S10')]

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')

df_log['case:concept:name'] = df_log['case:concept:name'].str.strip()
df_log['time:timestamp'] = df_log['time:timestamp'].str.strip()
df_log['concept:name'] = df_log['concept:name'].str.strip()

df_log['case:concept:name'].nunique()

# remove instances with incorrect timestamp
df_incomplete = df_log[['case:concept:name', 'time:timestamp']]
df_incomplete['year'] = df_incomplete['time:timestamp'].str[:4].astype(int)
df_incomplete = df_incomplete[(df_incomplete['year'] < 1900) | \
                              (df_incomplete['year'] > 2020)]
df_incomplete = df_incomplete.drop_duplicates(subset=['case:concept:name'])
df_incomplete['case:concept:name'].nunique()

# df_incomplete = df_log[df_log['time:timestamp'].str.len() < 14]
# df_incomplete = df_incomplete.drop_duplicates(subset=['case:concept:name'])
# df_incomplete['case:concept:name'].nunique()

key = ['case:concept:name']
i1 = df_log.set_index(key).index
i2 = df_incomplete.set_index(key).index

# df_log = df_log[~i1.isin(i2)]
df_log['case:concept:name'].nunique()

df_log['time:timestamp'] = \
    pd.to_datetime(df_log['time:timestamp'], utc=True, format='%Y%m%d%H%M%S')

df_log = df_log[['case:concept:name',
                 'concept:name',
                 'concept:name_cod',
                 'time:timestamp']]

df_log = df_log.sort_values('time:timestamp')

df_hist = df_log.groupby('case:concept:name').count().\
    sort_values('concept:name')

# filter outliers of number of movements [0.05, 0.95]
lower_bound = df_hist['concept:name'].quantile(0.05)
upper_bound = df_hist['concept:name'].quantile(0.95)
df_hist = df_hist[(df_hist['concept:name'] < lower_bound) |
                  (df_hist['concept:name'] > upper_bound)]
df_hist.reset_index(level=0, inplace=True)

df_log['case:concept:name'].nunique()
key = ['case:concept:name']
i1 = df_log.set_index(key).index
i2 = df_hist.set_index(key).index

# df_log = df_log[~i1.isin(i2)]
df_log['case:concept:name'].nunique()

df_time = df_log.copy()

df_time['time:timestamp2'] = df_time['time:timestamp']

df_time = df_time.groupby('case:concept:name').\
            agg({'time:timestamp' : min, 'time:timestamp2': max})

df_time['duration'] = \
    (df_time['time:timestamp2'] - df_time['time:timestamp']).dt.days

lower_bound = int(df_time.quantile(0.05))
upper_bound = int(df_time.quantile(0.95))

df_time = df_time[(df_time['duration'] < lower_bound) |
                  (df_time['duration'] > upper_bound)]

df_time.count()
df_time.reset_index(level=0, inplace=True)


df_log['case:concept:name'].nunique()

key = ['case:concept:name']
i1 = df_log.set_index(key).index
i2 = df_time.set_index(key).index

# df_log = df_log[~i1.isin(i2)]

df_log['case:concept:name'].nunique()

# log = log_converter.apply(df_log)

l = Log(df_log=df_log)
l.filter_variants(1)
dfg = DFG(l.log,
          parameters={parameters.Parameters.AGGREGATION_MEASURE:'mean'},
          variant=dfg_discovery.Variants.PERFORMANCE)


print(dfg.dfg)

Visualizer.dfg_visualizer(dfg.dfg, 
                          l.log,
                          variant=dfg_visualization.Variants.PERFORMANCE)

print('teste')