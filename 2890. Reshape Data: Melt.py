import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # 使用 pd.melt 將寬格式轉換為長格式
    reshaped = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    
    # 保持 product 欄位不變並返回長格式
    return reshaped
