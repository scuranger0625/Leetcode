import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # 遍歷每一行，檢查 name 欄位是否為 None
    for index, row in students.iterrows():
        if row['name'] is None:  # 如果 name 欄位為 None
            students = students.drop(index)  # 刪除該行
            
    return students