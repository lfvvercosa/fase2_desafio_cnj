from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.statistics.traces.log import case_statistics
from pm4py.algo.filtering.log.variants import variants_filter
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.statistics.traces.log import case_statistics


LOW_FILTERING = 1
MODERATE_FILTERING = 4
INTENSE_FILTERING = 8


class Log():
    def __init__(self, file_location=None, df_log=None):
        if df_log is None:
            self.log = xes_importer.apply(file_location)
        else:
            self.log = log_converter.apply(df_log)


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


    def median_time(self):
        median_case_duration = case_statistics.\
            get_median_caseduration(self.log, parameters={
            case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"
            })
            
        return median_case_duration

