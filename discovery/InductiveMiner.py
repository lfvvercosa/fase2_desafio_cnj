from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.discovery.inductive.parameters import Parameters


class InductiveMiner():
    def __init__(self,
                 log,
                 parameters=None):

        self.net, self.initial_marking, self.final_marking = \
            inductive_miner.apply(log,
                                  parameters={Parameters.NOISE_THRESHOLD:0.5},
                                  variant=inductive_miner.IMf)