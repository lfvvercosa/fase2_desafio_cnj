import pandas as pd


file_path = '/home/vercosa/Documentos/bases_desafio_cnj/'+\
            'versao1.csv'

datatypes = {'case:concept:name': str,
             'time:timestamp'   : str}

df_log = pd.read_csv(file_path,
                     dtype=datatypes,
                     sep=';', 
                     engine='python')


# check distincts
df_log['case:tribunal'].unique().tolist()
df_log['case:grau'].unique().tolist()

df_log['concept:name'].unique().tolist()
len(df_log['concept:name'].unique().tolist())

df_log['case: ano'].unique().tolist()
len(df_log['case: ano'].unique().tolist())

df_log['case: codigo assunto_final'].unique().tolist()
len(df_log['case: codigo assunto_final'].unique().tolist())

df_log['case: orgao'].unique().tolist()
len(df_log['case: orgao'].unique().tolist())


# check how many encoding errors
l1 = [x for x in df_log['case: orgao'].unique().tolist()] 
l2 = [x for x in df_log['case: orgao'].unique().tolist()] 
l2 = [x.encode('latin-1', errors='ignore').decode('latin-1') for x in l2]

count = 0 

for i in range(len(l1)): 
    if l1[i] == l2[i]: 
        count += 1 

count


# check varas with same 'assuntos'
df_sim = df_log[['case: orgao', 'case: codigo assunto_final']].drop_duplicates()
df_sim['case: orgao'] = df_sim['case: orgao'].str.strip()
df_sim = df_sim.groupby('case: orgao')['case: codigo assunto_final'].\
    apply(list).reset_index(name='assuntos')

df_sim['assuntos'] = df_sim['assuntos'].astype(str) 


df_sim = df_sim.groupby('assuntos')['case: orgao'].\
    apply(list).reset_index(name='varas')
df_sim['numero_varas'] = df_sim['varas'].str.len()                          
df_sim = df_sim.sort_values(by='numero_varas')

df_sim.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                          'varas_por_assuntos.csv')


# check number of process by vara
df_proc = df_log[['case: orgao', 'case:concept:name']].drop_duplicates()
df_proc = df_proc.groupby('case: orgao').count().sort_values(by='case:concept:name')
df_proc = df_proc.rename(columns={'case:concept:name':'process_count'})
df_proc.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                          'processos_por_vara.csv')


# find number of process from varas of category 68
l = df_sim[df_sim['numero_varas'] == 68]['varas'].tolist()[0]
df_cat68 = pd.DataFrame(l, columns=['case: orgao'])
df_cat68 = df_cat68.merge(df_proc, on='case: orgao', how='left')
df_cat68 = df_cat68.sort_values(by='process_count')
df_cat68.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                          'processos_grupo_68.csv')


# find number of process from varas of category 523
l = df_sim[df_sim['numero_varas'] == 523]['varas'].tolist()[0]
df_cat68 = pd.DataFrame(l, columns=['case: orgao'])
df_cat68 = df_cat68.merge(df_proc, on='case: orgao', how='left')
df_cat68 = df_cat68.sort_values(by='process_count')
df_cat68.to_csv(path_or_buf='/home/vercosa/Documentos/bases_desafio_cnj/'+\
                          'processos_grupo_523.csv')

