from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
import pandas as pd


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_html(data, index_col=0)[0]
        return df.to_dict()
