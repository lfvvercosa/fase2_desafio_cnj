
from log.Log import Log
from pm4py.statistics.traces.log import case_statistics
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from discovery.DFG import DFG
import visualization.Visualizer as Visualizer


# file_path = 'log/examples/running-example.xes'
file_path = 'log/examples/Receipt phase of an environmental permit' + \
			' application process (_WABO_) CoSeLoG project.xes'


l = Log(file_path)

# variants_count = case_statistics.get_variant_statistics(l.log)
# variants_count = \
#     sorted(variants_count, 
#            key=lambda x: x['count'], 
#            reverse=True)

# print('')
# print(variants_count)
# print('')

l.filter_variants(Log.INTENSE_FILTERING)

# dfg_discovery.apply(l.log)

dfg = DFG(l.log)

Visualizer.dfg_visualizer(dfg.dfg, l.log)


# variants_count = case_statistics.get_variant_statistics(l.log)
# variants_count = \
#     sorted(variants_count, 
#            key=lambda x: x['count'], 
#            reverse=True)

# print('')
# print(variants_count)
# print('')