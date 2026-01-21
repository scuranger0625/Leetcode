# Leetcode, Ligmaball
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur =0
        min_cur = 0

        for x in nums:
            cur += x
            min_cur = min(min_cur, cur)
        
        return 1 - min_cur
