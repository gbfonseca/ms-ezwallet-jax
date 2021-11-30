from pandas import DataFrame
import locale
from locale import atof


class PandasHelper():
    def insert_country_flag(self, df: DataFrame, flag: str) -> DataFrame:
        df_with_flag = df.applymap(lambda value: "{}.{}".format(value, flag))
        return df_with_flag

    def rename_stock(self, df: DataFrame) -> DataFrame:
        renamed_df = df.rename(columns={'Papel': 'code'})
        return renamed_df


pandas_helper = PandasHelper()
