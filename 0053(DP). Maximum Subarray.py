class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        res = nums[0] # 為了處理負數，初始最大值不能設為 0

        for i in range(1,n+1):
            curr_num = nums[i-1] # 拿到當前的數字 (因為 i 從 1 開始，所以是 nums[i-1])
            dp[i] = max(curr_num,dp[i-1]+ curr_num)

            res = max(res,dp[i])
        
        return res



        
            
