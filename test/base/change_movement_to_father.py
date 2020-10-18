import pandas as pd
import re


movement_path = '/home/vercosa/Insync/doutorado/hackaton_cnj/' + \
                'projeto_git/desafio_cnj/data/interim/df_movimentos.csv'

df_mov = pd.read_csv(movement_path,
                     engine='python')

df_mov = df_mov[['breadscrum', 'cod_item', 'nome']]
df_mov = df_mov.rename(columns={'cod_item':'concept:name_cod'})


# change movements names

reg = '\:(.*?)\:'
                    
df_mov['father_mov_code']  = df_mov['breadscrum'].str.\
                                findall(reg, flags=re.I).str[0]

df_mov['father_mov_code'].fillna(df_mov['concept:name_cod'], 
                                 inplace=True)

df_mov['father_mov_code'] = df_mov['father_mov_code'].astype(int)

df_mov.loc[((df_mov['concept:name_cod'] == 22) |
            (df_mov['concept:name_cod'] == 246)),\
             'nome'] = 'Baixa/Arquivamento'

# change 'Magistrado' movimentos to uppest father

df_mov.loc[(df_mov['father_mov_code'] == 193),\
             'nome'] = 'Julgamento'

df_mov.loc[(df_mov['father_mov_code'] == 11009),\
             'nome'] = 'Despacho'

df_mov.loc[(df_mov['father_mov_code'] == 3),\
             'nome'] = 'Decisão'









# data = {'father_mov_code': [3, 11009, 193, 865, 12522, 15, 18, 48, 104, 1, 14],
#         'father_mov': ['Decisão', 'Despacho', 'Julgamento', 'Arquivista', 
#                        'Auxiliar da Justiça','Contador','Distribuidor',
#                        'Escrivão/Diretor de Secretaria/Secretário Jurídico',
#                        'Oficial de Justiça', 'Magistrado', 'Serventuário']}


# df_mov_depara = pd.DataFrame(data)


###########

file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')

# check how many have movimentacao 'Distribuição', cod: 26

len(df_log['case: orgao'].unique().tolist())

df_query = df_log[['case: orgao', 'concept:name_cod']].drop_duplicates()
df_query[df_query['concept:name_cod'] == 12474]

# check how many have movimentacao 'Citação', 
# cod: 12284, 12286, 12288, 12287, 12285

df_query[(df_query['concept:name_cod'] == 12284) | 
         (df_query['concept:name_cod'] == 12286) | 
         (df_query['concept:name_cod'] == 12288) | 
         (df_query['concept:name_cod'] == 12287) | 
         (df_query['concept:name_cod'] == 12285)]

# check how many have 'Trânsito em Julgado', cod: 848  
df_query[df_query['concept:name_cod'] == 848]


# check how many have 'Baixa'/'Arquivamento', cod: 22/246
df_query[(df_query['concept:name_cod'] == 246)]


# check how many have 'Remessa', cod: 123
df_query[(df_query['concept:name_cod'] == 123)]


# check how many have 'Tutela', cod: 123
df_query[(df_query['concept:name_cod'] == 332) | 
         (df_query['concept:name_cod'] == 785) | 
         (df_query['concept:name_cod'] == 889) |
         (df_query['concept:name_cod'] == 817)]


# check how many have 'Audiencia', cod: diverse

df_query[(df_query['concept:name_cod'] == 12739) | 
         (df_query['concept:name_cod'] == 12624) | 
         (df_query['concept:name_cod'] == 12741) | 
         (df_query['concept:name_cod'] == 12740) | 
         (df_query['concept:name_cod'] == 12742) | 
         (df_query['concept:name_cod'] == 12749) |
         (df_query['concept:name_cod'] == 12750) | 
         (df_query['concept:name_cod'] == 12743) |
         (df_query['concept:name_cod'] == 12751) | 
         (df_query['concept:name_cod'] == 12744) |
         (df_query['concept:name_cod'] == 12752) | 
         (df_query['concept:name_cod'] == 12745) |
         (df_query['concept:name_cod'] == 12746) | 
         (df_query['concept:name_cod'] == 12747) |
         (df_query['concept:name_cod'] == 12753) |
         (df_query['concept:name_cod'] == 970)]

# check most frequent 'movimentos'

df_freq_mov = df_query.groupby('concept:name_cod').count().\
                    sort_values(by='case: orgao',
                                ascending=False)

df_freq_mov = df_freq_mov.rename(columns={'case: orgao':'count'})

df_mov_join = df_mov.rename(columns={'cod_item':'concept:name_cod'})

df_freq_mov = df_freq_mov.merge(df_mov_join[['concept:name_cod',
                               'breadscrum',
                               'nome']], 
                                on='concept:name_cod', 
                                how='left')

df_freq_mov.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                          'most_freq_movimentos.csv', sep=';')                             

