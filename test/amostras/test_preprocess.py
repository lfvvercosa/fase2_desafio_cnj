from log.PreProcess import PreProcess


file_path = '/home/vercosa/Documentos/amostra_desafio_cnj/'+\
            'sample/tjba_sample.csv'

p = PreProcess(file_path)
p.select_desired_columns()

p.filter_outlier_timestamp()
p.filter_outlier_movements()
p.filter_outlier_trace_time()

print(p.df_log)
print(p.df_log.describe())
print(p.df_log.columns)