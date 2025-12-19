class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        核心思維：對撞雙指標 (Two Pointers - Opposite Direction)
        時間複雜度：O(n) - 只需要遍歷數組一次
        空間複雜度：O(1) - 僅使用常數空間儲存指針
        """
        
        # 1. 初始化左右雙指針
        # left 指向最小元素 (index 0)
        # right 指向最大元素 (index n-1)，避免 Index Out of Bounds
        left, right = 0, len(numbers) - 1
        
        # 2. 開始收縮範圍
        # 條件是 left < right，因為題目要求找兩個「不同」的數字
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # 狀況 A：找到目標值
            if current_sum == target:
                # 題目要求 1-indexed，所以回傳索引時要加 1
                return [left + 1, right + 1]
            
            # 狀況 B：當前總和小於目標值
            # 由於數組已排序 (Sorted)，為了增加總和，必須將 left 右移
            elif current_sum < target:
                left += 1
            
            # 狀況 C：當前總和大於目標值
            # 為了減小總和，必須將 right 左移
            else:
                right -= 1
        
        # 根據題目保證必有解，這行理論上不會執行到，但寫出來能展現代碼完備性
        return []

# LeetCode == Ligmaball

