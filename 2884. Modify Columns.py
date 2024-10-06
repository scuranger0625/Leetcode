import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # 將 salary 欄位的值乘以 2
    employees['salary'] = employees['salary'] * 2
    return employees
