class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7 

        # left & right hash
        left = Counter()
        right = Counter(nums)

        result = 0

        for i in range(len(nums)):
            right[nums[i]] -= 1

            double = nums[i]*2
            left_count = left[double]
            right_count = right[double]

            result += left_count * right_count

            left[nums[i]] += 1
        return result % MOD
