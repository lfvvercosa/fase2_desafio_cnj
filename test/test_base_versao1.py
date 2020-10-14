import pandas as pd


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')


# get three varas with same assuntos and between 100 to 200 processes 
# to create their DFG and compare
df_vara1 = df_log[df_log['case: orgao'] == \
    'Vara Criminal e de Execuções Fiscais da comarca de Visconde do Rio Branco']
df_vara1['case:concept:name'].drop_duplicates().size
df_vara1.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                            'log_vara1.csv', sep=';', index=False)


df_vara2 = df_log[df_log['case: orgao'] == \
    '01 CUMULATIVA DE CRAVINHOS']
df_vara2['case:concept:name'].drop_duplicates().size
df_vara2.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                            'log_vara2.csv', sep=';', index=False)


df_vara3 = df_log[df_log['case: orgao'] == \
    'CURITIBA - CENTRAL DE MOVIMENTAÇÕES PROCESSUAIS - VARA DA FAZENDA PÚBLICA']
df_vara3['case:concept:name'].drop_duplicates().size
df_vara3.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                            'log_vara3.csv', sep=';', index=False)



