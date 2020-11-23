import pandas as pd

file_path5 = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao5/version_5.csv'

file_path6 = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
             'versao6/resultado_1_0_null.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df5 = pd.read_csv(file_path5,
                  dtype=datatypes,
                  sep=';', 
                  engine='python')

df6 = pd.read_csv(file_path6,
                  dtype=datatypes,
                  sep=';', 
                  engine='python')

df5['case: orgao_mun'] = df5['case: orgao_mun'].str.upper()
df5['case: orgao_mun'] = df5['case: orgao_mun'].\
    str.replace(' - ','-')
df5['case: orgao_mun'] = df5['case: orgao_mun'].\
    str.replace('-',' - ')

df6['case: orgao_mun'] = df6['case: orgao_mun'].str.upper()
df6['case: orgao_mun'] = df6['case: orgao_mun'].\
    str.replace(' - ','-')
df6['case: orgao_mun'] = df6['case: orgao_mun'].\
    str.replace('-',' - ')

df5[df5['case: orgao_mun'] == \
    'V DOS FEITOS DE REL DE CONS CIV E COMERCIAIS DE SANTA'+\
    ' MARIA DA VITÓRIA - TJBA'].drop_duplicates('case:concept:name')

df6[df6['case: orgao_mun'] == \
    'V DOS FEITOS DE REL DE CONS CIV E COMERCIAIS DE SANTA'+\
    ' MARIA DA VITÓRIA - TJBA'].drop_duplicates('case:concept:name')


df5[df5['case: orgao_mun'].str.contains(\
'VARA DO JUIZADO ESPECIAL CÍVEL - TJAM')]