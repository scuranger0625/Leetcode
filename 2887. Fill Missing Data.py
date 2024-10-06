import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # 將 quantity 欄位中的 None 值填充為 0
    products['quantity'] = products['quantity'].fillna(0)
    return products
