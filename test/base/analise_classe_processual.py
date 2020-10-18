import pandas as pd


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'dados_basicos_estadual/df_dadosbasicos_justica_estadual.csv'

df = pd.read_csv(file_path,
                 sep=',', 
                 engine='python')

print('####################')
print('check distincts')
print('####################')

df['dadosBasicos.orgaoJulgador.nomeOrgao'].unique().tolist()
len(df['dadosBasicos.orgaoJulgador.nomeOrgao'].unique().tolist())

df['dadosBasicos.classeProcessual'].unique().tolist()
len(df['dadosBasicos.classeProcessual'].unique().tolist())


df_group = df[['dadosBasicos.orgaoJulgador.nomeOrgao',
               'dadosBasicos.classeProcessual']].drop_duplicates()

df_group = df_group.groupby('dadosBasicos.orgaoJulgador.nomeOrgao')\
                ['dadosBasicos.classeProcessual'].\
                apply(list).reset_index(name='classes')

df_group['numero_classes'] = df_group['classes'].str.len()

df_group = df_group.sort_values(by='numero_classes')

