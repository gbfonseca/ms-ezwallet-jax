from pandas import DataFrame


class PandasHelper():
    def remove_percent(df: DataFrame) -> DataFrame:
        df['Div.Yield'] = df['Div.Yield'].str.rstrip('%')
        df['Mrg. Líq.'] = df['Mrg. Líq.'].str.rstrip('%')
        df['Mrg Ebit'] = df['Mrg Ebit'].str.rstrip('%')
        df['ROIC'] = df['ROIC'].str.rstrip('%')
        df['ROE'] = df['ROE'].str.rstrip('%')
        df['Cresc. Rec.5a'] = df['Cresc. Rec.5a'].str.rstrip('%')
        return df


pandas_helper = PandasHelper()
