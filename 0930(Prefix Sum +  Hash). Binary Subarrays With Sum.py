from collections import defaultdict

# Leetcode, Ligmaball
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 用來「記錄某個數值出現過幾次」的計數器 每個 key 對應一個計數器，而且這些計數器一開始都從 0 開始。
        count = defaultdict(int)
        # 很重要：代表「什麼都還沒選」
        count[0]=1 

        prefix=0
        ans=0

        for x in nums:
            prefix += x
            # 所有以前累積和是 prefix - goal 的位置，都可以跟我現在這個位置組成一個和為 goal 的子陣列，所以要把它們的數量全部加進答案。
            # O(n²) 的「枚舉所有子陣列」
            # 變成 O(1) 的「查表加法」
            # Prefix Sum + Hash
            ans += count[prefix - goal]
            count[prefix] += 1

        return ans
            



        
