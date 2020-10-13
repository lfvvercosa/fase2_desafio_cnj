from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.visualization.petrinet import visualizer as pn_visualizer


def dfg_visualizer(dfg, 
                   log, 
                   variant=dfg_visualization.Variants.FREQUENCY):
    gviz = dfg_visualization.apply(dfg, 
                                   log=log, 
                                   variant=variant)
    dfg_visualization.view(gviz)


def petrinet_visualizer(net,
                        initial_marking,
                        final_marking,
                        parameters=
                            {pn_visualizer.Variants.WO_DECORATION.\
                                value.Parameters.FORMAT:"png"}):
    gviz = pn_visualizer.apply(net, 
                               initial_marking, 
                               final_marking, 
                               parameters=parameters)
    pn_visualizer.view(gviz)