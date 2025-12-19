class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 雙指針前提：一定要先排序
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n):
            # 去重邏輯 (1)：如果固定住的第一個數字跟上一個一樣，直接跳過
            # 這是為了避免產生重複的三元組起點
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # --- 以下就是你擅長的 Two Sum II 模板 ---
            target = -nums[i]
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 去重邏輯 (2)：找到答案後，如果左指針下一個數字一樣，跳過它
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重邏輯 (3)：找到答案後，如果右指針前一個數字一樣，跳過它
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 找到答案後，兩邊都要往內縮一步
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return res

    # Leetcode == Ligmaball
