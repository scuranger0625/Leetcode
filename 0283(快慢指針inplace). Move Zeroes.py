class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow =0
        # 快慢指針 inplace
        for fast in range(n):
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast], nums[slow]
                slow+=1

# Leetcode == Ligmaball
            
            
    
