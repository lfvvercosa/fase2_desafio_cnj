import pandas as pd
from utils.System import DEBUG


class PreProcess():
    def __init__(self, 
                 file_location,
                 datatypes={'case:concept:name': str,
                            'time:timestamp'   : str},
                 sep=';',
                 engine='python'):

        self.df_log = pd.read_csv(file_location,
                                  dtype=datatypes,
                                  sep=sep, 
                                  engine=engine)
    

    def select_desired_columns(self, l=['case:concept:name',
                                        'concept:name',
                                        'concept:name_cod',
                                        'time:timestamp']):

        self.df_log = self.df_log[l]

    def filter_outlier_timestamp(self):
        self.df_log['time:timestamp'] = self.df_log['time:timestamp'].str.strip()
        
        df_incomplete = self.df_log[['case:concept:name', 'time:timestamp']]
        df_incomplete['year'] = df_incomplete['time:timestamp'].str[:4].astype(int)
        df_incomplete = df_incomplete[(df_incomplete['year'] < 1900) | \
                                    (df_incomplete['year'] > 2020)]
        df_incomplete = df_incomplete.drop_duplicates(subset=['case:concept:name'])
        
        key = ['case:concept:name']
        i1 = self.df_log.set_index(key).index
        i2 = df_incomplete.set_index(key).index

        if(DEBUG):
            before = self.df_log['case:concept:name'].nunique()

        self.df_log = self.df_log[~i1.isin(i2)]

        if(DEBUG):
            after = self.df_log['case:concept:name'].nunique()
            print('incorrect timestamps filtered: ', (before - after))
            print('total traces after: ', after)

        self.df_log['time:timestamp'] = \
                pd.to_datetime(self.df_log['time:timestamp'], 
                               utc=True, 
                               format='%Y%m%d%H%M%S')


    def filter_outlier_movements(self, lower=0.05, upper=0.95):
        df_hist = self.df_log.groupby('case:concept:name').count().\
            sort_values('concept:name')

        lower_bound = df_hist['concept:name'].quantile(lower)
        upper_bound = df_hist['concept:name'].quantile(upper)
        df_hist = df_hist[(df_hist['concept:name'] < lower_bound) |
                        (df_hist['concept:name'] > upper_bound)]
        df_hist.reset_index(level=0, inplace=True)

        key = ['case:concept:name']
        i1 = self.df_log.set_index(key).index
        i2 = df_hist.set_index(key).index

        if(DEBUG):
            before = self.df_log['case:concept:name'].nunique()

        self.df_log = self.df_log[~i1.isin(i2)]

        if(DEBUG):
            after = self.df_log['case:concept:name'].nunique()
            print('movement outliers filtered: ', (before - after))
            print('total traces after: ', after)
        

    def filter_outlier_trace_time(self, lower=0.05, upper=0.95):
        df_time = self.df_log.copy()
        df_time['time:timestamp2'] = df_time['time:timestamp']

        df_time = df_time.groupby('case:concept:name').\
                    agg({'time:timestamp' : min, 'time:timestamp2': max})
        df_time['duration'] = \
            (df_time['time:timestamp2'] - df_time['time:timestamp']).dt.days

        lower_bound = int(df_time.quantile(lower))
        upper_bound = int(df_time.quantile(upper))

        df_time = df_time[(df_time['duration'] < lower_bound) |
                        (df_time['duration'] > upper_bound)]
        df_time.reset_index(level=0, inplace=True)

        key = ['case:concept:name']
        i1 = self.df_log.set_index(key).index
        i2 = df_time.set_index(key).index

        if(DEBUG):
            before = self.df_log['case:concept:name'].nunique()

        self.df_log = self.df_log[~i1.isin(i2)]

        if(DEBUG):
            after = self.df_log['case:concept:name'].nunique()
            print('trace time outliers filtered: ', (before - after))
            print('total traces after: ', after)

