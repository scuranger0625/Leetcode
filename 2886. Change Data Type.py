import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # 將 grade 欄位的資料型態轉換為 int
    students['grade'] = students['grade'].astype(int)
    return students
