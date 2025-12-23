# Leetcode, Ligmaball
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        
        # 定義 → 轉移 → 初始化 → 計算順序 → 回答
        def robline(arr):
            if len(arr) ==1:
                return arr[0]

            a = arr[0]
            b = max(arr[0], arr[1])
                  
            for i in range(2, len(arr)):
                c = max(b, a + arr[i])
                a = b
                b = c

            return b
        # 情況一：不搶最後一間
        case1 = robline(nums[0:n-1])

        # 情況二：不搶第一間
        case2 = robline(nums[1:n])

        return max(case1, case2)

                


        
