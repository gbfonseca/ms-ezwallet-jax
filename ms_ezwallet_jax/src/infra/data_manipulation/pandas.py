from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_csv('./acoes.csv', encoding='ISO-8859-1',
                         skiprows=2, delimiter=';')
        new_df = pd.DataFrame(df['Empresa'].values, columns=['code'])
        new_df = pandas_helper.insert_country_flag(
            new_df, 'SA')
        new_df['indexes'] = df['Código'].values
        new_df['indexes'] = new_df['indexes'].str.split(',')
        new_df = new_df.sort_values(by='code', ascending=True)
        stocks = new_df.to_dict('records')
        return stocks
