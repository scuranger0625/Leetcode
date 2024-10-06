import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # 使用 pivot 將 city 作為列，month 作為欄，溫度作為值
    pivoted = weather.pivot(index='city', columns='month', values='temperature')
    
    # 轉置矩陣後將 city 變成月的標籤
    pivoted = pivoted.T
    
    # 重新命名 city 為 month
    pivoted.index.name = 'month'
    
    return pivoted
