from pm4py.visualization.dfg import visualizer as dfg_visualization


def dfg_visualizer(dfg, 
                   log, 
                   variant=dfg_visualization.Variants.FREQUENCY):
    gviz = dfg_visualization.apply(dfg, 
                                   log=log, 
                                   variant=variant)
    dfg_visualization.view(gviz)