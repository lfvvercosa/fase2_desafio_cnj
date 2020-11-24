import pandas as pd
import re


map_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
               'versao7/movimento_estadual_G1_filtered.csv'


classes_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
             'projeto_git/desafio_cnj/data/interim/df_classes.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_map = pd.read_csv(map_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')

df_map = df_map.drop_duplicates(subset=['case:concept:name'])                         

df_classes = pd.read_csv(classes_path,
                         dtype=datatypes,
                         sep=',', 
                         engine='python')


# get root class
df_classes['case: classe_root'] = \
    df_classes['breadscrum'].str.split(':').str[0]
df_classes = df_classes[['cod_item','case: classe_root']]
df_classes = df_classes.rename(columns={'cod_item': 'case: classe'})

df_map = df_map.merge(df_classes, on='case: classe', how='left')

df_map['case: orgao_mun'] = df_map['case: orgao_mun'].str.upper()
df_map['case: orgao_mun'] = df_map['case: orgao_mun'].\
    str.replace(' - ','-')
df_map['case: orgao_mun'] = df_map['case: orgao_mun'].\
    str.replace('-',' - ')

df_map = df_map[['case:concept:name', 'case: orgao_mun', 'case: classe_root']]

df_map.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                           '/versao7/classes_mapping.csv', 
              sep=';', 
              index=False)


