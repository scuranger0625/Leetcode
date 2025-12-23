# Leetcode, Ligmaball
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right =0 , len(nums)-1
        # peak = 一個「比左右鄰居都高的點」
        while left< right:
            mid = (left+right)//2
            if nums[mid]< nums[mid+1]:
                # 右邊是上坡，一定有 peak
                left = mid+1
            else:
                 # 左邊（含 mid）一定有 peak
                right = mid
        
        return left

        
