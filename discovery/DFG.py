from pm4py.algo.discovery.dfg import algorithm as dfg_discovery


class DFG():
    def __init__(self, 
                 log, 
                 parameters=None, 
                 variant=dfg_discovery.Variants.FREQUENCY):
                 
        self.dfg = dfg_discovery.apply(log,
                                       parameters=parameters,
                                       variant=variant)

