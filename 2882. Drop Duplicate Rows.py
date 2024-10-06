import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # 刪除重複的 email，只保留第一次出現的行
    result = customers.drop_duplicates(subset=['email'], keep='first')
    return result
