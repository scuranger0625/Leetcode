class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # 題意：已經排序就回傳 0
        if all(nums[i] == i for i in range(n)):
            return 0

        # 將所有「不在正確位置」的值做 AND
        k = (1 << n.bit_length()) - 1
        for i, v in enumerate(nums):
            if v != i:
                k &= v
        return k
