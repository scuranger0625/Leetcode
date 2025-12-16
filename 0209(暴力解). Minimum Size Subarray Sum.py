# （O(n²)，一定 TLE）

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # 固定左端點 i
        for i in range(n):
            curr_sum = 0

            # 右端點 j 往右擴展
            for j in range(i, n):
                curr_sum += nums[j]

                # 每一對 (i, j) 都是一個連續子陣列
                if curr_sum >= target:
                    ans = min(ans, j - i + 1)
                    # 注意：這裡「不 break」，因為我們是在學暴力
                    # （break 是優化，不是暴力本質）

        return 0 if ans == float('inf') else ans
