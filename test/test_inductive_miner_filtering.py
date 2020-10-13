
from log import Log
from pm4py.statistics.traces.log import case_statistics
from discovery.InductiveMiner import InductiveMiner
from pm4py.algo.discovery.inductive.parameters import Parameters
import visualization.Visualizer as Visualizer


# file_path = 'log/examples/running-example.xes'
file_path = 'log/examples/Receipt phase of an environmental permit' + \
			' application process (_WABO_) CoSeLoG project.xes'


l = Log.Log(file_path)

# variants_count = case_statistics.get_variant_statistics(l.log)
# variants_count = \
#     sorted(variants_count, 
#            key=lambda x: x['count'], 
#            reverse=True)

# print('')
# print(variants_count)
# print('')

# l.filter_variants(Log.INTENSE_FILTERING)

# dfg_discovery.apply(l.log)

parameters = {Parameters.NOISE_THRESHOLD:True}

im = InductiveMiner(l.log, parameters)

for place in im.net.places:
	print("\nPLACE: "+place.name)
	for arc in place.in_arcs:
  		print(arc.source.name, arc.source.label)


Visualizer.petrinet_visualizer(im.net, 
							   im.initial_marking,
							   im.final_marking)


# variants_count = case_statistics.get_variant_statistics(l.log)
# variants_count = \
#     sorted(variants_count, 
#            key=lambda x: x['count'], 
#            reverse=True)

# print('')
# print(variants_count)
# print('')