import pandas as pd
from sklearn.cluster import DBSCAN


assuntos_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/fase2_git/'+\
       'repositorio_fase_2/fase2_desafio_cnj/data/interim/clustering/'+\
       'df_grupo_assunto_g1.csv'

classes_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/fase2_git/'+\
       'repositorio_fase_2/fase2_desafio_cnj/data/interim/clustering/'+\
       'df_grupo_classe_g1.csv'

varas_signif_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
                    'versao7/varas_mais_que_24_processos.csv'

# classes_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/fase2_git/'+\
#        'repositorio_fase_2/fase2_desafio_cnj/data/interim/clustering/'+\
#        'df_grupo_classe_g1.csv'

df = pd.read_csv(assuntos_path,
                 sep=';',
                 engine='python')

df_classes = pd.read_csv(classes_path,
                         sep=';',
                         engine='python')

df_varas = pd.read_csv(varas_signif_path,
                       sep=';',
                       engine='python')


######### PADRONIZAR NOME DA UJ #########
# padrao é maiúsculo e sem sufixo 'g1'


df['Orgao'] = df['Orgao'].str.replace(' \(g1\)','')
df = df.rename(columns={'Orgao':'case: orgao_mun'})
df['case: orgao_mun'] = df['case: orgao_mun'].str.upper()
df['case: orgao_mun'] = df['case: orgao_mun'].str.replace('"','')
df['case: orgao_mun'] = df['case: orgao_mun'].\
    str.replace(' - ','-')
df['case: orgao_mun'] = df['case: orgao_mun'].\
    str.replace('-',' - ')


######### REMOVER VARAS COM MENOS DE 25 PROCESSOS #########
 
key = ['case: orgao_mun']
i1 = df.set_index(key).index
i2 = df_varas.set_index(key).index

df = df[i1.isin(i2)]


######### NORMALIZAR ASSUNTOS #########
# percentualmente por UJ

assuntos_cols = list(df)
assuntos_cols.remove('case: orgao_mun')

df['total'] = df[assuntos_cols].sum(axis=1)
df.loc[:, assuntos_cols] = \
    df.loc[:, assuntos_cols].div(df['total'], axis=0)

df.loc[:, assuntos_cols] = \
    df.loc[:, assuntos_cols].round(3)

######### NORMALIZAR COLUNA 'total' #########
# única que precisa de normalização

df['total'] = (df['total']-df['total'].min()) \
    /(df['total'].max()-df['total'].min())

df['total'] = df['total'].round(3)
df = df.reset_index() 
df.drop('index', inplace=True, axis=1)


######### PROCEDIMENTO SEMELHANTE PARA DF_CLASSES #########
######### PADRONIZAR NOME DA UJ #########
# padrao é maiúsculo e sem sufixo 'g1'


df_classes['Orgao'] = df_classes['Orgao'].str.replace(' \(g1\)','')
df_classes = df_classes.rename(columns={'Orgao':'case: orgao_mun'})
df_classes['case: orgao_mun'] = df_classes['case: orgao_mun'].str.upper()
df_classes['case: orgao_mun'] = df_classes['case: orgao_mun'].\
    str.replace('"','')
df_classes['case: orgao_mun'] = df_classes['case: orgao_mun'].\
    str.replace(' - ','-')
df_classes['case: orgao_mun'] = df_classes['case: orgao_mun'].\
    str.replace('-',' - ')



######### NORMALIZAR CLASSES #########
# percentualmente por UJ

assuntos_cols = list(df_classes)
assuntos_cols.remove('case: orgao_mun')

df_classes['total'] = df_classes[assuntos_cols].sum(axis=1)
df_classes.loc[:, assuntos_cols] = \
    df_classes.loc[:, assuntos_cols].div(df_classes['total'], axis=0)

df_classes.loc[:, assuntos_cols] = \
    df_classes.loc[:, assuntos_cols].round(3)

######### NORMALIZAR COLUNA 'total' #########
# única que precisa de normalização

df_classes['total'] = (df_classes['total']-df_classes['total'].min()) \
    /(df_classes['total'].max()-df_classes['total'].min())

df_classes['total'] = df_classes['total'].round(3)
# df_classes = df_classes.reset_index() 
# df_classes.drop('index', inplace=True, axis=1)

# df_classes.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
#                       '/versao7/teste_df_classes.csv', sep=';')

######### JUNTAR CLASSE E ASSUNTO #########

# trabalhar com o total da classe
df = df.drop('total', axis=1)

# merge

df = df.merge(df_classes, on='case: orgao_mun', how='left')


######### CLUSTERIZAR COM DBSCAN ######### 
# para encontrar UJs que são semelhantes

feature_cols = list(df)
feature_cols.remove('case: orgao_mun')

X = df[feature_cols].to_numpy()
clustering = DBSCAN(eps=0.1, min_samples=10).fit(X)

clustering.labels_


######### TESTAR CLUSTERIZAÇÃO ######### 

df_cluster = pd.DataFrame(data=clustering.labels_, columns=['cluster'])

df_aux = df_cluster.copy()
df_aux['count'] = df_aux['cluster']
df_aux.groupby('cluster').count()

######### SALVAR DATAFRAME ######### 

df = df.merge(df_cluster, left_index=True, right_index=True, how='left')
df.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                      '/versao7/clusterizacao.csv', sep=';')

