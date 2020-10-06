from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.statistics.traces.log import case_statistics
from pm4py.algo.filtering.log.variants import variants_filter


LOW_FILTERING = 1
MODERATE_FILTERING = 2
INTENSE_FILTERING = 4


class Log():
    def __init__(self, file_location):
        self.log = xes_importer.apply(file_location)


    def filter_variants(self, filter_level):
        variants_count = case_statistics.get_variant_statistics(self.log)
        variants_count = \
            sorted(variants_count, 
                   key=lambda x: x['count'], 
                   reverse=True)
        total_traces = len(self.log)
        total_variants = len(variants_count)
        filter_threshold = (1/total_variants) * filter_level

        desired_variants = \
            [v['variant'] for v in variants_count \
                  if v['count']/total_traces >= filter_threshold]
        self.log = variants_filter.apply(self.log, desired_variants)

