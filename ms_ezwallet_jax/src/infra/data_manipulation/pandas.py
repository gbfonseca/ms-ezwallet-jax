from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_csv('./acoes.csv', encoding='ISO-8859-1',  skiprows=2, delimiter=';')
        new_df = pd.DataFrame(df['Empresa'].values, columns=['code'])
        codes_with_flag_dict = pandas_helper.insert_country_flag(
            new_df, 'SA').to_dict('records')
        return codes_with_flag_dict
