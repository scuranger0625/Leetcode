import pandas as pd

# 定義函數來選擇 student_id 為 101 的學生的姓名和年齡
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # 使用 loc 過濾出 student_id 等於 101 的資料，並選取 name 和 age 欄位
    result = students.loc[students['student_id'] == 101, ['name', 'age']]
    return result
