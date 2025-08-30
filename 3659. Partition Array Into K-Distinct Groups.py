from typing import List
from collections import Counter

# 雜湊函式
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # 特例:必須能被整除
        if n % k != 0:
            return False
        
        group_count = n // k # 群組總數 = 元素數目 / k
        freq = Counter(nums)

        # 檢查並避免同籠問題
        for cnt in freq.values():
            if cnt > group_count: # 同一數字不可>群組數量
                return False

        return True       
        
