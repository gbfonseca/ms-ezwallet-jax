from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_html(data)[0]
        df = pandas_helper.remove_percent(df)
        df = pandas_helper.convert_fields_to_number(df)
        df = pandas_helper.convert_price_to_correct_value(df)
        df = pandas_helper.remap_field_values(df)
        return df.to_dict('records')
