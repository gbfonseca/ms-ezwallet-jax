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

    def convert_price_to_correct_value(self, df: DataFrame) -> DataFrame:
        df['Cotação'] = df['Cotação'] / 100
        return df

    def remap_field_values(self, df: DataFrame) -> DataFrame:
        df = df.rename(
            columns={'Div.Yield': 'div_yield', 'P/Cap.Giro': 'p/cap_giro', 'P/Ativ Circ.Liq': 'p/ativ_circ_liq', 'Mrg. Líq.': 'mrg_liq', 'Liq. Corr.': 'liq_corr', 'Liq.2meses': 'liq_2_meses', 'Patrim. Líq': 'patrim_liq', 'Dív.Brut/ Patrim.': 'div_brut/patrim', 'Cresc. Rec.5a': 'cresc_rec_5a'})
        return df

    def rename_stock(self, df: DataFrame) -> DataFrame:
        renamed_df = df.rename(columns={'Papel': 'code'})
        return renamed_df


pandas_helper = PandasHelper()
