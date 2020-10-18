from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from collections import Counter


class DFG():
    def __init__(self, 
                 log, 
                 parameters=None, 
                 variant=dfg_discovery.Variants.FREQUENCY):
                 
        self.dfg = dfg_discovery.apply(log,
                                       parameters=parameters,
                                       variant=variant)


    def __filter_orphans_activities(self):
        edges = self.dfg.most_common()
        lonely_act = []
        new_dfg = {}

        for e in edges:
            if e[0][0] == e[0][1]:
                lonely_act.append(e[0][0])

        for e in edges:
            if e[0][0] in lonely_act and \
               e[0][0] != e[0][1]:
               lonely_act.remove(e[0][0])

        for e in edges:
            if e[0][0] not in lonely_act:
                new_dfg[e[0]] = e[1] 
        
        self.dfg = Counter(new_dfg)


    def filter_edges(self, percentage = 0.8):

        number_of_edges = len(self.dfg)
        most_common_list = self.dfg.\
            most_common(int(percentage * number_of_edges))

        new_dfg = {}

        for e in most_common_list:
            new_dfg[e[0]] = e[1]

        self.dfg = Counter(new_dfg)
        self.__filter_orphans_activities()

    
    def filter_activities(self, percentage = -1, number_act = -1):
        
        all_activities = list(set([item for sublist in \
            list(self.dfg.elements()) for item in sublist]))
        all_activities = list(set(all_activities))
        act_dict = {}
        act_frequent = []
        edges = self.dfg.most_common()
        new_dfg = {}
        
        if percentage != -1:
            pos_last_act = int(len(all_activities)*percentage)
        else:
            pos_last_act = number_act

        for act in all_activities:
            act_dict[act] = 0
        
        for edge in self.dfg.most_common():
            act_dict[edge[0][0]] +=  edge[1]

            if act_dict[edge[0][0]] != act_dict[edge[0][1]]:
                act_dict[edge[0][1]] +=  edge[1]
        
        # sort by frequency
        temp = list(sorted(act_dict.items(), 
                    key=lambda item: item[1],
                    reverse=True))

        act_frequent = [x[0] for x in temp][:pos_last_act]

        for edge in edges:
            if edge[0][0] in act_frequent and \
               edge[0][1] in act_frequent:
               new_dfg[edge[0]] = edge[1]
        
        self.dfg = Counter(new_dfg)
        self.__filter_orphans_activities()


