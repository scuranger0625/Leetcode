import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # 使用 rename 函數直接替換欄位名稱
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })
    return students

    