import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np


df_teste = pd.DataFrame({'a': [1,2,3,5,9,8], 
                         'b': [2,3,4,7,10,9], 
                         'c':['dd','ee','ff','ee','qa','mn'], 
                         'd':[1,1,2,6,9,8]})


df_teste

assuntos_cols = list(df_teste)
assuntos_cols.remove('c')

df_teste['total'] = df_teste[assuntos_cols].sum(axis=1)
df_teste.loc[:, assuntos_cols] = \
    df_teste.loc[:, assuntos_cols].div(df_teste['total'], axis=0)

df_teste.loc[:, assuntos_cols] = \
    df_teste.loc[:, assuntos_cols].round(3)

df_teste



df_teste['total'] = (df_teste['total']-df_teste['total'].min()) \
    /(df_teste['total'].max()-df_teste['total'].min())

df_teste

assuntos_cols.append('total')

df_np = df_teste[assuntos_cols].to_numpy()
clustering = DBSCAN(eps=0.15, min_samples=2).fit(df_np)
clustering.labels_

# X = np.array([[1, 2], [2, 2], [2, 3],
#               [8, 7], [8, 8], [25, 80]])


# clustering = DBSCAN(eps=3, min_samples=2).fit(X)
# clustering.labels_

# clustering
