import pandas as pd


map_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
               'versao7/dadosbasicos_G1.csv'

main_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
               'versao7/movimento_estadual_G1_filtered.csv'

assuntos_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
             'projeto_git/desafio_cnj/data/interim/df_assuntos.csv'

df_map = pd.read_csv(map_path,
                          sep=';',
                          dtype=object,
                          engine='python')

df_assuntos = pd.read_csv(assuntos_path,
                          sep=',',
                          dtype=object,
                          engine='python')

df_main = pd.read_csv(main_path,
                          sep=';',
                          dtype=object,
                          engine='python')





# get root assuntos
df_assuntos['case: assunto_root'] = \
    df_assuntos['breadscrum'].str.split(':').str[0]
df_assuntos = df_assuntos[['cod_item','case: assunto_root']]
df_assuntos = df_assuntos.\
    rename(columns={'cod_item': 'case: codigo assunto_final'})


# remove null assuntos

df_map = df_map[~df_map['case: codigo assunto_final'].isna()]

# not all processes have 'assunto principal'

# explode assuntos list

df_aux = df_map[['case:concept:name', 'case: codigo assunto_final']]
df_aux = pd.DataFrame(df_aux['case: codigo assunto_final'].\
                      str.split(',').tolist(), 
                      index=df_aux['case:concept:name']).stack()


df_aux = \
    df_aux.reset_index()[[0, 'case:concept:name']] 
df_aux.columns = ['case: codigo assunto_final', 'case:concept:name']

df_aux = df_aux.rename(columns={'case: codigo assunto_final': \
                    'case: codigo assunto_final2'})

# remove outliers
upper_thres = df_aux.groupby('case:concept:name').count().\
    sort_values('case: codigo assunto_final2').quantile(.99).values[0]

df_aux2 = df_aux.groupby('case:concept:name', as_index=False).count()\
    .sort_values('case: codigo assunto_final2')

df_aux2 = df_aux2[df_aux2['case: codigo assunto_final2'] < upper_thres]

key = ['case:concept:name']
i1 = df_aux.set_index(key).index
i2 = df_aux2.set_index(key).index

df_aux = df_aux[i1.isin(i2)]

df_map = df_map.drop_duplicates('case:concept:name')\
    [['case:concept:name']]

df_map = df_aux.merge(df_map, on='case:concept:name', how='left')

df_main = df_main.drop_duplicates('case:concept:name')\
    [['case:concept:name','case: orgao_mun']]

df_map = df_map.merge(df_main, on='case:concept:name', how='right')
df_map = df_map[~df_map['case: codigo assunto_final2'].isna()]


# merge with assuntos root

df_map = df_map.rename(columns={'case: codigo assunto_final2': \
                    'case: codigo assunto_final',
                    'case: orgao': 'case: orgao_mun'})

df_map = df_map.merge(df_assuntos, 
                      on='case: codigo assunto_final', 
                      how='left')


df_map.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao7/assuntos_mapping.csv', 
              sep=';', 
              index=False)

