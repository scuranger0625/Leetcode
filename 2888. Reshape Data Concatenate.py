import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # 透過 pd.concat 合併 df1 和 df2
    return pd.concat([df1, df2], ignore_index=True)

    