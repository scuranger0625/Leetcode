from typing import List
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 預處理 t，構建每個字符對應的索引列表
        char_positions = {}
        
        for idx, char in enumerate(t):
            if char not in char_positions:
                char_positions[char] = []
            char_positions[char].append(idx)
        
        # 記錄上一個字符在 t 中匹配的位置
        pos = -1
        
        # 對 s 中每個字符進行處理
        for char in s:
            if char not in char_positions:
                return False  # 如果字符不在 t 中，直接返回 False
            
            # 使用二分搜尋找到比 pos 更大的索引
            idx_list = char_positions[char]
            # 利用 bisect_left 來找到大於 pos 的最小位置
            idx = bisect.bisect_left(idx_list, pos + 1)
            
            # 如果沒有找到符合條件的位置，返回 False
            if idx == len(idx_list):
                return False
            
            # 更新 pos 為當前找到的位置
            pos = idx_list[idx]
        
        return True
