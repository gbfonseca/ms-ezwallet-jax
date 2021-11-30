from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_html(data)[0]
        renamed_df = pandas_helper.rename_stock(df)
        codes = renamed_df['code'].to_frame()
        codes_with_flag_dict = pandas_helper.insert_country_flag(
            codes, 'SA').to_dict('records')
        return codes_with_flag_dict
