# Leetcode, Ligmaball
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # 用雜湊表紀錄 val-> idx

        for idx, val in enumerate(nums):
            # 我需要某個數字跟 val 加起來等於 target，那個數字就是 target - val
            complement = target - val
            # 如果另一半已經被紀錄過（表示之前看過 complement）
            # 那 complement 的 idx + 現在的 idx 就是答案
            if complement in seen:
                return [seen[complement], idx]
            # 否則，把現在的 val 記錄下來，以便之後遇到「它的另一半」時可以配對
            seen[val] = idx
        # 題目保證一定有答案，所以正常情況永遠不會走到這行
        return []

        

            

            
