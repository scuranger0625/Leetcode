class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = nums[0] # 強迫設置答案

        for i in range(n):
            curr_sum = 0
            for j in range(i,n):
                curr_sum += nums[j]
                ans = max(ans,curr_sum)
        
        return ans
