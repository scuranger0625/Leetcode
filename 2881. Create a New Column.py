import pandas as pd

# 定義函式 createBonusColumn
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # 新增 bonus 欄位，值為 salary 的兩倍
    employees['bonus'] = employees['salary'] * 2
    return employees