import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # 過濾體重大於等於 100 並按 weight 降序排列，最後返回 name 欄位作為 DataFrame
    return animals[animals['weight'] >= 100].sort_values(by='weight', ascending=False)[['name']]
