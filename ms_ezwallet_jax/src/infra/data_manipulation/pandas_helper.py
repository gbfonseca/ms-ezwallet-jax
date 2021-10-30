from pandas import DataFrame
import locale
from locale import atof


class PandasHelper():
    def remove_percent(self, df: DataFrame) -> DataFrame:
        df['Div.Yield'] = df['Div.Yield'].str.rstrip('%')
        df['Mrg. Líq.'] = df['Mrg. Líq.'].str.rstrip('%')
        df['Mrg Ebit'] = df['Mrg Ebit'].str.rstrip('%')
        df['ROIC'] = df['ROIC'].str.rstrip('%')
        df['ROE'] = df['ROE'].str.rstrip('%')
        df['Cresc. Rec.5a'] = df['Cresc. Rec.5a'].str.rstrip('%')
        return df

    def convert_fields_to_number(self, df: DataFrame) -> DataFrame:
        df_papel = df['Papel']
        df.drop(df.columns[0], axis=1, inplace=True)
        locale.setlocale(locale.LC_NUMERIC, '')
        df = df.applymap(lambda value: atof(str(value)))
        df['Papel'] = df_papel
        return df


pandas_helper = PandasHelper()
