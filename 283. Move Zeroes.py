from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # 記錄非零元素的位置
        
        # 第一次遍歷：將非零元素向前移動
        for i in range(len(nums)):
            if nums[i] != 0:
                # 將非零元素移動到 last_non_zero 位置
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        # 第二次遍歷：將剩餘位置設為 0
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
