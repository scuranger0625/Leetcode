class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]      # 右邊進來（實際加法）

            while window_sum >= target:    # 合法就縮（找最短）
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]   # 左邊出去（實際減法）
                left += 1

        return 0 if ans == float('inf') else ans
