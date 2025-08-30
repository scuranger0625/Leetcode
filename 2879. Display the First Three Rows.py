import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # 使用 iloc 選取前三行
    result = employees.iloc[0:3]
    return result
