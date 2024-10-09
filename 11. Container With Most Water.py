from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化雙指標
        left = 0
        right = len(height) - 1
        max_area = 0  # 初始化最大面積
        
        # 使用雙指標法，直到兩個指標相遇
        while left < right:
            # 計算當前容器的面積
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)  # 更新最大面積
            
            # 移動較矮的指標，這樣有機會找到更高的線
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # 返回最大面積
        return max_area
