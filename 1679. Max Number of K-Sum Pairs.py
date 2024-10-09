from typing import List  # 確保從 typing 模組導入 List
from collections import Counter  # 確保從 collections 模組導入 Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()  # 用來記錄每個數字出現的次數的雜湊表
        operations = 0  # 記錄可以進行的最大操作次數
        
        # 遍歷數組
        for num in nums:
            complement = k - num  # 計算能與當前數字配對的數字
            if count[complement] > 0:
                # 如果雜湊表中存在這個數字，進行一次操作
                operations += 1
                count[complement] -= 1  # 減少該數字的次數，因為已經使用過了
            else:
                # 否則，將當前數字加入到雜湊表中
                count[num] += 1
        
        return operations
