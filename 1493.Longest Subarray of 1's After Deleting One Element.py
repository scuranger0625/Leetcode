from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0  # 最長的子陣列長度
        zero_count = 0  # 記錄0的數量
        left = 0  # 滑動窗口的左邊界

        # 使用滑動窗口技術遍歷陣列
        for right in range(len(nums)):
            # 當前窗口擴展一格
            if nums[right] == 0:
                zero_count += 1
            
            # 如果發現超過一個0，則需要調整窗口，將左邊界右移
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 計算當前窗口的長度，不包括要刪除的那一個元素（因此要-1）
            max_len = max(max_len, right - left)
        
        # 因為必須刪除一個元素，所以最終結果是max_len
        return max_len

# 測試用例
solution = Solution()
print(solution.longestSubarray([1, 1, 0, 1]))  # 輸出: 3
print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 輸出: 5
print(solution.longestSubarray([1, 1, 1]))  # 輸出: 2
