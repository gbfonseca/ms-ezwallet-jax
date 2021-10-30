from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from .pandas_helper import pandas_helper
import pandas as pd
import locale
from locale import atof


class DataManipulationAdapter(DataManipulation):
    def to_dict(self, data: str):
        df = pd.read_html(data)[0]

        df = pandas_helper.remove_percent(df)

        df_papel = df['Papel']
        df.drop(df.columns[0], axis=1, inplace=True)
        locale.setlocale(locale.LC_NUMERIC, '')
        df = df.applymap(lambda value: atof(str(value)))
        df['Papel'] = df_papel

        df['Cotação'] = df['Cotação'] / 100

        df = df.rename(
            columns={'Div.Yield': 'div_yield', 'P/Cap.Giro': 'p/cap_giro', 'P/Ativ Circ.Liq': 'p/ativ_circ_liq', 'Mrg. Líq.': 'mrg_liq', 'Liq. Corr.': 'liq_corr', 'Liq.2meses': 'liq_2_meses', 'Patrim. Líq': 'patrim_liq', 'Dív.Brut/ Patrim.': 'div_brut/patrim', 'Cresc. Rec.5a': 'cresc_rec_5a'})
        return df.to_dict('records')
