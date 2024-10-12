from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 計算整個數組的總和
        total_sum = sum(nums)
        left_sum = 0  # 初始化左側和為 0

        # 使用二元搜尋法來找到樞軸索引
        for i in range(len(nums)):
            # 右側和可以用總和減去當前元素和左側和計算
            right_sum = total_sum - left_sum - nums[i]
            
            # 如果左側和等於右側和，則返回該索引
            if left_sum == right_sum:
                return i
            
            # 更新左側和
            left_sum += nums[i]

        # 如果沒找到，返回 -1
        return -1
