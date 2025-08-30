class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 初始化兩個變數來追蹤最小值和次小值
        min1 = float('inf')  # 最小值
        min2 = float('inf')  # 次小值
        
        # 遍歷陣列
        for num in nums:
            # 如果當前數字比最小值還小，更新最小值
            if num <= min1:
                min1 = num
            # 如果當前數字比最小值大，比次小值小，更新次小值
            elif num <= min2:
                min2 = num
            # 如果當前數字比次小值大，說明找到三個遞增的數字
            else:
                return True
        
        # 如果遍歷結束，沒有找到符合條件的三元組，返回 False
        return False

# 測試範例
sol = Solution()

# 測試範例1: nums = [1, 2, 3, 4, 5] 應該返回 True
print(sol.increasingTriplet([1, 2, 3, 4, 5]))  # 輸出: True

# 測試範例2: nums = [5, 4, 3, 2, 1] 應該返回 False
print(sol.increasingTriplet([5, 4, 3, 2, 1]))  # 輸出: False

# 測試範例3: nums = [2, 1, 5, 0, 4, 6] 應該返回 True
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))  # 輸出: True
        
