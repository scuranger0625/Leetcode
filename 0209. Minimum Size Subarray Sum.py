class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0                  # 左邊界
        window_sum = 0            # 目前區間的總和
        ans = float('inf')        # 最短長度（先設無限大）

        for right in range(len(nums)):
            window_sum += nums[right]   # 右指標擴張：一定要「真的加」

            # 只要目前區間總和 >= target，就嘗試縮左邊找更短
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]  # 左指標收縮：一定要「真的減」
                left += 1

        return 0 if ans == float('inf') else ans
