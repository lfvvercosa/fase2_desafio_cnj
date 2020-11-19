import statistics
import networkx as nx
import matplotlib.pyplot as plt

from log.Log import Log
from log.PreProcess import PreProcess
from utils.System import DEBUG

class MacroSteps():
    def __init__(self, log, macrosteps):
        self.log = log
        self.macrosteps = macrosteps


    def create_transition(self, orig, name, time, tran_dict):

        if orig:
            time_elapsed = (time - orig[1]).days
            key = orig[0] + ' -> ' + name

            # if key not in tran_dict:
            #     tran_dict[key] = []
            
            tran_dict[key] = time_elapsed



    def find_macro_trace(self, trace, macrosteps):

        tran_dict = {}
        orig = None
        
        for (idx,activ) in enumerate(trace):

            # print('### activ')
            # print(activ)
            # print('')

            name = activ['concept:name']
            time = activ['time:timestamp']

            if idx == 0 and name not in macrosteps:
                orig = ('Outros', activ['time:timestamp'])

            if name in macrosteps:
                macrosteps.remove(name)
                self.create_transition(orig, name, time, tran_dict)

                orig = (name, time)

            elif idx == len(trace) - 1:
                name = 'Baixa/Arquivamento'
                self.create_transition(orig, name, time, tran_dict)


        return tran_dict


    def find_all_macro_trace(self, log, macrosteps, freq=True):

        traces = {}
        all_macro_trace = {}

        for trace in log:

            # print('### trace')
            # print(trace)
            # print('')

            my_macrosteps = macrosteps.copy()
            tran_dict = self.find_macro_trace(trace, my_macrosteps)

            if freq:

                for tran in tran_dict:
                    if tran not in all_macro_trace:
                        all_macro_trace[tran] = 0

                    all_macro_trace[tran] += 1
            
            else:

                for tran in tran_dict:
                    if tran not in all_macro_trace:
                        all_macro_trace[tran] = []

                    all_macro_trace[tran].append(tran_dict[tran])

        if not freq:
            for key in all_macro_trace:
                all_macro_trace[key] = \
                    statistics.median(all_macro_trace[key])


        return all_macro_trace


    def create_macro_graph(self, trace):
        
        G = nx.DiGraph()

        for key in trace:
            (orig, dest) = key.split(' -> ')
            G.add_edge(orig, dest, weight=trace[key])

        return G


    def graph_most_frequent_path(self,
                                 G, 
                                 orig='Distribuição', 
                                 dest='Baixa/Arquivamento',
                                ):
        most_frequent = 0
        most_frequent_path = -1
        simple_paths = list(nx.all_simple_paths(G, 
                                                source=orig,
                                                target=dest))

        for idx_path, path in enumerate(simple_paths):
            
            # print(path)
            count = 0

            for idx_act,act in enumerate(path):
                if idx_act + 1 < len(path):
                    orig = path[idx_act]
                    dest = path[idx_act+1]
                    count += G[orig][dest]['weight']     

            if count > most_frequent:
                most_frequent = count
                most_frequent_path = idx_path
        
            # print('most_frequent_path: ', str(most_frequent_path))

        return simple_paths[most_frequent_path]


    def get_time_most_freq_path(self, G, path, macro_trace_time):
        
        G_time = self.create_macro_graph(macro_trace_time)

        time_most_freq = {}

        for idx_act, act in enumerate(path):
            if idx_act + 1 < len(path):
                    orig = path[idx_act]
                    dest = path[idx_act+1]
                    time = G[orig][dest]['weight']
                    time_most_freq[orig + ' -> ' + dest] = time 

        return time_most_freq
    

    def filter_less_frequent_activ(self, G_freq, percent=0.05):
        less_freq = []
        dict_freq = nx.get_edge_attributes(G_freq,'weight')
        total_freq = sum(list(dict_freq.values()))

        for key in dict_freq:
            if dict_freq[key]/total_freq < percent:
                less_freq.append(key)

        return less_freq


    def filter_instantaneous_transitions(self, G_time):
        filt = []
        dict_time = nx.get_edge_attributes(G_time,'weight')

        for key in dict_time:
            if dict_time[key] == 0.0:
                filt.append(key)

        return filt    


    def remove_keys(self, my_dict, l):
        for k in l:
            my_dict.pop(k, None)

        return my_dict


    def get_time_percentage_activ(self, G_time, less_freq):
        time_percent_macrosteps = {}
        instant_transit = self.filter_instantaneous_transitions(G_time)

        # print('less_freq: ', str(less_freq))
        # print('')
        # print('instant_transit: ', str(instant_transit))
        # print('')

        edge_times = nx.get_edge_attributes(G_time,'weight')
        edge_times = self.remove_keys(edge_times, less_freq)
        edge_times = self.remove_keys(edge_times, instant_transit)

        # rebuild the Graph
        weighted_edges = []

        for key in edge_times:
            weighted_edges.append((key[0], key[1], edge_times[key]))

        G = nx.DiGraph()
        G.add_weighted_edges_from(weighted_edges)
        nodes = list(G.nodes)

        # print('edge_times: ', str(edge_times))
        # print('')

        # print('nodes: ', str(nodes))
        # print('')
        
        for n in nodes:
            node_edges = G.out_edges(n)
            total_edges = len(node_edges)

            if total_edges > 0:
                time_percent_macrosteps[n] = 0

                for e in node_edges:
                    time_percent_macrosteps[n] += edge_times[e]
                time_percent_macrosteps[n] /= total_edges
        
        # print('time_macrosteps: ', str(time_percent_macrosteps))

        total_time = sum(list(time_percent_macrosteps.values()))

        for key in time_percent_macrosteps:
            time_percent_macrosteps[key] = \
                round((time_percent_macrosteps[key] / total_time) * 100,2)
        
        # print('')
        # print('time_pecent_macrosteps: ', str(time_percent_macrosteps))

        return time_percent_macrosteps


    def calc_macrosteps(self):
        
        macro_trace_freq = self.find_all_macro_trace(self.log, 
                                                     self.macrosteps, 
                                                     freq=True)
        macro_trace_time = self.find_all_macro_trace(self.log, 
                                                     self.macrosteps, 
                                                     freq=False) 

        # time_macrosteps = {}

        if(DEBUG):
            print('macro_trace_freq: ', str(macro_trace_freq))
        
        G_freq = self.create_macro_graph(macro_trace_freq)
        G_time = self.create_macro_graph(macro_trace_time)

        # pos=nx.spring_layout(G)
        # pos=nx.get_node_attributes(G,'pos')
        # nx.draw(G, with_labels = True, pos=pos)
        # labels = nx.get_edge_attributes(G,'weight')
        # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        # plt.show()

        # path_number = self.graph_most_frequent_path(G)

        # time_edges = self.get_time_most_freq_path(G, 
        #                                           path_number, 
        #                                           macro_trace_time)

        # if(DEBUG):
        #     print('time edges: ', str(time_edges))

        # for key in time_edges:
        #     time_macrosteps[key.split(' -> ')[0]] = time_edges[key]
        
        less_freq = \
            self.filter_less_frequent_activ(G_freq, percent=0.05)
        time_macrosteps =  \
            self.get_time_percentage_activ(G_time, less_freq)

        return time_macrosteps


    def get_macro_trace(self, freq=True):
        macro_trace = self.find_all_macro_trace(self.log, 
                                                self.macrosteps, 
                                                freq=freq)
                                        
        return macro_trace

