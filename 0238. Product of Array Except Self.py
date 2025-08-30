from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # 初始化答案陣列為 1

        # 計算每個位置左邊的乘積
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 計算每個位置右邊的乘積，並同時更新答案陣列
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

# 測試範例
sol = Solution()
nums = [1, 2, 3, 4]
output = sol.productExceptSelf(nums)
print(output)  # 輸出: [24, 12, 8, 6]
