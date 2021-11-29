from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_html(data)[0]
        renamed_df = pandas_helper.rename_stock(df)
        codes_dict = renamed_df['code'].to_frame().to_dict('records')
        return codes_dict
