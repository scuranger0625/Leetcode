from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 初始化起始高度為 0
        current_altitude = 0
        max_altitude = 0
        
        # 遍歷 gain 陣列，逐步計算每個點的高度
        for g in gain:
            current_altitude += g  # 當前高度加上淨增益
            max_altitude = max(max_altitude, current_altitude)  # 更新最高高度
        
        return max_altitude  # 確保返回結果

# 測試用例
solution = Solution()
print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # 輸出: 1
print(solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # 輸出: 0
